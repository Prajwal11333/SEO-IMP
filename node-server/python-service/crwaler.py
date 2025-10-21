# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin, urlparse
# import re

# class WebCrawler:
#     def __init__(self, base_url):
#         self.base_url = base_url
#         self.domain = urlparse(base_url).netloc
#         self.visited = set()
#         self.pages = []
    
#     async def fetch_page(self, session, url):
#         try:
#             async with session.get(url, timeout=10) as response:
#                 if response.status == 200:
#                     html = await response.text()
#                     return html
#                 return None
#         except Exception as e:
#             print(f"Error fetching {url}: {e}")
#             return None
    
#     def extract_data(self, html, url):
#         soup = BeautifulSoup(html, 'html.parser')
        
#         # Extract metadata
#         title = soup.find('title')
#         title_text = title.get_text().strip() if title else ""
        
#         meta_desc = soup.find('meta', attrs={'name': 'description'})
#         description = meta_desc.get('content', '') if meta_desc else ""
        
#         # Extract all text content
#         for script in soup(["script", "style"]):
#             script.decompose()
        
#         text = soup.get_text()
#         lines = (line.strip() for line in text.splitlines())
#         chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
#         text = ' '.join(chunk for chunk in chunks if chunk)
        
#         # Extract headings
#         headings = {
#             'h1': [h.get_text().strip() for h in soup.find_all('h1')],
#             'h2': [h.get_text().strip() for h in soup.find_all('h2')],
#             'h3': [h.get_text().strip() for h in soup.find_all('h3')]
#         }
        
#         # Extract links
#         links = []
#         for link in soup.find_all('a', href=True):
#             href = link['href']
#             absolute_url = urljoin(url, href)
#             if urlparse(absolute_url).netloc == self.domain:
#                 links.append(absolute_url)
        
#         # Extract images
#         images = []
#         for img in soup.find_all('img'):
#             images.append({
#                 'src': img.get('src', ''),
#                 'alt': img.get('alt', '')
#             })
        
#         return {
#             'url': url,
#             'title': title_text,
#             'description': description,
#             'text': text,
#             'headings': headings,
#             'links': links,
#             'images': images,
#             'word_count': len(text.split())
#         }
    
#     async def crawl(self, max_pages=10):
#         to_visit = [self.base_url]
        
#         async with aiohttp.ClientSession() as session:
#             while to_visit and len(self.visited) < max_pages:
#                 url = to_visit.pop(0)
                
#                 if url in self.visited:
#                     continue
                
#                 self.visited.add(url)
                
#                 html = await self.fetch_page(session, url)
#                 if html:
#                     page_data = self.extract_data(html, url)
#                     self.pages.append(page_data)
                    
#                     # Add new links to visit
#                     for link in page_data['links']:
#                         if link not in self.visited and link not in to_visit:
#                             to_visit.append(link)
                
#                 await asyncio.sleep(0.5)  # Be polite
        
#         return self.pages



import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.visited = set()
        self.pages = []
    
    async def fetch_page(self, session, url):
        try:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    html = await response.text()
                    return html
                return None
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_data(self, html, url):
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract metadata
        title = soup.find('title')
        title_text = title.get_text().strip() if title else ""
        
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc.get('content', '') if meta_desc else ""
        
        # Extract all text content
        for script in soup(["script", "style"]):
            script.decompose()
        
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        # Extract headings
        headings = {
            'h1': [h.get_text().strip() for h in soup.find_all('h1')],
            'h2': [h.get_text().strip() for h in soup.find_all('h2')],
            'h3': [h.get_text().strip() for h in soup.find_all('h3')]
        }
        
        # Extract links
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            absolute_url = urljoin(url, href)
            if urlparse(absolute_url).netloc == self.domain:
                links.append(absolute_url)
        
        # Extract images
        images = []
        for img in soup.find_all('img'):
            images.append({
                'src': img.get('src', ''),
                'alt': img.get('alt', '')
            })
        
        return {
            'url': url,
            'title': title_text,
            'description': description,
            'text': text,
            'headings': headings,
            'links': links,
            'images': images,
            'word_count': len(text.split())
        }
    
    async def crawl(self, max_pages=10):
        to_visit = [self.base_url]
        
        async with aiohttp.ClientSession() as session:
            while to_visit and len(self.visited) < max_pages:
                url = to_visit.pop(0)
                
                if url in visited:
                    continue
                
                self.visited.add(url)
                
                html = await self.fetch_page(session, url)
                if html:
                    page_data = self.extract_data(html, url)
                    self.pages.append(page_data)
                    
                    # Add new links to visit
                    for link in page_data['links']:
                        if link not in self.visited and link not in to_visit:
                            to_visit.append(link)
                
                await asyncio.sleep(0.5)  # Be polite
        
        return self.pages