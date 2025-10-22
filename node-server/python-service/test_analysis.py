import asyncio
import json
from crawler import WebCrawler
from nlp_analyzer import NLPAnalyzer

async def test_analysis(url):
    print(f"\n🔍 Testing analysis for: {url}\n")
    
    # Test crawler
    print("1️⃣ Testing Crawler...")
    crawler = WebCrawler(url)
    pages = await crawler.crawl(max_pages=3)
    print(f"   ✅ Crawled {len(pages)} pages")
    
    if pages:
        first_page = pages[0]
        print(f"   📄 First page title: {first_page['title']}")
        print(f"   📝 Word count: {first_page['word_count']}")
        print(f"   🔗 Links found: {len(first_page['links'])}")
    
    # Test analyzer
    print("\n2️⃣ Testing NLP Analyzer...")
    nlp_analyzer = NLPAnalyzer()
    
    all_results = []
    for page in pages:
        analysis = nlp_analyzer.analyze_page(page)
        all_results.append(analysis)
        print(f"   ✅ Analyzed: {page['url']}")
        print(f"      Score: {analysis['seo_score']['score']}")
        print(f"      Keywords: {[k['word'] for k in analysis['keywords'][:5]]}")
    
    # Test report generation
    print("\n3️⃣ Testing Report Generation...")
    final_report = nlp_analyzer.generate_report(all_results)
    
    print(f"   📊 Summary:")
    print(f"      Total Pages: {final_report['summary']['total_pages']}")
    print(f"      Avg SEO Score: {final_report['summary']['average_seo_score']}")
    print(f"      Total Words: {final_report['summary']['total_words']}")
    print(f"      Top Keywords: {[k['word'] for k in final_report['top_keywords'][:5]]}")
    print(f"      Common Issues: {len(final_report['common_issues'])}")
    
    print("\n✅ Test complete!\n")
    print("📄 Full report:")
    print(json.dumps(final_report, indent=2))
    
    return final_report

if __name__ == "__main__":
    # Test with different URLs
    test_urls = [
        "https://example.com",
        "https://github.com",
    ]
    
    for url in test_urls:
        print("\n" + "="*60)
        asyncio.run(test_analysis(url))
        print("="*60)