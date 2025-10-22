# # # # # # from fastapi import FastAPI, BackgroundTasks
# # # # # # from fastapi.middleware.cors import CORSMiddleware
# # # # # # from fastapi.responses import StreamingResponse
# # # # # # from pydantic import BaseModel
# # # # # # import asyncio
# # # # # # import uuid
# # # # # # from crawler import WebCrawler
# # # # # # from nlp_analyzer import NLPAnalyzer

# # # # # # app = FastAPI()

# # # # # # app.add_middleware(
# # # # # #     CORSMiddleware,
# # # # # #     allow_origins=["*"],
# # # # # #     allow_credentials=True,
# # # # # #     allow_methods=["*"],
# # # # # #     allow_headers=["*"],
# # # # # # )

# # # # # # # Store active analysis tasks
# # # # # # active_tasks = {}

# # # # # # class AnalyzeRequest(BaseModel):
# # # # # #     url: str

# # # # # # class AnalysisTask:
# # # # # #     def __init__(self, task_id: str, url: str):
# # # # # #         self.task_id = task_id
# # # # # #         self.url = url
# # # # # #         self.queue = asyncio.Queue()
# # # # # #         self.completed = False

# # # # # # @app.post("/analyze")
# # # # # # async def analyze_website(request: AnalyzeRequest, background_tasks: BackgroundTasks):
# # # # # #     task_id = str(uuid.uuid4())
# # # # # #     task = AnalysisTask(task_id, request.url)
# # # # # #     active_tasks[task_id] = task
    
# # # # # #     # Start analysis in background
# # # # # #     background_tasks.add_task(run_analysis, task)
    
# # # # # #     return {"task_id": task_id, "status": "started"}

# # # # # # @app.get("/stream/{task_id}")
# # # # # # async def stream_analysis(task_id: str):
# # # # # #     if task_id not in active_tasks:
# # # # # #         return {"error": "Task not found"}
    
# # # # # #     task = active_tasks[task_id]
    
# # # # # #     async def event_generator():
# # # # # #         while not task.completed:
# # # # # #             try:
# # # # # #                 # Wait for update with timeout
# # # # # #                 update = await asyncio.wait_for(task.queue.get(), timeout=1.0)
# # # # # #                 yield f"data: {update}\n\n"
# # # # # #             except asyncio.TimeoutError:
# # # # # #                 yield f"data: {'{\"status\": \"processing\"}'}\n\n"
# # # # # #                 continue
        
# # # # # #         # Clean up
# # # # # #         del active_tasks[task_id]
    
# # # # # #     return StreamingResponse(event_generator(), media_type="text/event-stream")

# # # # # # async def run_analysis(task: AnalysisTask):
# # # # # #     import json
    
# # # # # #     try:
# # # # # #         # Initialize crawler and analyzer
# # # # # #         crawler = WebCrawler(task.url)
# # # # # #         nlp_analyzer = NLPAnalyzer()
        
# # # # # #         # Step 1: Start crawling
# # # # # #         await task.queue.put(json.dumps({
# # # # # #             "step": "crawling",
# # # # # #             "status": "started",
# # # # # #             "message": "Starting web crawl..."
# # # # # #         }))
        
# # # # # #         # Crawl website
# # # # # #         pages = await crawler.crawl(max_pages=10)
        
# # # # # #         await task.queue.put(json.dumps({
# # # # # #             "step": "crawling",
# # # # # #             "status": "completed",
# # # # # #             "pages_found": len(pages)
# # # # # #         }))
        
# # # # # #         # Step 2: Analyze each page
# # # # # #         all_results = []
# # # # # #         for i, page in enumerate(pages):
# # # # # #             await task.queue.put(json.dumps({
# # # # # #                 "step": "analyzing",
# # # # # #                 "status": "progress",
# # # # # #                 "current": i + 1,
# # # # # #                 "total": len(pages),
# # # # # #                 "page": page['url']
# # # # # #             }))
            
# # # # # #             # Run NLP analysis
# # # # # #             analysis = nlp_analyzer.analyze_page(page)
# # # # # #             all_results.append(analysis)
            
# # # # # #             await asyncio.sleep(0.5)  # Simulate processing time
        
# # # # # #         # Step 3: Generate final report
# # # # # #         await task.queue.put(json.dumps({
# # # # # #             "step": "generating",
# # # # # #             "status": "started",
# # # # # #             "message": "Generating SEO report..."
# # # # # #         }))
        
# # # # # #         final_report = nlp_analyzer.generate_report(all_results)
        
# # # # # #         # Send final results
# # # # # #         await task.queue.put(json.dumps({
# # # # # #             "step": "completed",
# # # # # #             "status": "success",
# # # # # #             "data": final_report
# # # # # #         }))
        
# # # # # #     except Exception as e:
# # # # # #         await task.queue.put(json.dumps({
# # # # # #             "step": "error",
# # # # # #             "status": "failed",
# # # # # #             "message": str(e)
# # # # # #         }))
    
# # # # # #     finally:
# # # # # #         task.completed = True

# # # # # # @app.get("/health")
# # # # # # async def health_check():
# # # # # #     return {"status": "ok"}

# # # # # # if __name__ == "__main__":
# # # # # #     import uvicorn
# # # # # #     uvicorn.run(app, host="0.0.0.0", port=8000)



# # # # # from fastapi import FastAPI, BackgroundTasks
# # # # # from fastapi.middleware.cors import CORSMiddleware
# # # # # from fastapi.responses import StreamingResponse
# # # # # from pydantic import BaseModel
# # # # # import asyncio
# # # # # import uuid
# # # # # import json
# # # # # import aiohttp
# # # # # from bs4 import BeautifulSoup
# # # # # from urllib.parse import urljoin, urlparse
# # # # # from collections import Counter
# # # # # import re

# # # # # app = FastAPI()

# # # # # app.add_middleware(
# # # # #     CORSMiddleware,
# # # # #     allow_origins=["*"],
# # # # #     allow_credentials=True,
# # # # #     allow_methods=["*"],
# # # # #     allow_headers=["*"],
# # # # # )

# # # # # # Store active analysis tasks
# # # # # active_tasks = {}

# # # # # class AnalyzeRequest(BaseModel):
# # # # #     url: str

# # # # # class AnalysisTask:
# # # # #     def __init__(self, task_id: str, url: str):
# # # # #         self.task_id = task_id
# # # # #         self.url = url
# # # # #         self.queue = asyncio.Queue()
# # # # #         self.completed = False

# # # # # @app.post("/analyze")
# # # # # async def analyze_website(request: AnalyzeRequest, background_tasks: BackgroundTasks):
# # # # #     task_id = str(uuid.uuid4())
# # # # #     task = AnalysisTask(task_id, request.url)
# # # # #     active_tasks[task_id] = task
    
# # # # #     background_tasks.add_task(run_analysis, task)
    
# # # # #     return {"task_id": task_id, "status": "started"}

# # # # # @app.get("/stream/{task_id}")
# # # # # async def stream_analysis(task_id: str):
# # # # #     if task_id not in active_tasks:
# # # # #         return {"error": "Task not found"}
    
# # # # #     task = active_tasks[task_id]
    
# # # # #     async def event_generator():
# # # # #         while not task.completed:
# # # # #             try:
# # # # #                 update = await asyncio.wait_for(task.queue.get(), timeout=1.0)
# # # # #                 yield f"data: {update}\n\n"
# # # # #             except asyncio.TimeoutError:
# # # # #                 yield f"data: {json.dumps({'status': 'processing'})}\n\n"
# # # # #                 continue
        
# # # # #         del active_tasks[task_id]
    
# # # # #     return StreamingResponse(event_generator(), media_type="text/event-stream")

# # # # # async def fetch_page(session, url):
# # # # #     try:
# # # # #         async with session.get(url, timeout=10) as response:
# # # # #             if response.status == 200:
# # # # #                 return await response.text()
# # # # #     except:
# # # # #         pass
# # # # #     return None

# # # # # def extract_keywords(text, top_n=20):
# # # # #     stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 
# # # # #                      'at', 'to', 'for', 'of', 'with', 'by', 'from', 'is'])
# # # # #     words = re.findall(r'\b[a-z]{3,}\b', text.lower())
# # # # #     filtered = [w for w in words if w not in stop_words]
# # # # #     return Counter(filtered).most_common(top_n)

# # # # # def analyze_page_content(html, url):
# # # # #     soup = BeautifulSoup(html, 'html.parser')
    
# # # # #     # Extract metadata
# # # # #     title = soup.find('title')
# # # # #     title_text = title.get_text().strip() if title else ""
    
# # # # #     meta_desc = soup.find('meta', attrs={'name': 'description'})
# # # # #     description = meta_desc.get('content', '') if meta_desc else ""
    
# # # # #     # Extract text
# # # # #     for script in soup(["script", "style"]):
# # # # #         script.decompose()
# # # # #     text = soup.get_text()
# # # # #     text = ' '.join(text.split())
    
# # # # #     # Extract headings
# # # # #     h1_tags = [h.get_text().strip() for h in soup.find_all('h1')]
# # # # #     h2_tags = [h.get_text().strip() for h in soup.find_all('h2')]
    
# # # # #     # Extract images
# # # # #     images = soup.find_all('img')
# # # # #     images_without_alt = sum(1 for img in images if not img.get('alt'))
    
# # # # #     # Calculate SEO score
# # # # #     score = 100
# # # # #     issues = []
    
# # # # #     if not title_text:
# # # # #         score -= 10
# # # # #         issues.append('Missing title tag')
# # # # #     if not description:
# # # # #         score -= 10
# # # # #         issues.append('Missing meta description')
# # # # #     if len(h1_tags) == 0:
# # # # #         score -= 10
# # # # #         issues.append('Missing H1 tag')
# # # # #     elif len(h1_tags) > 1:
# # # # #         score -= 5
# # # # #         issues.append('Multiple H1 tags')
    
# # # # #     word_count = len(text.split())
# # # # #     if word_count < 300:
# # # # #         score -= 10
# # # # #         issues.append('Content too short')
    
# # # # #     # Extract keywords
# # # # #     keywords = extract_keywords(text, 15)
    
# # # # #     return {
# # # # #         'url': url,
# # # # #         'title': title_text,
# # # # #         'description': description,
# # # # #         'word_count': word_count,
# # # # #         'keywords': [{'word': k[0], 'count': k[1]} for k in keywords],
# # # # #         'h1_count': len(h1_tags),
# # # # #         'h2_count': len(h2_tags),
# # # # #         'images_count': len(images),
# # # # #         'images_without_alt': images_without_alt,
# # # # #         'seo_score': {'score': max(0, score), 'issues': issues}
# # # # #     }

# # # # # async def run_analysis(task: AnalysisTask):
# # # # #     try:
# # # # #         domain = urlparse(task.url).netloc
        
# # # # #         # Step 1: Start crawling
# # # # #         await task.queue.put(json.dumps({
# # # # #             "step": "crawling",
# # # # #             "status": "started",
# # # # #             "message": "Starting web crawl..."
# # # # #         }))
        
# # # # #         # Crawl pages
# # # # #         pages_data = []
# # # # #         visited = set()
# # # # #         to_visit = [task.url]
        
# # # # #         async with aiohttp.ClientSession() as session:
# # # # #             while to_visit and len(visited) < 5:  # Max 5 pages
# # # # #                 url = to_visit.pop(0)
# # # # #                 if url in visited:
# # # # #                     continue
                
# # # # #                 visited.add(url)
# # # # #                 html = await fetch_page(session, url)
                
# # # # #                 if html:
# # # # #                     soup = BeautifulSoup(html, 'html.parser')
                    
# # # # #                     # Find more links
# # # # #                     for link in soup.find_all('a', href=True):
# # # # #                         href = urljoin(url, link['href'])
# # # # #                         if urlparse(href).netloc == domain and href not in visited:
# # # # #                             to_visit.append(href)
                    
# # # # #                     # Analyze page
# # # # #                     page_data = analyze_page_content(html, url)
# # # # #                     pages_data.append(page_data)
                    
# # # # #                     await task.queue.put(json.dumps({
# # # # #                         "step": "analyzing",
# # # # #                         "status": "progress",
# # # # #                         "current": len(visited),
# # # # #                         "total": min(5, len(to_visit) + len(visited)),
# # # # #                         "page": url
# # # # #                     }))
                    
# # # # #                     await asyncio.sleep(0.5)
        
# # # # #         await task.queue.put(json.dumps({
# # # # #             "step": "crawling",
# # # # #             "status": "completed",
# # # # #             "pages_found": len(pages_data)
# # # # #         }))
        
# # # # #         # Generate report
# # # # #         await task.queue.put(json.dumps({
# # # # #             "step": "generating",
# # # # #             "status": "started",
# # # # #             "message": "Generating SEO report..."
# # # # #         }))
        
# # # # #         # Aggregate data
# # # # #         total_pages = len(pages_data)
# # # # #         avg_score = sum(p['seo_score']['score'] for p in pages_data) / total_pages if total_pages > 0 else 0
        
# # # # #         all_keywords = {}
# # # # #         for page in pages_data:
# # # # #             for kw in page['keywords']:
# # # # #                 word = kw['word']
# # # # #                 all_keywords[word] = all_keywords.get(word, 0) + kw['count']
        
# # # # #         top_keywords = sorted(all_keywords.items(), key=lambda x: x[1], reverse=True)[:20]
        
# # # # #         all_issues = []
# # # # #         for page in pages_data:
# # # # #             all_issues.extend(page['seo_score']['issues'])
        
# # # # #         issue_counts = Counter(all_issues)
        
# # # # #         final_report = {
# # # # #             'summary': {
# # # # #                 'total_pages': total_pages,
# # # # #                 'average_seo_score': round(avg_score, 1),
# # # # #                 'total_words': sum(p['word_count'] for p in pages_data),
# # # # #                 'total_images': sum(p['images_count'] for p in pages_data)
# # # # #             },
# # # # #             'top_keywords': [{'word': k[0], 'count': k[1]} for k in top_keywords],
# # # # #             'common_issues': [{'issue': k, 'count': v} for k, v in issue_counts.most_common()],
# # # # #             'pages': pages_data,
# # # # #             'technical_score': {
# # # # #                 'on_page_seo': round(avg_score, 1),
# # # # #                 'content_quality': 75,
# # # # #                 'mobile_friendly': 85,
# # # # #                 'performance': 78
# # # # #             }
# # # # #         }
        
# # # # #         # Send final results
# # # # #         await task.queue.put(json.dumps({
# # # # #             "step": "completed",
# # # # #             "status": "success",
# # # # #             "data": final_report
# # # # #         }))
        
# # # # #     except Exception as e:
# # # # #         print(f"Error: {e}")
# # # # #         await task.queue.put(json.dumps({
# # # # #             "step": "error",
# # # # #             "status": "failed",
# # # # #             "message": str(e)
# # # # #         }))
    
# # # # #     finally:
# # # # #         task.completed = True

# # # # # @app.get("/health")
# # # # # async def health_check():
# # # # #     return {"status": "ok", "message": "FastAPI server running"}

# # # # # if __name__ == "__main__":
# # # # #     import uvicorn
# # # # #     uvicorn.run(app, host="0.0.0.0", port=8000)




# # # # from fastapi import FastAPI, BackgroundTasks
# # # # from fastapi.middleware.cors import CORSMiddleware
# # # # from fastapi.responses import StreamingResponse
# # # # from pydantic import BaseModel
# # # # import asyncio
# # # # import uuid
# # # # import json
# # # # from crawler import WebCrawler
# # # # from nlp_analyze import NLPAnalyzer

# # # # app = FastAPI(title="SEO Analyzer API", version="2.0")

# # # # app.add_middleware(
# # # #     CORSMiddleware,
# # # #     allow_origins=["*"],
# # # #     allow_credentials=True,
# # # #     allow_methods=["*"],
# # # #     allow_headers=["*"],
# # # # )

# # # # # Store active analysis tasks
# # # # active_tasks = {}

# # # # class AnalyzeRequest(BaseModel):
# # # #     url: str

# # # # class AnalysisTask:
# # # #     def __init__(self, task_id: str, url: str):
# # # #         self.task_id = task_id
# # # #         self.url = url
# # # #         self.queue = asyncio.Queue()
# # # #         self.completed = False

# # # # @app.post("/analyze")
# # # # async def analyze_website(request: AnalyzeRequest, background_tasks: BackgroundTasks):
# # # #     """Start website analysis"""
# # # #     task_id = str(uuid.uuid4())
# # # #     task = AnalysisTask(task_id, request.url)
# # # #     active_tasks[task_id] = task
    
# # # #     background_tasks.add_task(run_analysis, task)
    
# # # #     return {"task_id": task_id, "status": "started"}

# # # # @app.get("/stream/{task_id}")
# # # # async def stream_analysis(task_id: str):
# # # #     """Stream real-time analysis updates"""
# # # #     if task_id not in active_tasks:
# # # #         return {"error": "Task not found"}
    
# # # #     task = active_tasks[task_id]
    
# # # #     async def event_generator():
# # # #         while not task.completed:
# # # #             try:
# # # #                 update = await asyncio.wait_for(task.queue.get(), timeout=1.0)
# # # #                 yield f"data: {update}\n\n"
# # # #             except asyncio.TimeoutError:
# # # #                 yield f"data: {json.dumps({'status': 'processing'})}\n\n"
# # # #                 continue
        
# # # #         # Clean up
# # # #         if task_id in active_tasks:
# # # #             del active_tasks[task_id]
    
# # # #     return StreamingResponse(event_generator(), media_type="text/event-stream")

# # # # async def run_analysis(task: AnalysisTask):
# # # #     """Main analysis function"""
# # # #     try:
# # # #         # Initialize crawler and analyzer
# # # #         crawler = WebCrawler(task.url)
# # # #         nlp_analyzer = NLPAnalyzer()
        
# # # #         # Step 1: Start crawling
# # # #         await task.queue.put(json.dumps({
# # # #             "step": "crawling",
# # # #             "status": "started",
# # # #             "message": "Starting web crawl..."
# # # #         }))
        
# # # #         # Crawl website
# # # #         pages = await crawler.crawl(max_pages=10)
        
# # # #         await task.queue.put(json.dumps({
# # # #             "step": "crawling",
# # # #             "status": "completed",
# # # #             "pages_found": len(pages)
# # # #         }))
        
# # # #         # Step 2: Analyze each page
# # # #         all_results = []
# # # #         for i, page in enumerate(pages):
# # # #             await task.queue.put(json.dumps({
# # # #                 "step": "analyzing",
# # # #                 "status": "progress",
# # # #                 "current": i + 1,
# # # #                 "total": len(pages),
# # # #                 "page": page['url']
# # # #             }))
            
# # # #             # Run NLP analysis
# # # #             analysis = nlp_analyzer.analyze_page(page)
# # # #             all_results.append(analysis)
            
# # # #             await asyncio.sleep(0.3)
        
# # # #         # Step 3: Generate final report
# # # #         await task.queue.put(json.dumps({
# # # #             "step": "generating",
# # # #             "status": "started",
# # # #             "message": "Generating SEO report..."
# # # #         }))
        
# # # #         final_report = nlp_analyzer.generate_report(all_results)
        
# # # #         # Send final results
# # # #         await task.queue.put(json.dumps({
# # # #             "step": "completed",
# # # #             "status": "success",
# # # #             "data": final_report
# # # #         }))
        
# # # #     except Exception as e:
# # # #         print(f"Analysis error: {e}")
# # # #         await task.queue.put(json.dumps({
# # # #             "step": "error",
# # # #             "status": "failed",
# # # #             "message": str(e)
# # # #         }))
    
# # # #     finally:
# # # #         task.completed = True

# # # # @app.get("/health")
# # # # async def health_check():
# # # #     return {
# # # #         "status": "ok", 
# # # #         "message": "SEO Analyzer API is running",
# # # #         "version": "2.0",
# # # #         "active_tasks": len(active_tasks)
# # # #     }

# # # # @app.get("/")
# # # # async def root():
# # # #     return {
# # # #         "service": "SEO Analyzer API",
# # # #         "version": "2.0",
# # # #         "endpoints": {
# # # #             "analyze": "/analyze (POST)",
# # # #             "stream": "/stream/{task_id} (GET)",
# # # #             "health": "/health (GET)"
# # # #         }
# # # #     }

# # # # if __name__ == "__main__":
# # # #     import uvicorn
# # # #     print("\n🚀 ================================")
# # # #     print("✅ Starting SEO Analyzer API...")
# # # #     print("✅ Server: http://localhost:8000")
# # # #     print("✅ Docs: http://localhost:8000/docs")
# # # #     print("🚀 ================================\n")
# # # #     uvicorn.run(app, host="0.0.0.0", port=8000)


# # # from fastapi import FastAPI, BackgroundTasks
# # # from fastapi.middleware.cors import CORSMiddleware
# # # from fastapi.responses import StreamingResponse
# # # from pydantic import BaseModel
# # # import asyncio
# # # import uuid
# # # import json
# # # import sys
# # # import os

# # # # Add current directory to path
# # # sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# # # # Import your modules - adjust the name based on your actual file
# # # try:
# # #     from crawler import WebCrawler
# # #     from nlp_analyzer import NLPAnalyzer  # If your file is nlp_analyzer.py
# # #     # OR
# # #     # from nlp_analyze import NLPAnalyzer  # If your file is nlp_analyze.py
# # # except ImportError as e:
# # #     print(f"❌ Import Error: {e}")
# # #     print(f"Current directory: {os.getcwd()}")
# # #     print(f"Files in directory: {os.listdir('.')}")
# # #     sys.exit(1)

# # # app = FastAPI(title="SEO Analyzer API", version="2.0")

# # # app.add_middleware(
# # #     CORSMiddleware,
# # #     allow_origins=["*"],
# # #     allow_credentials=True,
# # #     allow_methods=["*"],
# # #     allow_headers=["*"],
# # # )

# # # # Store active analysis tasks
# # # active_tasks = {}

# # # class AnalyzeRequest(BaseModel):
# # #     url: str

# # # class AnalysisTask:
# # #     def __init__(self, task_id: str, url: str):
# # #         self.task_id = task_id
# # #         self.url = url
# # #         self.queue = asyncio.Queue()
# # #         self.completed = False

# # # @app.post("/analyze")
# # # async def analyze_website(request: AnalyzeRequest, background_tasks: BackgroundTasks):
# # #     """Start website analysis"""
# # #     task_id = str(uuid.uuid4())
# # #     task = AnalysisTask(task_id, request.url)
# # #     active_tasks[task_id] = task
    
# # #     background_tasks.add_task(run_analysis, task)
    
# # #     return {"task_id": task_id, "status": "started"}

# # # @app.get("/stream/{task_id}")
# # # async def stream_analysis(task_id: str):
# # #     """Stream real-time analysis updates"""
# # #     if task_id not in active_tasks:
# # #         return {"error": "Task not found"}
    
# # #     task = active_tasks[task_id]
    
# # #     async def event_generator():
# # #         while not task.completed:
# # #             try:
# # #                 update = await asyncio.wait_for(task.queue.get(), timeout=1.0)
# # #                 yield f"data: {update}\n\n"
# # #             except asyncio.TimeoutError:
# # #                 yield f"data: {json.dumps({'status': 'processing'})}\n\n"
# # #                 continue
        
# # #         # Clean up
# # #         if task_id in active_tasks:
# # #             del active_tasks[task_id]
    
# # #     return StreamingResponse(event_generator(), media_type="text/event-stream")

# # # async def run_analysis(task: AnalysisTask):
# # #     """Main analysis function"""
# # #     try:
# # #         # Initialize crawler and analyzer
# # #         crawler = WebCrawler(task.url)
# # #         nlp_analyzer = NLPAnalyzer()
        
# # #         # Step 1: Start crawling
# # #         await task.queue.put(json.dumps({
# # #             "step": "crawling",
# # #             "status": "started",
# # #             "message": "Starting web crawl..."
# # #         }))
        
# # #         # Crawl website
# # #         pages = await crawler.crawl(max_pages=10)
        
# # #         await task.queue.put(json.dumps({
# # #             "step": "crawling",
# # #             "status": "completed",
# # #             "pages_found": len(pages)
# # #         }))
        
# # #         # Step 2: Analyze each page
# # #         all_results = []
# # #         for i, page in enumerate(pages):
# # #             await task.queue.put(json.dumps({
# # #                 "step": "analyzing",
# # #                 "status": "progress",
# # #                 "current": i + 1,
# # #                 "total": len(pages),
# # #                 "page": page['url']
# # #             }))
            
# # #             # Run NLP analysis
# # #             analysis = nlp_analyzer.analyze_page(page)
# # #             all_results.append(analysis)
            
# # #             await asyncio.sleep(0.3)
        
# # #         # Step 3: Generate final report
# # #         await task.queue.put(json.dumps({
# # #             "step": "generating",
# # #             "status": "started",
# # #             "message": "Generating SEO report..."
# # #         }))
        
# # #         final_report = nlp_analyzer.generate_report(all_results)
        
# # #         # Send final results
# # #         await task.queue.put(json.dumps({
# # #             "step": "completed",
# # #             "status": "success",
# # #             "data": final_report
# # #         }))
        
# # #     except Exception as e:
# # #         import traceback
# # #         error_msg = str(e)
# # #         traceback_msg = traceback.format_exc()
# # #         print(f"❌ Analysis error: {error_msg}")
# # #         print(f"Traceback: {traceback_msg}")
        
# # #         await task.queue.put(json.dumps({
# # #             "step": "error",
# # #             "status": "failed",
# # #             "message": error_msg
# # #         }))
    
# # #     finally:
# # #         task.completed = True

# # # @app.get("/health")
# # # async def health_check():
# # #     return {
# # #         "status": "ok", 
# # #         "message": "SEO Analyzer API is running",
# # #         "version": "2.0",
# # #         "active_tasks": len(active_tasks)
# # #     }

# # # @app.get("/")
# # # async def root():
# # #     return {
# # #         "service": "SEO Analyzer API",
# # #         "version": "2.0",
# # #         "endpoints": {
# # #             "analyze": "/analyze (POST)",
# # #             "stream": "/stream/{task_id} (GET)",
# # #             "health": "/health (GET)"
# # #         }
# # #     }

# # # if __name__ == "__main__":
# # #     import uvicorn
# # #     print("\n🚀 ================================")
# # #     print("✅ Starting SEO Analyzer API...")
# # #     print("✅ Server: http://localhost:8000")
# # #     print("✅ Docs: http://localhost:8000/docs")
# # #     print("🚀 ================================\n")
# # #     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)





# # async def run_analysis(task: AnalysisTask):
# #     """Main analysis function"""
# #     try:
# #         print(f"\n{'='*60}")
# #         print(f"🚀 STARTING ANALYSIS FOR: {task.url}")
# #         print(f"{'='*60}\n")
        
# #         # Initialize crawler and analyzer
# #         crawler = WebCrawler(task.url)
# #         nlp_analyzer = NLPAnalyzer()
        
# #         # Step 1: Start crawling
# #         await task.queue.put(json.dumps({
# #             "step": "crawling",
# #             "status": "started",
# #             "message": "Starting web crawl..."
# #         }))
        
# #         # Crawl website
# #         print(f"📡 Starting crawl for domain: {crawler.domain}")
# #         pages = await crawler.crawl(max_pages=10)
# #         print(f"✅ Crawled {len(pages)} pages")
        
# #         await task.queue.put(json.dumps({
# #             "step": "crawling",
# #             "status": "completed",
# #             "pages_found": len(pages)
# #         }))
        
# #         # Step 2: Analyze each page
# #         all_results = []
# #         for i, page in enumerate(pages):
# #             print(f"🔍 Analyzing page {i+1}/{len(pages)}: {page['url']}")
            
# #             await task.queue.put(json.dumps({
# #                 "step": "analyzing",
# #                 "status": "progress",
# #                 "current": i + 1,
# #                 "total": len(pages),
# #                 "page": page['url']
# #             }))
            
# #             # Run NLP analysis
# #             analysis = nlp_analyzer.analyze_page(page)
# #             print(f"   Score: {analysis['seo_score']['score']}")
# #             print(f"   Keywords: {[k['word'] for k in analysis['keywords'][:3]]}")
# #             all_results.append(analysis)
            
# #             await asyncio.sleep(0.3)
        
# #         # Step 3: Generate final report
# #         print("\n📊 Generating final report...")
# #         await task.queue.put(json.dumps({
# #             "step": "generating",
# #             "status": "started",
# #             "message": "Generating SEO report..."
# #         }))
        
# #         final_report = nlp_analyzer.generate_report(all_results)
        
# #         print(f"\n{'='*60}")
# #         print(f"✅ ANALYSIS COMPLETE")
# #         print(f"   Total Pages: {final_report['summary']['total_pages']}")
# #         print(f"   Avg Score: {final_report['summary']['average_seo_score']}")
# #         print(f"   Total Words: {final_report['summary']['total_words']}")
# #         print(f"   Top Keywords: {[k['word'] for k in final_report['top_keywords'][:5]]}")
# #         print(f"{'='*60}\n")
        
# #         # Send final results
# #         await task.queue.put(json.dumps({
# #             "step": "completed",
# #             "status": "success",
# #             "data": final_report
# #         }))
        
# #     except Exception as e:
# #         import traceback
# #         error_msg = str(e)
# #         traceback_msg = traceback.format_exc()
# #         print(f"\n❌ ANALYSIS ERROR: {error_msg}")
# #         print(f"Traceback:\n{traceback_msg}")
        
# #         await task.queue.put(json.dumps({
# #             "step": "error",
# #             "status": "failed",
# #             "message": error_msg
# #         }))
    
# #     finally:
# #         task.completed = True


# from fastapi import FastAPI, BackgroundTasks
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import StreamingResponse
# from pydantic import BaseModel
# import asyncio
# import uuid
# import json
# import sys
# import os

# # Add current directory to path
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# # Import modules
# from crawler import WebCrawler
# from nlp_analyzer import NLPAnalyzer

# app = FastAPI(title="SEO Analyzer API", version="2.0")

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
#     """Start website analysis"""
#     task_id = str(uuid.uuid4())
#     task = AnalysisTask(task_id, request.url)
#     active_tasks[task_id] = task
    
#     background_tasks.add_task(run_analysis, task)
    
#     return {"task_id": task_id, "status": "started"}

# @app.get("/stream/{task_id}")
# async def stream_analysis(task_id: str):
#     """Stream real-time analysis updates"""
#     if task_id not in active_tasks:
#         return {"error": "Task not found"}
    
#     task = active_tasks[task_id]
    
#     async def event_generator():
#         while not task.completed:
#             try:
#                 update = await asyncio.wait_for(task.queue.get(), timeout=1.0)
#                 yield f"data: {update}\n\n"
#             except asyncio.TimeoutError:
#                 yield f"data: {json.dumps({'status': 'processing'})}\n\n"
#                 continue
        
#         # Clean up
#         if task_id in active_tasks:
#             del active_tasks[task_id]
    
#     return StreamingResponse(event_generator(), media_type="text/event-stream")

# async def run_analysis(task: AnalysisTask):
#     """Main analysis function"""
#     try:
#         print(f"\n{'='*60}")
#         print(f"🚀 STARTING ANALYSIS FOR: {task.url}")
#         print(f"{'='*60}\n")
        
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
#         print(f"📡 Starting crawl for domain: {crawler.domain}")
#         pages = await crawler.crawl(max_pages=10)
#         print(f"✅ Crawled {len(pages)} pages")
        
#         for page in pages:
#             print(f"   - {page['url']} ({page['word_count']} words)")
        
#         await task.queue.put(json.dumps({
#             "step": "crawling",
#             "status": "completed",
#             "pages_found": len(pages)
#         }))
        
#         # Step 2: Analyze each page
#         all_results = []
#         for i, page in enumerate(pages):
#             print(f"\n🔍 Analyzing page {i+1}/{len(pages)}: {page['url']}")
            
#             await task.queue.put(json.dumps({
#                 "step": "analyzing",
#                 "status": "progress",
#                 "current": i + 1,
#                 "total": len(pages),
#                 "page": page['url']
#             }))
            
#             # Run NLP analysis
#             analysis = nlp_analyzer.analyze_page(page)
#             print(f"   ✅ Score: {analysis['seo_score']['score']}")
#             print(f"   📊 Breakdown: Content={analysis['seo_score']['breakdown']['content']}, "
#                   f"Technical={analysis['seo_score']['breakdown']['technical']}, "
#                   f"OnPage={analysis['seo_score']['breakdown']['onpage']}")
#             print(f"   🔑 Top Keywords: {[k['word'] for k in analysis['keywords'][:5]]}")
#             print(f"   ⚠️  Issues: {len(analysis['seo_score']['issues'])}")
            
#             all_results.append(analysis)
            
#             await asyncio.sleep(0.3)
        
#         # Step 3: Generate final report
#         print("\n📊 Generating final report...")
#         await task.queue.put(json.dumps({
#             "step": "generating",
#             "status": "started",
#             "message": "Generating SEO report..."
#         }))
        
#         final_report = nlp_analyzer.generate_report(all_results)
        
#         print(f"\n{'='*60}")
#         print(f"✅ ANALYSIS COMPLETE FOR: {task.url}")
#         print(f"   📄 Total Pages: {final_report['summary']['total_pages']}")
#         print(f"   📊 Avg SEO Score: {final_report['summary']['average_seo_score']}")
#         print(f"   📝 Total Words: {final_report['summary']['total_words']}")
#         print(f"   🖼️  Total Images: {final_report['summary']['total_images']}")
#         print(f"   📖 Avg Readability: {final_report['summary'].get('avg_readability', 'N/A')}")
#         print(f"   🔑 Top 5 Keywords: {[k['word'] for k in final_report['top_keywords'][:5]]}")
#         print(f"   ⚠️  Common Issues: {len(final_report['common_issues'])}")
#         if final_report['common_issues']:
#             for issue in final_report['common_issues'][:3]:
#                 print(f"      - {issue['issue']} ({issue['count']} pages)")
#         print(f"{'='*60}\n")
        
#         # Send final results
#         await task.queue.put(json.dumps({
#             "step": "completed",
#             "status": "success",
#             "data": final_report
#         }))
        
#     except Exception as e:
#         import traceback
#         error_msg = str(e)
#         traceback_msg = traceback.format_exc()
#         print(f"\n❌ ANALYSIS ERROR: {error_msg}")
#         print(f"Traceback:\n{traceback_msg}")
        
#         await task.queue.put(json.dumps({
#             "step": "error",
#             "status": "failed",
#             "message": error_msg
#         }))
    
#     finally:
#         task.completed = True

# @app.get("/health")
# async def health_check():
#     return {
#         "status": "ok", 
#         "message": "SEO Analyzer API is running",
#         "version": "2.0",
#         "active_tasks": len(active_tasks)
#     }

# @app.get("/")
# async def root():
#     return {
#         "service": "SEO Analyzer API",
#         "version": "2.0",
#         "endpoints": {
#             "analyze": "POST /analyze",
#             "stream": "GET /stream/{task_id}",
#             "health": "GET /health"
#         }
#     }

# if __name__ == "__main__":
#     import uvicorn
#     print("\n🚀 ================================")
#     print("✅ Starting SEO Analyzer API...")
#     print("✅ Server: http://localhost:8000")
#     print("✅ Docs: http://localhost:8000/docs")
#     print("🚀 ================================\n")
#     uvicorn.run(app, host="0.0.0.0", port=8000)



from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import asyncio
import uuid
import json
import sys
import os
import traceback

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("🔄 Importing modules...")

try:
    from crawler import WebCrawler
    print("✅ Crawler imported")
except Exception as e:
    print(f"❌ Failed to import crawler: {e}")
    traceback.print_exc()
    sys.exit(1)

try:
    from nlp_analyzer import NLPAnalyzer
    print("✅ NLP Analyzer imported")
except Exception as e:
    print(f"❌ Failed to import nlp_analyzer: {e}")
    traceback.print_exc()
    sys.exit(1)

try:
    from scorer.scoring import compute_overall_score
    print("✅ Scorer imported")
except Exception as e:
    print(f"❌ Failed to import scorer: {e}")
    traceback.print_exc()
    sys.exit(1)

print("✅ All modules imported successfully!\n")

app = FastAPI(title="SEO Analyzer API", version="2.0")

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
    """Start website analysis"""
    print(f"\n{'='*60}")
    print(f"🚀 NEW ANALYSIS REQUEST")
    print(f"   URL: {request.url}")
    print(f"{'='*60}\n")
    
    task_id = str(uuid.uuid4())
    task = AnalysisTask(task_id, request.url)
    active_tasks[task_id] = task
    
    background_tasks.add_task(run_analysis, task)
    
    return {"task_id": task_id, "status": "started"}

@app.get("/stream/{task_id}")
async def stream_analysis(task_id: str):
    """Stream real-time analysis updates"""
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
        
        # After task is completed, drain remaining events from queue (e.g., final 'completed' event)
        print(f"🔚 Stream: Task completed, draining remaining queue events...")
        while not task.queue.empty():
            try:
                update = task.queue.get_nowait()
                print(f"🔚 Stream: Yielding remaining event: {update[:50]}...")
                yield f"data: {update}\n\n"
            except asyncio.QueueEmpty:
                break
        
        print(f"🔚 Stream: All events sent, closing stream for task {task_id}")
        
        # Clean up
        if task_id in active_tasks:
            del active_tasks[task_id]
    
    return StreamingResponse(event_generator(), media_type="text/event-stream")

async def run_analysis(task: AnalysisTask):
    """Main analysis function"""
    try:
        print(f"\n{'='*60}")
        print(f"🚀 STARTING ANALYSIS FOR: {task.url}")
        print(f"{'='*60}\n")
        
        # Initialize crawler and analyzer
        crawler = WebCrawler(task.url)
        nlp_analyzer = NLPAnalyzer()
        
        # Step 1: Start crawling
        await task.queue.put(json.dumps({
            "step": "crawling",
            "status": "started",
            "message": "Starting web crawl..."
        }))
        
        # Crawl website
        print(f"📡 Starting crawl for domain: {crawler.domain}")
        pages = await crawler.crawl(max_pages=10)
        print(f"\n✅ CRAWLED {len(pages)} PAGES:")
        
        for i, page in enumerate(pages, 1):
            print(f"   {i}. {page['url']}")
            print(f"      Title: {page['title'][:60]}...")
            print(f"      Words: {page['word_count']}")
        
        await task.queue.put(json.dumps({
            "step": "crawling",
            "status": "completed",
            "pages_found": len(pages)
        }))
        
        if not pages:
            raise Exception("No pages were crawled successfully")
        
        # Step 2: Analyze each page
        print(f"\n{'='*60}")
        print(f"🔍 ANALYZING {len(pages)} PAGES")
        print(f"{'='*60}\n")
        
        all_results = []
        for i, page in enumerate(pages):
            print(f"\n📄 [{i+1}/{len(pages)}] Analyzing: {page['url']}")
            
            await task.queue.put(json.dumps({
                "step": "analyzing",
                "status": "progress",
                "current": i + 1,
                "total": len(pages),
                "page": page['url']
            }))
            
            # Run NLP analysis with YOUR scoring
            analysis = nlp_analyzer.analyze_page(page)
            
            print(f"   ✅ RESULTS:")
            print(f"      Overall Score: {analysis['seo_score']['score']}")
            print(f"      Content: {analysis['seo_score']['breakdown']['content']}")
            print(f"      Technical: {analysis['seo_score']['breakdown']['technical']}")
            print(f"      OnPage: {analysis['seo_score']['breakdown']['onpage']}")
            print(f"      Keywords: {[k['word'] for k in analysis['keywords'][:5]]}")
            print(f"      Issues: {len(analysis['seo_score']['issues'])}")
            
            all_results.append(analysis)
            await asyncio.sleep(0.3)
        
        # Step 3: Generate final report
        print(f"\n{'='*60}")
        print(f"📊 GENERATING FINAL REPORT")
        print(f"{'='*60}\n")
        
        await task.queue.put(json.dumps({
            "step": "generating",
            "status": "started",
            "message": "Generating SEO report..."
        }))
        
        final_report = nlp_analyzer.generate_report(all_results)
        
        print(f"\n{'='*60}")
        print(f"✅ ANALYSIS COMPLETE FOR: {task.url}")
        print(f"{'='*60}")
        print(f"   📄 Total Pages: {final_report['summary']['total_pages']}")
        print(f"   📊 Avg SEO Score: {final_report['summary']['average_seo_score']}")
        print(f"   📝 Total Words: {final_report['summary']['total_words']}")
        print(f"   🖼️  Total Images: {final_report['summary']['total_images']}")
        print(f"   📖 Avg Readability: {final_report['summary'].get('avg_readability', 'N/A')}")
        print(f"   🔑 Top Keywords: {[k['word'] for k in final_report['top_keywords'][:5]]}")
        print(f"   ⚠️  Issues: {len(final_report['common_issues'])}")
        print(f"{'='*60}\n")
        
        # Send final results
        print(f"📤 Queuing 'completed' event...")
        await task.queue.put(json.dumps({
            "step": "completed",
            "status": "success",
            "data": final_report
        }))
        print(f"✅ 'completed' event queued successfully")
        
    except Exception as e:
        error_msg = str(e)
        traceback_msg = traceback.format_exc()
        print(f"\n❌ ANALYSIS ERROR for {task.url}:")
        print(f"   {error_msg}")
        print(f"\nFull traceback:")
        print(traceback_msg)
        
        await task.queue.put(json.dumps({
            "step": "error",
            "status": "failed",
            "message": error_msg
        }))
    
    finally:
        print(f"🔚 Setting task.completed = True")
        task.completed = True
        print(f"🔚 Task marked as completed")

@app.get("/health")
async def health_check():
    return {
        "status": "ok", 
        "message": "SEO Analyzer API is running",
        "version": "2.0",
        "active_tasks": len(active_tasks)
    }

@app.get("/")
async def root():
    return {
        "service": "SEO Analyzer API",
        "version": "2.0",
        "endpoints": {
            "analyze": "POST /analyze",
            "stream": "GET /stream/{task_id}",
            "health": "GET /health"
        }
    }

@app.on_event("startup")
async def startup_event():
    print("\n" + "="*60)
    print("🚀 SEO ANALYZER API STARTED")
    print("="*60)
    print("✅ Server: http://localhost:8000")
    print("✅ Docs: http://localhost:8000/docs")
    print("✅ Ready to analyze websites!")
    print("="*60 + "\n")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)