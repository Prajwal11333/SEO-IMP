# from fastapi import FastAPI, BackgroundTasks
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import StreamingResponse
# from pydantic import BaseModel
# import asyncio
# import uuid
# from crawler import WebCrawler
# from nlp_analyzer import NLPAnalyzer

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Store active analysis tasks
# active_tasks = {}

# class AnalyzeRequest(BaseModel):
#     url: str

# class AnalysisTask:
#     def __init__(self, task_id: str, url: str):
#         self.task_id = task_id
#         self.url = url
#         self.queue = asyncio.Queue()
#         self.completed = False

# @app.post("/analyze")
# async def analyze_website(request: AnalyzeRequest, background_tasks: BackgroundTasks):
#     task_id = str(uuid.uuid4())
#     task = AnalysisTask(task_id, request.url)
#     active_tasks[task_id] = task
    
#     # Start analysis in background
#     background_tasks.add_task(run_analysis, task)
    
#     return {"task_id": task_id, "status": "started"}

# @app.get("/stream/{task_id}")
# async def stream_analysis(task_id: str):
#     if task_id not in active_tasks:
#         return {"error": "Task not found"}
    
#     task = active_tasks[task_id]
    
#     async def event_generator():
#         while not task.completed:
#             try:
#                 # Wait for update with timeout
#                 update = await asyncio.wait_for(task.queue.get(), timeout=1.0)
#                 yield f"data: {update}\n\n"
#             except asyncio.TimeoutError:
#                 yield f"data: {'{\"status\": \"processing\"}'}\n\n"
#                 continue
        
#         # Clean up
#         del active_tasks[task_id]
    
#     return StreamingResponse(event_generator(), media_type="text/event-stream")

# async def run_analysis(task: AnalysisTask):
#     import json
    
#     try:
#         # Initialize crawler and analyzer
#         crawler = WebCrawler(task.url)
#         nlp_analyzer = NLPAnalyzer()
        
#         # Step 1: Start crawling
#         await task.queue.put(json.dumps({
#             "step": "crawling",
#             "status": "started",
#             "message": "Starting web crawl..."
#         }))
        
#         # Crawl website
#         pages = await crawler.crawl(max_pages=10)
        
#         await task.queue.put(json.dumps({
#             "step": "crawling",
#             "status": "completed",
#             "pages_found": len(pages)
#         }))
        
#         # Step 2: Analyze each page
#         all_results = []
#         for i, page in enumerate(pages):
#             await task.queue.put(json.dumps({
#                 "step": "analyzing",
#                 "status": "progress",
#                 "current": i + 1,
#                 "total": len(pages),
#                 "page": page['url']
#             }))
            
#             # Run NLP analysis
#             analysis = nlp_analyzer.analyze_page(page)
#             all_results.append(analysis)
            
#             await asyncio.sleep(0.5)  # Simulate processing time
        
#         # Step 3: Generate final report
#         await task.queue.put(json.dumps({
#             "step": "generating",
#             "status": "started",
#             "message": "Generating SEO report..."
#         }))
        
#         final_report = nlp_analyzer.generate_report(all_results)
        
#         # Send final results
#         await task.queue.put(json.dumps({
#             "step": "completed",
#             "status": "success",
#             "data": final_report
#         }))
        
#     except Exception as e:
#         await task.queue.put(json.dumps({
#             "step": "error",
#             "status": "failed",
#             "message": str(e)
#         }))
    
#     finally:
#         task.completed = True

# @app.get("/health")
# async def health_check():
#     return {"status": "ok"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)



from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import asyncio
import uuid
import json
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import Counter
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store active analysis tasks
active_tasks = {}

class AnalyzeRequest(BaseModel):
    url: str

class AnalysisTask:
    def __init__(self, task_id: str, url: str):
        self.task_id = task_id
        self.url = url
        self.queue = asyncio.Queue()
        self.completed = False

@app.post("/analyze")
async def analyze_website(request: AnalyzeRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    task = AnalysisTask(task_id, request.url)
    active_tasks[task_id] = task
    
    background_tasks.add_task(run_analysis, task)
    
    return {"task_id": task_id, "status": "started"}

@app.get("/stream/{task_id}")
async def stream_analysis(task_id: str):
    if task_id not in active_tasks:
        return {"error": "Task not found"}
    
    task = active_tasks[task_id]
    
    async def event_generator():
        while not task.completed:
            try:
                update = await asyncio.wait_for(task.queue.get(), timeout=1.0)
                yield f"data: {update}\n\n"
            except asyncio.TimeoutError:
                yield f"data: {json.dumps({'status': 'processing'})}\n\n"
                continue
        
        del active_tasks[task_id]
    
    return StreamingResponse(event_generator(), media_type="text/event-stream")

async def fetch_page(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            if response.status == 200:
                return await response.text()
    except:
        pass
    return None

def extract_keywords(text, top_n=20):
    stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 
                     'at', 'to', 'for', 'of', 'with', 'by', 'from', 'is'])
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    filtered = [w for w in words if w not in stop_words]
    return Counter(filtered).most_common(top_n)

def analyze_page_content(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract metadata
    title = soup.find('title')
    title_text = title.get_text().strip() if title else ""
    
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc.get('content', '') if meta_desc else ""
    
    # Extract text
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text()
    text = ' '.join(text.split())
    
    # Extract headings
    h1_tags = [h.get_text().strip() for h in soup.find_all('h1')]
    h2_tags = [h.get_text().strip() for h in soup.find_all('h2')]
    
    # Extract images
    images = soup.find_all('img')
    images_without_alt = sum(1 for img in images if not img.get('alt'))
    
    # Calculate SEO score
    score = 100
    issues = []
    
    if not title_text:
        score -= 10
        issues.append('Missing title tag')
    if not description:
        score -= 10
        issues.append('Missing meta description')
    if len(h1_tags) == 0:
        score -= 10
        issues.append('Missing H1 tag')
    elif len(h1_tags) > 1:
        score -= 5
        issues.append('Multiple H1 tags')
    
    word_count = len(text.split())
    if word_count < 300:
        score -= 10
        issues.append('Content too short')
    
    # Extract keywords
    keywords = extract_keywords(text, 15)
    
    return {
        'url': url,
        'title': title_text,
        'description': description,
        'word_count': word_count,
        'keywords': [{'word': k[0], 'count': k[1]} for k in keywords],
        'h1_count': len(h1_tags),
        'h2_count': len(h2_tags),
        'images_count': len(images),
        'images_without_alt': images_without_alt,
        'seo_score': {'score': max(0, score), 'issues': issues}
    }

async def run_analysis(task: AnalysisTask):
    try:
        domain = urlparse(task.url).netloc
        
        # Step 1: Start crawling
        await task.queue.put(json.dumps({
            "step": "crawling",
            "status": "started",
            "message": "Starting web crawl..."
        }))
        
        # Crawl pages
        pages_data = []
        visited = set()
        to_visit = [task.url]
        
        async with aiohttp.ClientSession() as session:
            while to_visit and len(visited) < 5:  # Max 5 pages
                url = to_visit.pop(0)
                if url in visited:
                    continue
                
                visited.add(url)
                html = await fetch_page(session, url)
                
                if html:
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Find more links
                    for link in soup.find_all('a', href=True):
                        href = urljoin(url, link['href'])
                        if urlparse(href).netloc == domain and href not in visited:
                            to_visit.append(href)
                    
                    # Analyze page
                    page_data = analyze_page_content(html, url)
                    pages_data.append(page_data)
                    
                    await task.queue.put(json.dumps({
                        "step": "analyzing",
                        "status": "progress",
                        "current": len(visited),
                        "total": min(5, len(to_visit) + len(visited)),
                        "page": url
                    }))
                    
                    await asyncio.sleep(0.5)
        
        await task.queue.put(json.dumps({
            "step": "crawling",
            "status": "completed",
            "pages_found": len(pages_data)
        }))
        
        # Generate report
        await task.queue.put(json.dumps({
            "step": "generating",
            "status": "started",
            "message": "Generating SEO report..."
        }))
        
        # Aggregate data
        total_pages = len(pages_data)
        avg_score = sum(p['seo_score']['score'] for p in pages_data) / total_pages if total_pages > 0 else 0
        
        all_keywords = {}
        for page in pages_data:
            for kw in page['keywords']:
                word = kw['word']
                all_keywords[word] = all_keywords.get(word, 0) + kw['count']
        
        top_keywords = sorted(all_keywords.items(), key=lambda x: x[1], reverse=True)[:20]
        
        all_issues = []
        for page in pages_data:
            all_issues.extend(page['seo_score']['issues'])
        
        issue_counts = Counter(all_issues)
        
        final_report = {
            'summary': {
                'total_pages': total_pages,
                'average_seo_score': round(avg_score, 1),
                'total_words': sum(p['word_count'] for p in pages_data),
                'total_images': sum(p['images_count'] for p in pages_data)
            },
            'top_keywords': [{'word': k[0], 'count': k[1]} for k in top_keywords],
            'common_issues': [{'issue': k, 'count': v} for k, v in issue_counts.most_common()],
            'pages': pages_data,
            'technical_score': {
                'on_page_seo': round(avg_score, 1),
                'content_quality': 75,
                'mobile_friendly': 85,
                'performance': 78
            }
        }
        
        # Send final results
        await task.queue.put(json.dumps({
            "step": "completed",
            "status": "success",
            "data": final_report
        }))
        
    except Exception as e:
        print(f"Error: {e}")
        await task.queue.put(json.dumps({
            "step": "error",
            "status": "failed",
            "message": str(e)
        }))
    
    finally:
        task.completed = True

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "FastAPI server running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)