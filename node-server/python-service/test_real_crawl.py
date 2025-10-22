import asyncio
from crawler import WebCrawler

async def test_multiple_sites():
    """Test crawling different websites to verify we get different data"""
    
    test_sites = [
        "https://example.com",
        "https://www.python.org",
    ]
    
    for url in test_sites:
        print(f"\n{'='*70}")
        print(f"🔍 TESTING: {url}")
        print(f"{'='*70}\n")
        
        crawler = WebCrawler(url)
        pages = await crawler.crawl(max_pages=3)
        
        if not pages:
            print(f"❌ NO PAGES CRAWLED FOR {url}!")
            continue
        
        print(f"\n✅ Successfully crawled {len(pages)} pages\n")
        
        for i, page in enumerate(pages, 1):
            print(f"Page {i}:")
            print(f"  URL: {page['url']}")
            print(f"  Title: {page['title']}")
            print(f"  Word Count: {page['word_count']}")
            print(f"  H1 Count: {len(page['headings']['h1'])}")
            print(f"  H1 Tags: {page['headings']['h1'][:2]}")
            print(f"  First 100 chars: {page['text'][:100]}...")
            print(f"  Images: {len(page['images'])}")
            print(f"  Links: {len(page['links'])}")
            print()
        
        print(f"{'='*70}\n")
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(test_multiple_sites())