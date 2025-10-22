import asyncio
from crawler import WebCrawler

async def debug_crawl(url):
    print(f"\n{'='*60}")
    print(f"🔍 DEBUG CRAWLING: {url}")
    print(f"{'='*60}\n")
    
    crawler = WebCrawler(url)
    pages = await crawler.crawl(max_pages=5)
    
    print(f"\n✅ Results:")
    print(f"   Total pages: {len(pages)}")
    
    for i, page in enumerate(pages, 1):
        print(f"\n   Page {i}:")
        print(f"   URL: {page['url']}")
        print(f"   Title: {page['title'][:50]}...")
        print(f"   Word count: {page['word_count']}")
        print(f"   H1 count: {len(page['headings']['h1'])}")
        print(f"   Images: {len(page['images'])}")
        print(f"   Links: {len(page['links'])}")
        print(f"   Description: {page['description'][:80]}...")
    
    return pages

if __name__ == "__main__":
    test_urls = [
        "https://example.com",
        "https://www.python.org",
    ]
    
    for url in test_urls:
        asyncio.run(debug_crawl(url))
        print("\n" + "="*60 + "\n")