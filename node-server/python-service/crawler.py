# # # # # # import asyncio
# # # # # # import aiohttp
# # # # # # from bs4 import BeautifulSoup
# # # # # # from urllib.parse import urljoin, urlparse
# # # # # # import re

# # # # # # class WebCrawler:
# # # # # #     def __init__(self, base_url):
# # # # # #         self.base_url = base_url
# # # # # #         self.domain = urlparse(base_url).netloc
# # # # # #         self.visited = set()
# # # # # #         self.pages = []
    
# # # # # #     async def fetch_page(self, session, url):
# # # # # #         try:
# # # # # #             async with session.get(url, timeout=10) as response:
# # # # # #                 if response.status == 200:
# # # # # #                     html = await response.text()
# # # # # #                     return html
# # # # # #                 return None
# # # # # #         except Exception as e:
# # # # # #             print(f"Error fetching {url}: {e}")
# # # # # #             return None
    
# # # # # #     def extract_data(self, html, url):
# # # # # #         soup = BeautifulSoup(html, 'html.parser')
        
# # # # # #         # Extract metadata
# # # # # #         title = soup.find('title')
# # # # # #         title_text = title.get_text().strip() if title else ""
        
# # # # # #         meta_desc = soup.find('meta', attrs={'name': 'description'})
# # # # # #         description = meta_desc.get('content', '') if meta_desc else ""
        
# # # # # #         # Extract all text content
# # # # # #         for script in soup(["script", "style"]):
# # # # # #             script.decompose()
        
# # # # # #         text = soup.get_text()
# # # # # #         lines = (line.strip() for line in text.splitlines())
# # # # # #         chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# # # # # #         text = ' '.join(chunk for chunk in chunks if chunk)
        
# # # # # #         # Extract headings
# # # # # #         headings = {
# # # # # #             'h1': [h.get_text().strip() for h in soup.find_all('h1')],
# # # # # #             'h2': [h.get_text().strip() for h in soup.find_all('h2')],
# # # # # #             'h3': [h.get_text().strip() for h in soup.find_all('h3')]
# # # # # #         }
        
# # # # # #         # Extract links
# # # # # #         links = []
# # # # # #         for link in soup.find_all('a', href=True):
# # # # # #             href = link['href']
# # # # # #             absolute_url = urljoin(url, href)
# # # # # #             if urlparse(absolute_url).netloc == self.domain:
# # # # # #                 links.append(absolute_url)
        
# # # # # #         # Extract images
# # # # # #         images = []
# # # # # #         for img in soup.find_all('img'):
# # # # # #             images.append({
# # # # # #                 'src': img.get('src', ''),
# # # # # #                 'alt': img.get('alt', '')
# # # # # #             })
        
# # # # # #         return {
# # # # # #             'url': url,
# # # # # #             'title': title_text,
# # # # # #             'description': description,
# # # # # #             'text': text,
# # # # # #             'headings': headings,
# # # # # #             'links': links,
# # # # # #             'images': images,
# # # # # #             'word_count': len(text.split())
# # # # # #         }
    
# # # # # #     async def crawl(self, max_pages=10):
# # # # # #         to_visit = [self.base_url]
        
# # # # # #         async with aiohttp.ClientSession() as session:
# # # # # #             while to_visit and len(self.visited) < max_pages:
# # # # # #                 url = to_visit.pop(0)
                
# # # # # #                 if url in self.visited:
# # # # # #                     continue
                
# # # # # #                 self.visited.add(url)
                
# # # # # #                 html = await self.fetch_page(session, url)
# # # # # #                 if html:
# # # # # #                     page_data = self.extract_data(html, url)
# # # # # #                     self.pages.append(page_data)
                    
# # # # # #                     # Add new links to visit
# # # # # #                     for link in page_data['links']:
# # # # # #                         if link not in self.visited and link not in to_visit:
# # # # # #                             to_visit.append(link)
                
# # # # # #                 await asyncio.sleep(0.5)  # Be polite
        
# # # # # #         return self.pages



# # # # # import asyncio
# # # # # import aiohttp
# # # # # from bs4 import BeautifulSoup
# # # # # from urllib.parse import urljoin, urlparse
# # # # # import re

# # # # # class WebCrawler:
# # # # #     def __init__(self, base_url):
# # # # #         self.base_url = base_url
# # # # #         self.domain = urlparse(base_url).netloc
# # # # #         self.visited = set()
# # # # #         self.pages = []
    
# # # # #     async def fetch_page(self, session, url):
# # # # #         try:
# # # # #             async with session.get(url, timeout=10) as response:
# # # # #                 if response.status == 200:
# # # # #                     html = await response.text()
# # # # #                     return html
# # # # #                 return None
# # # # #         except Exception as e:
# # # # #             print(f"Error fetching {url}: {e}")
# # # # #             return None
    
# # # # #     def extract_data(self, html, url):
# # # # #         soup = BeautifulSoup(html, 'html.parser')
        
# # # # #         # Extract metadata
# # # # #         title = soup.find('title')
# # # # #         title_text = title.get_text().strip() if title else ""
        
# # # # #         meta_desc = soup.find('meta', attrs={'name': 'description'})
# # # # #         description = meta_desc.get('content', '') if meta_desc else ""
        
# # # # #         # Extract all text content
# # # # #         for script in soup(["script", "style"]):
# # # # #             script.decompose()
        
# # # # #         text = soup.get_text()
# # # # #         lines = (line.strip() for line in text.splitlines())
# # # # #         chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# # # # #         text = ' '.join(chunk for chunk in chunks if chunk)
        
# # # # #         # Extract headings
# # # # #         headings = {
# # # # #             'h1': [h.get_text().strip() for h in soup.find_all('h1')],
# # # # #             'h2': [h.get_text().strip() for h in soup.find_all('h2')],
# # # # #             'h3': [h.get_text().strip() for h in soup.find_all('h3')]
# # # # #         }
        
# # # # #         # Extract links
# # # # #         links = []
# # # # #         for link in soup.find_all('a', href=True):
# # # # #             href = link['href']
# # # # #             absolute_url = urljoin(url, href)
# # # # #             if urlparse(absolute_url).netloc == self.domain:
# # # # #                 links.append(absolute_url)
        
# # # # #         # Extract images
# # # # #         images = []
# # # # #         for img in soup.find_all('img'):
# # # # #             images.append({
# # # # #                 'src': img.get('src', ''),
# # # # #                 'alt': img.get('alt', '')
# # # # #             })
        
# # # # #         return {
# # # # #             'url': url,
# # # # #             'title': title_text,
# # # # #             'description': description,
# # # # #             'text': text,
# # # # #             'headings': headings,
# # # # #             'links': links,
# # # # #             'images': images,
# # # # #             'word_count': len(text.split())
# # # # #         }
    
# # # # #     async def crawl(self, max_pages=10):
# # # # #         to_visit = [self.base_url]
        
# # # # #         async with aiohttp.ClientSession() as session:
# # # # #             while to_visit and len(self.visited) < max_pages:
# # # # #                 url = to_visit.pop(0)
                
# # # # #                 if url in visited:
# # # # #                     continue
                
# # # # #                 self.visited.add(url)
                
# # # # #                 html = await self.fetch_page(session, url)
# # # # #                 if html:
# # # # #                     page_data = self.extract_data(html, url)
# # # # #                     self.pages.append(page_data)
                    
# # # # #                     # Add new links to visit
# # # # #                     for link in page_data['links']:
# # # # #                         if link not in self.visited and link not in to_visit:
# # # # #                             to_visit.append(link)
                
# # # # #                 await asyncio.sleep(0.5)  # Be polite
        
# # # # #         return self.pages




# # # # import asyncio
# # # # import aiohttp
# # # # from bs4 import BeautifulSoup
# # # # from urllib.parse import urljoin, urlparse
# # # # import re

# # # # class WebCrawler:
# # # #     def __init__(self, base_url):
# # # #         self.base_url = base_url
# # # #         self.domain = urlparse(base_url).netloc
# # # #         self.visited = set()
# # # #         self.pages = []
    
# # # #     async def fetch_page(self, session, url):
# # # #         try:
# # # #             async with session.get(url, timeout=10) as response:
# # # #                 if response.status == 200:
# # # #                     html = await response.text()
# # # #                     return html
# # # #                 return None
# # # #         except Exception as e:
# # # #             print(f"Error fetching {url}: {e}")
# # # #             return None
    
# # # #     def extract_data(self, html, url):
# # # #         soup = BeautifulSoup(html, 'html.parser')
        
# # # #         # Extract metadata
# # # #         title = soup.find('title')
# # # #         title_text = title.get_text().strip() if title else ""
        
# # # #         meta_desc = soup.find('meta', attrs={'name': 'description'})
# # # #         description = meta_desc.get('content', '') if meta_desc else ""
        
# # # #         # Extract all text content
# # # #         for script in soup(["script", "style"]):
# # # #             script.decompose()
        
# # # #         text = soup.get_text()
# # # #         lines = (line.strip() for line in text.splitlines())
# # # #         chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# # # #         text = ' '.join(chunk for chunk in chunks if chunk)
        
# # # #         # Extract headings
# # # #         headings = {
# # # #             'h1': [h.get_text().strip() for h in soup.find_all('h1')],
# # # #             'h2': [h.get_text().strip() for h in soup.find_all('h2')],
# # # #             'h3': [h.get_text().strip() for h in soup.find_all('h3')]
# # # #         }
        
# # # #         # Extract links
# # # #         links = []
# # # #         for link in soup.find_all('a', href=True):
# # # #             href = link['href']
# # # #             absolute_url = urljoin(url, href)
# # # #             if urlparse(absolute_url).netloc == self.domain:
# # # #                 links.append(absolute_url)
        
# # # #         # Extract images
# # # #         images = []
# # # #         for img in soup.find_all('img'):
# # # #             images.append({
# # # #                 'src': img.get('src', ''),
# # # #                 'alt': img.get('alt', '')
# # # #             })
        
# # # #         return {
# # # #             'url': url,
# # # #             'title': title_text,
# # # #             'description': description,
# # # #             'text': text,
# # # #             'headings': headings,
# # # #             'links': links,
# # # #             'images': images,
# # # #             'word_count': len(text.split())
# # # #         }
    
# # # #     async def crawl(self, max_pages=10):
# # # #         to_visit = [self.base_url]
        
# # # #         async with aiohttp.ClientSession() as session:
# # # #             while to_visit and len(self.visited) < max_pages:
# # # #                 url = to_visit.pop(0)
                
# # # #                 # FIX: Changed 'visited' to 'self.visited'
# # # #                 if url in self.visited:
# # # #                     continue
                
# # # #                 self.visited.add(url)
                
# # # #                 html = await self.fetch_page(session, url)
# # # #                 if html:
# # # #                     page_data = self.extract_data(html, url)
# # # #                     self.pages.append(page_data)
                    
# # # #                     # Add new links to visit
# # # #                     for link in page_data['links']:
# # # #                         if link not in self.visited and link not in to_visit:
# # # #                             to_visit.append(link)
                
# # # #                 await asyncio.sleep(0.5)  # Be polite
        
# # # #         return self.pages




# # # import asyncio
# # # import aiohttp
# # # from bs4 import BeautifulSoup
# # # from urllib.parse import urljoin, urlparse
# # # import re

# # # class WebCrawler:
# # #     def __init__(self, base_url):
# # #         self.base_url = base_url
# # #         self.domain = urlparse(base_url).netloc
# # #         self.visited = set()
# # #         self.pages = []
    
# # #     async def fetch_page(self, session, url):
# # #         """Fetch a single page"""
# # #         try:
# # #             headers = {
# # #                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
# # #             }
# # #             async with session.get(url, timeout=10, headers=headers, allow_redirects=True) as response:
# # #                 if response.status == 200:
# # #                     html = await response.text()
# # #                     return html
# # #                 return None
# # #         except Exception as e:
# # #             print(f"Error fetching {url}: {e}")
# # #             return None
    
# # #     def extract_data(self, html, url):
# # #         """Extract all relevant data from HTML"""
# # #         soup = BeautifulSoup(html, 'html.parser')
        
# # #         # Extract metadata
# # #         title = soup.find('title')
# # #         title_text = title.get_text().strip() if title else ""
        
# # #         meta_desc = soup.find('meta', attrs={'name': 'description'})
# # #         description = meta_desc.get('content', '') if meta_desc else ""
        
# # #         # Extract all text content
# # #         for script in soup(["script", "style", "noscript"]):
# # #             script.decompose()
        
# # #         text = soup.get_text()
# # #         lines = (line.strip() for line in text.splitlines())
# # #         chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# # #         text = ' '.join(chunk for chunk in chunks if chunk)
        
# # #         # Extract headings
# # #         headings = {
# # #             'h1': [h.get_text().strip() for h in soup.find_all('h1')],
# # #             'h2': [h.get_text().strip() for h in soup.find_all('h2')],
# # #             'h3': [h.get_text().strip() for h in soup.find_all('h3')]
# # #         }
        
# # #         # Extract links
# # #         links = []
# # #         for link in soup.find_all('a', href=True):
# # #             href = link['href']
# # #             absolute_url = urljoin(url, href)
# # #             parsed = urlparse(absolute_url)
            
# # #             # Only same domain links
# # #             if parsed.netloc == self.domain:
# # #                 # Remove fragments and parameters for uniqueness
# # #                 clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
# # #                 links.append(clean_url)
        
# # #         # Extract images
# # #         images = []
# # #         for img in soup.find_all('img'):
# # #             images.append({
# # #                 'src': img.get('src', ''),
# # #                 'alt': img.get('alt', '')
# # #             })
        
# # #         return {
# # #             'url': url,
# # #             'title': title_text,
# # #             'description': description,
# # #             'text': text,
# # #             'headings': headings,
# # #             'links': list(set(links)),  # Remove duplicates
# # #             'images': images,
# # #             'word_count': len(text.split())
# # #         }
    
# # #     async def crawl(self, max_pages=10):
# # #         """Crawl the website"""
# # #         to_visit = [self.base_url]
        
# # #         connector = aiohttp.TCPConnector(ssl=False)
# # #         async with aiohttp.ClientSession(connector=connector) as session:
# # #             while to_visit and len(self.visited) < max_pages:
# # #                 url = to_visit.pop(0)
                
# # #                 # BUG FIX: Changed 'visited' to 'self.visited'
# # #                 if url in self.visited:
# # #                     continue
                
# # #                 self.visited.add(url)
# # #                 print(f"📄 Crawling: {url}")
                
# # #                 html = await self.fetch_page(session, url)
# # #                 if html:
# # #                     page_data = self.extract_data(html, url)
# # #                     self.pages.append(page_data)
                    
# # #                     # Add new links to visit
# # #                     for link in page_data['links']:
# # #                         if link not in self.visited and link not in to_visit:
# # #                             # Avoid common file extensions
# # #                             if not any(ext in link.lower() for ext in [
# # #                                 '.pdf', '.jpg', '.jpeg', '.png', '.gif', '.zip', 
# # #                                 '.css', '.js', '.xml', '.json', '.txt'
# # #                             ]):
# # #                                 to_visit.append(link)
                
# # #                 await asyncio.sleep(0.5)  # Be polite to servers
        
# # #         print(f"✅ Crawled {len(self.pages)} pages")
# # #         return self.pages


# # import asyncio
# # import aiohttp
# # from bs4 import BeautifulSoup
# # from urllib.parse import urljoin, urlparse
# # import re

# # class WebCrawler:
# #     def __init__(self, base_url):
# #         self.base_url = base_url
# #         self.domain = urlparse(base_url).netloc
# #         self.visited = set()
# #         self.pages = []
    
# #     async def fetch_page(self, session, url):
# #         """Fetch a single page"""
# #         try:
# #             headers = {
# #                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
# #             }
# #             async with session.get(url, timeout=10, headers=headers, allow_redirects=True) as response:
# #                 if response.status == 200:
# #                     html = await response.text()
# #                     return html
# #                 return None
# #         except Exception as e:
# #             print(f"Error fetching {url}: {e}")
# #             return None
    
# #     def extract_data(self, html, url):
# #         """Extract all relevant data from HTML"""
# #         soup = BeautifulSoup(html, 'html.parser')
        
# #         # Extract metadata
# #         title = soup.find('title')
# #         title_text = title.get_text().strip() if title else ""
        
# #         meta_desc = soup.find('meta', attrs={'name': 'description'})
# #         description = meta_desc.get('content', '') if meta_desc else ""
        
# #         # Extract all text content
# #         for script in soup(["script", "style", "noscript"]):
# #             script.decompose()
        
# #         text = soup.get_text()
# #         lines = (line.strip() for line in text.splitlines())
# #         chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# #         text = ' '.join(chunk for chunk in chunks if chunk)
        
# #         # Extract headings
# #         headings = {
# #             'h1': [h.get_text().strip() for h in soup.find_all('h1')],
# #             'h2': [h.get_text().strip() for h in soup.find_all('h2')],
# #             'h3': [h.get_text().strip() for h in soup.find_all('h3')]
# #         }
        
# #         # Extract links
# #         links = []
# #         for link in soup.find_all('a', href=True):
# #             href = link['href']
# #             absolute_url = urljoin(url, href)
# #             parsed = urlparse(absolute_url)
            
# #             if parsed.netloc == self.domain:
# #                 clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
# #                 links.append(clean_url)
        
# #         # Extract images
# #         images = []
# #         for img in soup.find_all('img'):
# #             images.append({
# #                 'src': img.get('src', ''),
# #                 'alt': img.get('alt', '')
# #             })
        
# #         return {
# #             'url': url,
# #             'title': title_text,
# #             'description': description,
# #             'text': text,
# #             'headings': headings,
# #             'links': list(set(links)),
# #             'images': images,
# #             'word_count': len(text.split()),
# #             'raw_html': html  # Store raw HTML for schema detection
# #         }
    
# #     async def crawl(self, max_pages=10):
# #         """Crawl the website"""
# #         to_visit = [self.base_url]
        
# #         connector = aiohttp.TCPConnector(ssl=False)
# #         async with aiohttp.ClientSession(connector=connector) as session:
# #             while to_visit and len(self.visited) < max_pages:
# #                 url = to_visit.pop(0)
                
# #                 if url in self.visited:
# #                     continue
                
# #                 self.visited.add(url)
# #                 print(f"📄 Crawling: {url}")
                
# #                 html = await self.fetch_page(session, url)
# #                 if html:
# #                     page_data = self.extract_data(html, url)
# #                     self.pages.append(page_data)
                    
# #                     for link in page_data['links']:
# #                         if link not in self.visited and link not in to_visit:
# #                             if not any(ext in link.lower() for ext in [
# #                                 '.pdf', '.jpg', '.jpeg', '.png', '.gif', '.zip', 
# #                                 '.css', '.js', '.xml', '.json', '.txt'
# #                             ]):
# #                                 to_visit.append(link)
                
# #                 await asyncio.sleep(0.5)
        
# #         print(f"✅ Crawled {len(self.pages)} pages")
# #         return self.pages



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
#         print(f"🌐 Initialized crawler for domain: {self.domain}")
    
#     async def fetch_page(self, session, url):
#         """Fetch a single page with retries"""
#         try:
#             headers = {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#             }
#             print(f"   📡 Fetching: {url}")
            
#             async with session.get(url, timeout=15, headers=headers, allow_redirects=True, ssl=False) as response:
#                 print(f"      Status: {response.status}")
#                 if response.status == 200:
#                     html = await response.text()
#                     print(f"      ✅ Got {len(html)} bytes of HTML")
#                     return html
#                 else:
#                     print(f"      ⚠️ Non-200 status code")
#                     return None
#         except asyncio.TimeoutError:
#             print(f"      ⏱️ Timeout for {url}")
#             return None
#         except Exception as e:
#             print(f"      ❌ Error fetching {url}: {type(e).__name__}: {str(e)[:100]}")
#             return None
    
#     def extract_data(self, html, url):
#         """Extract all relevant data from HTML"""
#         soup = BeautifulSoup(html, 'html.parser')
        
#         # Extract metadata
#         title = soup.find('title')
#         title_text = title.get_text().strip() if title else ""
        
#         meta_desc = soup.find('meta', attrs={'name': 'description'})
#         if not meta_desc:
#             meta_desc = soup.find('meta', attrs={'property': 'og:description'})
#         description = meta_desc.get('content', '').strip() if meta_desc else ""
        
#         # Extract all text content
#         for script in soup(["script", "style", "noscript", "iframe"]):
#             script.decompose()
        
#         text = soup.get_text()
#         lines = (line.strip() for line in text.splitlines())
#         chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
#         text = ' '.join(chunk for chunk in chunks if chunk)
        
#         word_count = len(text.split())
        
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
#             parsed = urlparse(absolute_url)
            
#             if parsed.netloc == self.domain:
#                 clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}".rstrip('/')
#                 if clean_url not in links:
#                     links.append(clean_url)
        
#         # Extract images
#         images = []
#         for img in soup.find_all('img'):
#             images.append({
#                 'src': img.get('src', ''),
#                 'alt': img.get('alt', '').strip()
#             })
        
#         print(f"      📝 Extracted: {word_count} words, {len(headings['h1'])} H1s, {len(images)} images")
        
#         return {
#             'url': url,
#             'title': title_text,
#             'description': description,
#             'text': text,
#             'headings': headings,
#             'links': links,
#             'images': images,
#             'word_count': word_count,
#             'raw_html': html[:5000]  # Store first 5000 chars for schema detection
#         }
    
#     async def crawl(self, max_pages=10):
#         """Crawl the website"""
#         to_visit = [self.base_url]
        
#         print(f"\n🕷️ Starting crawl (max {max_pages} pages)...")
        
#         connector = aiohttp.TCPConnector(ssl=False, limit=10)
#         timeout = aiohttp.ClientTimeout(total=30)
        
#         async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
#             while to_visit and len(self.visited) < max_pages:
#                 url = to_visit.pop(0)
                
#                 if url in self.visited:
#                     continue
                
#                 self.visited.add(url)
#                 print(f"\n📄 [{len(self.visited)}/{max_pages}] Crawling: {url}")
                
#                 html = await self.fetch_page(session, url)
                
#                 if html:
#                     try:
#                         page_data = self.extract_data(html, url)
#                         self.pages.append(page_data)
                        
#                         # Add new links to visit
#                         for link in page_data['links'][:20]:  # Limit links per page
#                             if link not in self.visited and link not in to_visit:
#                                 # Avoid common file extensions
#                                 if not any(ext in link.lower() for ext in [
#                                     '.pdf', '.jpg', '.jpeg', '.png', '.gif', '.zip', 
#                                     '.css', '.js', '.xml', '.json', '.txt', '.doc',
#                                     '.mp4', '.mp3', '.avi', '.mov'
#                                 ]):
#                                     to_visit.append(link)
#                     except Exception as e:
#                         print(f"      ❌ Error extracting data: {type(e).__name__}: {str(e)[:100]}")
                
#                 await asyncio.sleep(0.5)  # Be polite to servers
        
#         print(f"\n✅ Crawl complete! Found {len(self.pages)} pages")
#         return self.pages


import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import hashlib

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.visited = set()
        self.pages = []
        self.request_count = 0
        print(f"\n🌐 Crawler initialized")
        print(f"   Domain: {self.domain}")
        print(f"   Base URL: {base_url}\n")
    
    async def fetch_page(self, session, url):
        """Fetch a single page with detailed logging"""
        self.request_count += 1
        request_id = self.request_count
        
        print(f"📡 [{request_id}] Fetching: {url}")
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            
            async with session.get(
                url, 
                timeout=aiohttp.ClientTimeout(total=20),
                headers=headers, 
                allow_redirects=True,
                ssl=False
            ) as response:
                
                status = response.status
                content_type = response.headers.get('Content-Type', '')
                
                print(f"   └─ Status: {status}")
                print(f"   └─ Content-Type: {content_type}")
                
                if status == 200:
                    html = await response.text()
                    html_hash = hashlib.md5(html.encode()).hexdigest()[:8]
                    
                    print(f"   └─ ✅ Success! Got {len(html):,} bytes")
                    print(f"   └─ Content hash: {html_hash}")
                    
                    return html
                else:
                    print(f"   └─ ⚠️  Non-200 status")
                    return None
                    
        except asyncio.TimeoutError:
            print(f"   └─ ⏱️  TIMEOUT after 20s")
            return None
        except aiohttp.ClientError as e:
            print(f"   └─ ❌ Client error: {type(e).__name__}")
            return None
        except Exception as e:
            print(f"   └─ ❌ Error: {type(e).__name__}: {str(e)[:50]}")
            return None
    
    def extract_data(self, html, url):
        """Extract data with detailed logging"""
        print(f"\n   📝 Extracting data from {url}")
        
        soup = BeautifulSoup(html, 'html.parser')
        
        # Title
        title_tag = soup.find('title')
        title = title_tag.get_text().strip() if title_tag else ""
        print(f"      Title: '{title[:60]}{'...' if len(title) > 60 else ''}'")
        
        # Meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if not meta_desc:
            meta_desc = soup.find('meta', attrs={'property': 'og:description'})
        description = meta_desc.get('content', '').strip() if meta_desc else ""
        print(f"      Meta: '{description[:60]}{'...' if len(description) > 60 else ''}'")
        
        # Clean text
        for tag in soup(["script", "style", "noscript", "iframe", "nav", "footer", "header"]):
            tag.decompose()
        
        text = soup.get_text(separator=' ', strip=True)
        text = ' '.join(text.split())  # Normalize whitespace
        word_count = len(text.split())
        
        print(f"      Words: {word_count:,}")
        print(f"      Text preview: '{text[:80]}...'")
        
        # Headings
        h1_tags = soup.find_all('h1')
        h2_tags = soup.find_all('h2')
        h3_tags = soup.find_all('h3')
        
        headings = {
            'h1': [h.get_text().strip() for h in h1_tags],
            'h2': [h.get_text().strip() for h in h2_tags],
            'h3': [h.get_text().strip() for h in h3_tags]
        }
        
        print(f"      H1: {len(headings['h1'])} {headings['h1'][:2] if headings['h1'] else []}")
        print(f"      H2: {len(headings['h2'])}")
        print(f"      H3: {len(headings['h3'])}")
        
        # Links
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            absolute_url = urljoin(url, href)
            parsed = urlparse(absolute_url)
            
            if parsed.netloc == self.domain:
                clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}".rstrip('/')
                if clean_url and clean_url not in links:
                    links.append(clean_url)
        
        print(f"      Links: {len(links)} internal links found")
        
        # Images
        images = []
        for img in soup.find_all('img'):
            images.append({
                'src': img.get('src', ''),
                'alt': img.get('alt', '').strip()
            })
        
        print(f"      Images: {len(images)}")
        
        return {
            'url': url,
            'title': title,
            'description': description,
            'text': text,
            'headings': headings,
            'links': links,
            'images': images,
            'word_count': word_count,
            'raw_html': html[:5000]
        }
    
    async def crawl(self, max_pages=10):
        """Crawl website with detailed logging"""
        to_visit = [self.base_url]
        
        print(f"\n{'='*70}")
        print(f"🕷️  STARTING CRAWL")
        print(f"   Target: {self.base_url}")
        print(f"   Max pages: {max_pages}")
        print(f"{'='*70}\n")
        
        connector = aiohttp.TCPConnector(ssl=False, limit=5)
        timeout = aiohttp.ClientTimeout(total=30)
        
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            while to_visit and len(self.visited) < max_pages:
                url = to_visit.pop(0)
                
                if url in self.visited:
                    continue
                
                self.visited.add(url)
                
                print(f"\n{'─'*70}")
                print(f"📄 Page {len(self.visited)}/{max_pages}")
                print(f"{'─'*70}")
                
                html = await self.fetch_page(session, url)
                
                if html:
                    try:
                        page_data = self.extract_data(html, url)
                        self.pages.append(page_data)
                        
                        print(f"   ✅ Page extracted successfully\n")
                        
                        # Add new links
                        new_links = 0
                        for link in page_data['links'][:15]:
                            if link not in self.visited and link not in to_visit:
                                if not any(ext in link.lower() for ext in [
                                    '.pdf', '.jpg', '.jpeg', '.png', '.gif', '.zip', 
                                    '.css', '.js', '.xml', '.json', '.txt'
                                ]):
                                    to_visit.append(link)
                                    new_links += 1
                        
                        if new_links > 0:
                            print(f"   🔗 Added {new_links} new URLs to queue")
                        
                    except Exception as e:
                        print(f"   ❌ Extraction error: {type(e).__name__}: {str(e)[:100]}")
                else:
                    print(f"   ❌ Failed to fetch page\n")
                
                await asyncio.sleep(1)  # Be polite
        
        print(f"\n{'='*70}")
        print(f"✅ CRAWL COMPLETE")
        print(f"   Pages crawled: {len(self.pages)}")
        print(f"   Total requests: {self.request_count}")
        print(f"{'='*70}\n")
        
        # Summary
        if self.pages:
            total_words = sum(p['word_count'] for p in self.pages)
            print(f"📊 SUMMARY:")
            print(f"   Total words: {total_words:,}")
            print(f"   Avg words/page: {total_words // len(self.pages):,}")
            print(f"   Pages with H1: {sum(1 for p in self.pages if p['headings']['h1'])}")
            print(f"   Total images: {sum(len(p['images']) for p in self.pages)}")
            print()
        
        return self.pages