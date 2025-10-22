from scorer.scoring import compute_overall_score

# Test with sample data
features = {
    'title': 'Example Domain',
    'meta_description': 'This domain is for use in illustrative examples',
    'word_count': 100,
    'headings': [{'tag': 'h1', 'text': 'Example Domain'}],
    'images_missing_alt': 0,
    'links_count': 1,
    'has_schema': False,
    'readability': {'flesch': 65}
}

result = compute_overall_score(features)
print("✅ Scorer test successful!")
print(f"Score: {result['overall_score']}")
print(f"Breakdown: {result['breakdown']}")
print(f"Issues: {result['notes']}")




# PS C:\Users\DELL INS 5510\Desktop\seo frontend\backend\node-server\python-service> python test_scorer.py
# ✅ Scorer test successful!
# Score: 58.0
# Breakdown: {'content': 55.0, 'technical': 71.0, 'onpage': 51.0}
# # Issues: ['Very short content — consider adding more helpful content (>300 words).', 'No structured data (JSON-LD) detected — adding Schema can help rich results.', 'Title is short or missing — include target keywords in the title (50-70 chars).']