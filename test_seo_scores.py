import sys
sys.path.insert(0, r'c:\Users\DELL INS 5510\Desktop\try\backend\node-server\python-service\generator')

from app import generate_content, analyze_content_quality, calculate_seo_scores

topic = "Digital Marketing Strategy"
keywords = ["digital marketing", "marketing strategy", "online marketing"]
audience = "business owners"
tone = "professional"

html = generate_content("blog", topic, keywords, tone, audience)
print(f"Generated Content Length: {len(html)} characters")
print(f"Word count: {len(html.split())}")

analysis = analyze_content_quality(html, keywords, 0)
print(f"\nContent Analysis:")
print(f"  Actual word count: {analysis['actual_word_count']}")
print(f"  Keyword density: {analysis['keyword_density']}%")
print(f"  Keyword coverage: {analysis['keyword_coverage']} keywords found")
print(f"  Heading score: {analysis['heading_score']}")
print(f"  Readability: {analysis['readability']}")
print(f"  Meta tags: {analysis['meta_tags_score']}")
print(f"  Content length score: {analysis['content_length_score']}")

seo_scores = calculate_seo_scores(analysis, keywords)
print(f"\nSEO Scores:")
for key, value in seo_scores.items():
    print(f"  {key}: {value}")
