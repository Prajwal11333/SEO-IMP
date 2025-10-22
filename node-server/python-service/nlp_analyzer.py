# # # import re
# # # from collections import Counter
# # # import spacy
# # # from textblob import TextBlob

# # # class NLPAnalyzer:
# # #     def __init__(self):
# # #         # Load spaCy model (download first: python -m spacy download en_core_web_sm)
# # #         try:
# # #             self.nlp = spacy.load("en_core_web_sm")
# # #         except:
# # #             print("Warning: spaCy model not found. Using basic analysis.")
# # #             self.nlp = None
    
# # #     def extract_keywords(self, text, top_n=20):
# # #         """Extract keywords using frequency analysis"""
# # #         # Remove common stop words
# # #         stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 
# # #                          'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are', 
# # #                          'was', 'were', 'be', 'been', 'being', 'have', 'has', 
# # #                          'had', 'do', 'does', 'did', 'will', 'would', 'could', 
# # #                          'should', 'may', 'might', 'can', 'this', 'that', 'these', 
# # #                          'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'])
        
# # #         # Clean and tokenize
# # #         words = re.findall(r'\b[a-z]{3,}\b', text.lower())
# # #         filtered_words = [w for w in words if w not in stop_words]
        
# # #         # Count frequencies
# # #         word_freq = Counter(filtered_words)
# # #         return word_freq.most_common(top_n)
    
# # #     def extract_entities(self, text):
# # #         """Extract named entities using spaCy"""
# # #         if not self.nlp:
# # #             return []
        
# # #         doc = self.nlp(text[:1000000])  # Limit text length
# # #         entities = []
# # #         for ent in doc.ents:
# # #             entities.append({
# # #                 'text': ent.text,
# # #                 'label': ent.label_
# # #             })
# # #         return entities
    
# # #     def analyze_sentiment(self, text):
# # #         """Analyze sentiment of the text"""
# # #         try:
# # #             blob = TextBlob(text[:5000])  # Limit for performance
# # #             polarity = blob.sentiment.polarity
            
# # #             if polarity > 0.1:
# # #                 sentiment = "positive"
# # #             elif polarity < -0.1:
# # #                 sentiment = "negative"
# # #             else:
# # #                 sentiment = "neutral"
            
# # #             return {
# # #                 'polarity': round(polarity, 2),
# # #                 'sentiment': sentiment
# # #             }
# # #         except:
# # #             return {'polarity': 0, 'sentiment': 'neutral'}
    
# # #     def calculate_readability(self, text):
# # #         """Calculate readability score"""
# # #         sentences = text.count('.') + text.count('!') + text.count('?')
# # #         words = len(text.split())
        
# # #         if sentences == 0 or words == 0:
# # #             return 0
        
# # #         # Simple readability metric
# # #         avg_words_per_sentence = words / sentences
        
# # #         # Flesch Reading Ease approximation
# # #         score = 206.835 - 1.015 * avg_words_per_sentence
# # #         score = max(0, min(100, score))
        
# # #         return round(score, 1)
    
# # #     def analyze_page(self, page_data):
# # #         """Analyze a single page"""
# # #         text = page_data['text']
        
# # #         # Extract keywords
# # #         keywords = self.extract_keywords(text, top_n=15)
        
# # #         # Extract entities
# # #         entities = self.extract_entities(text)
        
# # #         # Analyze sentiment
# # #         sentiment = self.analyze_sentiment(text)
        
# # #         # Calculate readability
# # #         readability = self.calculate_readability(text)
        
# # #         # SEO Score calculation
# # #         seo_score = self.calculate_seo_score(page_data)
        
# # #         return {
# # #             'url': page_data['url'],
# # #             'title': page_data['title'],
# # #             'word_count': page_data['word_count'],
# # #             'keywords': [{'word': k[0], 'count': k[1]} for k in keywords],
# # #             'entities': entities[:10],
# # #             'sentiment': sentiment,
# # #             'readability': readability,
# # #             'seo_score': seo_score,
# # #             'headings_count': {
# # #                 'h1': len(page_data['headings']['h1']),
# # #                 'h2': len(page_data['headings']['h2']),
# # #                 'h3': len(page_data['headings']['h3'])
# # #             },
# # #             'images_count': len(page_data['images']),
# # #             'images_without_alt': sum(1 for img in page_data['images'] if not img['alt'])
# # #         }
    
# # #     def calculate_seo_score(self, page_data):
# # #         """Calculate basic SEO score"""
# # #         score = 100
# # #         issues = []
        
# # #         # Title check
# # #         if not page_data['title']:
# # #             score -= 10
# # #             issues.append('Missing title tag')
# # #         elif len(page_data['title']) < 30 or len(page_data['title']) > 60:
# # #             score -= 5
# # #             issues.append('Title length not optimal')
        
# # #         # Meta description
# # #         if not page_data['description']:
# # #             score -= 10
# # #             issues.append('Missing meta description')
# # #         elif len(page_data['description']) < 120 or len(page_data['description']) > 160:
# # #             score -= 5
# # #             issues.append('Meta description length not optimal')
        
# # #         # H1 tags
# # #         if len(page_data['headings']['h1']) == 0:
# # #             score -= 10
# # #             issues.append('Missing H1 tag')
# # #         elif len(page_data['headings']['h1']) > 1:
# # #             score -= 5
# # #             issues.append('Multiple H1 tags')
        
# # #         # Images without alt
# # #         if page_data['images']:
# # #             alt_ratio = sum(1 for img in page_data['images'] if img['alt']) / len(page_data['images'])
# # #             if alt_ratio < 0.5:
# # #                 score -= 10
# # #                 issues.append('Many images missing alt text')
        
# # #         # Word count
# # #         if page_data['word_count'] < 300:
# # #             score -= 10
# # #             issues.append('Content too short')
        
# # #         return {
# # #             'score': max(0, score),
# # #             'issues': issues
# # #         }
    
# # #     def generate_report(self, all_results):
# # #         """Generate final SEO report"""
# # #         total_pages = len(all_results)
# # #         avg_score = sum(r['seo_score']['score'] for r in all_results) / total_pages if total_pages > 0 else 0
        
# # #         # Aggregate keywords from all pages
# # #         all_keywords = {}
# # #         for result in all_results:
# # #             for kw in result['keywords']:
# # #                 word = kw['word']
# # #                 all_keywords[word] = all_keywords.get(word, 0) + kw['count']
        
# # #         top_keywords = sorted(all_keywords.items(), key=lambda x: x[1], reverse=True)[:20]
        
# # #         # Aggregate issues
# # #         all_issues = []
# # #         for result in all_results:
# # #             all_issues.extend(result['seo_score']['issues'])
        
# # #         issue_counts = Counter(all_issues)
        
# # #         return {
# # #             'summary': {
# # #                 'total_pages': total_pages,
# # #                 'average_seo_score': round(avg_score, 1),
# # #                 'total_words': sum(r['word_count'] for r in all_results),
# # #                 'total_images': sum(r['images_count'] for r in all_results)
# # #             },
# # #             'top_keywords': [{'word': k[0], 'count': k[1]} for k in top_keywords],
# # #             'common_issues': [{'issue': k, 'count': v} for k, v in issue_counts.most_common()],
# # #             'pages': all_results,
# # #             'technical_score': {
# # #                 'on_page_seo': round(avg_score, 1),
# # #                 'content_quality': self.calculate_content_score(all_results),
# # #                 'mobile_friendly': 85,  # Placeholder
# # #                 'performance': 78  # Placeholder
# # #             }
# # #         }
    
# # #     def calculate_content_score(self, results):
# # #         """Calculate content quality score"""
# # #         avg_readability = sum(r['readability'] for r in results) / len(results) if results else 0
# # #         avg_word_count = sum(r['word_count'] for r in results) / len(results) if results else 0
        
# # #         score = 50
# # #         if avg_readability > 60:
# # #             score += 20
# # #         if avg_word_count > 500:
# # #             score += 20
        
# # #         return min(100, score)


# # import re
# # from collections import Counter

# # class NLPAnalyzer:
# #     def __init__(self):
# #         pass
    
# #     def extract_keywords(self, text, top_n=20):
# #         """Extract keywords using frequency analysis"""
# #         stop_words = set([
# #             'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 
# #             'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are', 
# #             'was', 'were', 'be', 'been', 'being', 'have', 'has', 
# #             'had', 'do', 'does', 'did', 'will', 'would', 'could', 
# #             'should', 'may', 'might', 'can', 'this', 'that', 'these', 
# #             'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they',
# #             'what', 'which', 'who', 'when', 'where', 'why', 'how',
# #             'all', 'each', 'every', 'both', 'few', 'more', 'most',
# #             'other', 'some', 'such', 'no', 'nor', 'not', 'only',
# #             'own', 'same', 'so', 'than', 'too', 'very', 'just'
# #         ])
        
# #         # Clean and tokenize
# #         words = re.findall(r'\b[a-z]{4,}\b', text.lower())
# #         filtered_words = [w for w in words if w not in stop_words]
        
# #         # Count frequencies
# #         word_freq = Counter(filtered_words)
# #         return word_freq.most_common(top_n)
    
# #     def calculate_seo_score(self, page_data):
# #         """Calculate SEO score for a page"""
# #         score = 100
# #         issues = []
        
# #         # Title check
# #         title = page_data.get('title', '')
# #         if not title:
# #             score -= 15
# #             issues.append('Missing title tag')
# #         elif len(title) < 30:
# #             score -= 8
# #             issues.append('Title too short (< 30 chars)')
# #         elif len(title) > 70:
# #             score -= 8
# #             issues.append('Title too long (> 70 chars)')
        
# #         # Meta description
# #         description = page_data.get('description', '')
# #         if not description:
# #             score -= 15
# #             issues.append('Missing meta description')
# #         elif len(description) < 120:
# #             score -= 8
# #             issues.append('Meta description too short (< 120 chars)')
# #         elif len(description) > 160:
# #             score -= 8
# #             issues.append('Meta description too long (> 160 chars)')
        
# #         # H1 tags
# #         h1_count = len(page_data['headings']['h1'])
# #         if h1_count == 0:
# #             score -= 15
# #             issues.append('Missing H1 tag')
# #         elif h1_count > 1:
# #             score -= 10
# #             issues.append(f'Multiple H1 tags ({h1_count} found)')
        
# #         # Images without alt
# #         if page_data['images']:
# #             images_without_alt = sum(1 for img in page_data['images'] if not img['alt'])
# #             if images_without_alt > 0:
# #                 ratio = images_without_alt / len(page_data['images'])
# #                 if ratio > 0.5:
# #                     score -= 12
# #                     issues.append(f'{images_without_alt}/{len(page_data["images"])} images missing alt text')
        
# #         # Word count
# #         word_count = page_data.get('word_count', 0)
# #         if word_count < 300:
# #             score -= 15
# #             issues.append(f'Content too short ({word_count} words, recommend 300+)')
        
# #         # H2 headings
# #         if len(page_data['headings']['h2']) == 0:
# #             score -= 5
# #             issues.append('No H2 headings found')
        
# #         return {
# #             'score': max(0, min(100, score)),
# #             'issues': issues
# #         }
    
# #     def analyze_page(self, page_data):
# #         """Analyze a single page"""
# #         text = page_data['text']
        
# #         # Extract keywords
# #         keywords = self.extract_keywords(text, top_n=15)
        
# #         # SEO Score
# #         seo_score = self.calculate_seo_score(page_data)
        
# #         return {
# #             'url': page_data['url'],
# #             'title': page_data['title'],
# #             'word_count': page_data['word_count'],
# #             'keywords': [{'word': k[0], 'count': k[1]} for k in keywords],
# #             'seo_score': seo_score,
# #             'h1_count': len(page_data['headings']['h1']),
# #             'h2_count': len(page_data['headings']['h2']),
# #             'h3_count': len(page_data['headings']['h3']),
# #             'images_count': len(page_data['images']),
# #             'images_without_alt': sum(1 for img in page_data['images'] if not img['alt'])
# #         }
    
# #     def generate_report(self, all_results):
# #         """Generate final SEO report"""
# #         total_pages = len(all_results)
# #         avg_score = sum(r['seo_score']['score'] for r in all_results) / total_pages if total_pages > 0 else 0
        
# #         # Aggregate keywords from all pages
# #         all_keywords = {}
# #         for result in all_results:
# #             for kw in result['keywords']:
# #                 word = kw['word']
# #                 all_keywords[word] = all_keywords.get(word, 0) + kw['count']
        
# #         top_keywords = sorted(all_keywords.items(), key=lambda x: x[1], reverse=True)[:20]
        
# #         # Aggregate issues
# #         all_issues = []
# #         for result in all_results:
# #             all_issues.extend(result['seo_score']['issues'])
        
# #         issue_counts = Counter(all_issues)
        
# #         return {
# #             'summary': {
# #                 'total_pages': total_pages,
# #                 'average_seo_score': round(avg_score, 1),
# #                 'total_words': sum(r['word_count'] for r in all_results),
# #                 'total_images': sum(r['images_count'] for r in all_results)
# #             },
# #             'top_keywords': [{'word': k[0], 'count': k[1]} for k in top_keywords],
# #             'common_issues': [{'issue': k, 'count': v} for k, v in issue_counts.most_common()],
# #             'pages': all_results,
# #             'technical_score': {
# #                 'on_page_seo': round(avg_score, 1),
# #                 'content_quality': self.calculate_content_quality_score(all_results),
# #                 'mobile_friendly': 85,
# #                 'performance': 78
# #             }
# #         }
    
# #     def calculate_content_quality_score(self, results):
# #         """Calculate overall content quality"""
# #         if not results:
# #             return 0
        
# #         avg_word_count = sum(r['word_count'] for r in results) / len(results)
        
# #         score = 50
# #         if avg_word_count > 500:
# #             score += 30
# #         elif avg_word_count > 300:
# #             score += 20
        
# #         # Check for structured content (headings)
# #         avg_h2 = sum(r['h2_count'] for r in results) / len(results)
# #         if avg_h2 > 3:
# #             score += 20
# #         elif avg_h2 > 1:
# #             score += 10
        
# #         return min(100, score)



# import re
# from collections import Counter
# from scorer.scoring import compute_overall_score

# class NLPAnalyzer:
#     def __init__(self):
#         pass
    
#     def extract_keywords(self, text, top_n=20):
#         """Extract keywords using frequency analysis"""
#         stop_words = set([
#             'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 
#             'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are', 
#             'was', 'were', 'be', 'been', 'being', 'have', 'has', 
#             'had', 'do', 'does', 'did', 'will', 'would', 'could', 
#             'should', 'may', 'might', 'can', 'this', 'that', 'these', 
#             'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they',
#             'what', 'which', 'who', 'when', 'where', 'why', 'how',
#             'all', 'each', 'every', 'both', 'few', 'more', 'most',
#             'other', 'some', 'such', 'no', 'nor', 'not', 'only',
#             'own', 'same', 'so', 'than', 'too', 'very', 'just'
#         ])
        
#         words = re.findall(r'\b[a-z]{4,}\b', text.lower())
#         filtered_words = [w for w in words if w not in stop_words]
#         word_freq = Counter(filtered_words)
#         return word_freq.most_common(top_n)
    
#     def calculate_readability(self, text):
#         """Calculate Flesch Reading Ease score"""
#         if not text:
#             return 0
        
#         sentences = len(re.findall(r'[.!?]+', text)) or 1
#         words = len(text.split()) or 1
#         syllables = sum(self.count_syllables(word) for word in text.split())
        
#         # Flesch Reading Ease formula
#         flesch = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
#         return max(0, min(100, flesch))
    
#     def count_syllables(self, word):
#         """Rough syllable count"""
#         word = word.lower()
#         count = 0
#         vowels = 'aeiouy'
#         if word[0] in vowels:
#             count += 1
#         for index in range(1, len(word)):
#             if word[index] in vowels and word[index - 1] not in vowels:
#                 count += 1
#         if word.endswith('e'):
#             count -= 1
#         if count == 0:
#             count += 1
#         return count
    
#     def detect_schema(self, html_text):
#         """Check if page has structured data"""
#         if not html_text:
#             return False
#         # Simple check for JSON-LD or Schema markup
#         return 'application/ld+json' in html_text.lower() or 'schema.org' in html_text.lower()
    
#     def analyze_page(self, page_data):
#         """Analyze a single page using advanced scoring"""
#         text = page_data['text']
#         title = page_data.get('title', '')
#         description = page_data.get('description', '')
        
#         # Extract keywords
#         keywords = self.extract_keywords(text, top_n=15)
        
#         # Calculate readability
#         flesch_score = self.calculate_readability(text)
        
#         # Count images without alt
#         images_missing_alt = sum(1 for img in page_data.get('images', []) if not img.get('alt'))
        
#         # Count internal/external links
#         links = page_data.get('links', [])
#         links_count = len(links)
        
#         # Detect structured data
#         has_schema = self.detect_schema(page_data.get('raw_html', ''))
        
#         # Prepare headings for scoring
#         headings_list = []
#         for h1 in page_data['headings'].get('h1', []):
#             headings_list.append({'tag': 'h1', 'text': h1})
#         for h2 in page_data['headings'].get('h2', []):
#             headings_list.append({'tag': 'h2', 'text': h2})
#         for h3 in page_data['headings'].get('h3', []):
#             headings_list.append({'tag': 'h3', 'text': h3})
        
#         # Build features dict for scoring system
#         features = {
#             'title': title,
#             'meta_description': description,
#             'word_count': page_data.get('word_count', 0),
#             'headings': headings_list,
#             'images_missing_alt': images_missing_alt,
#             'links_count': links_count,
#             'has_schema': has_schema,
#             'readability': {
#                 'flesch': flesch_score
#             }
#         }
        
#         # Use your advanced scoring system
#         score_result = compute_overall_score(features)
        
#         # Build final result
#         return {
#             'url': page_data['url'],
#             'title': title,
#             'word_count': page_data['word_count'],
#             'keywords': [{'word': k[0], 'count': k[1]} for k in keywords],
#             'seo_score': {
#                 'score': score_result['overall_score'],
#                 'breakdown': score_result['breakdown'],
#                 'issues': score_result['notes']
#             },
#             'readability': flesch_score,
#             'h1_count': len(page_data['headings']['h1']),
#             'h2_count': len(page_data['headings']['h2']),
#             'h3_count': len(page_data['headings']['h3']),
#             'images_count': len(page_data.get('images', [])),
#             'images_without_alt': images_missing_alt,
#             'has_schema': has_schema
#         }
    
#     def generate_report(self, all_results):
#         """Generate final SEO report with advanced metrics"""
#         total_pages = len(all_results)
#         avg_score = sum(r['seo_score']['score'] for r in all_results) / total_pages if total_pages > 0 else 0
        
#         # Aggregate keywords
#         all_keywords = {}
#         for result in all_results:
#             for kw in result['keywords']:
#                 word = kw['word']
#                 all_keywords[word] = all_keywords.get(word, 0) + kw['count']
        
#         top_keywords = sorted(all_keywords.items(), key=lambda x: x[1], reverse=True)[:20]
        
#         # Aggregate all issues from all pages
#         all_issues = []
#         for result in all_results:
#             all_issues.extend(result['seo_score']['issues'])
        
#         issue_counts = Counter(all_issues)
        
#         # Calculate breakdown averages
#         avg_content = sum(r['seo_score']['breakdown']['content'] for r in all_results) / total_pages if total_pages > 0 else 0
#         avg_technical = sum(r['seo_score']['breakdown']['technical'] for r in all_results) / total_pages if total_pages > 0 else 0
#         avg_onpage = sum(r['seo_score']['breakdown']['onpage'] for r in all_results) / total_pages if total_pages > 0 else 0
        
#         return {
#             'summary': {
#                 'total_pages': total_pages,
#                 'average_seo_score': round(avg_score, 1),
#                 'total_words': sum(r['word_count'] for r in all_results),
#                 'total_images': sum(r['images_count'] for r in all_results),
#                 'avg_readability': round(sum(r['readability'] for r in all_results) / total_pages if total_pages > 0 else 0, 1)
#             },
#             'top_keywords': [{'word': k[0], 'count': k[1]} for k in top_keywords],
#             'common_issues': [{'issue': k, 'count': v} for k, v in issue_counts.most_common()],
#             'pages': all_results,
#             'technical_score': {
#                 'overall_seo': round(avg_score, 1),
#                 'content_quality': round(avg_content, 1),
#                 'technical_seo': round(avg_technical, 1),
#                 'onpage_seo': round(avg_onpage, 1)
#             }
#         }



import re
from collections import Counter
from scorer.scoring import compute_overall_score

class NLPAnalyzer:
    def __init__(self):
        pass
    
    def extract_keywords(self, text, top_n=20):
        """Extract keywords using frequency analysis"""
        stop_words = set([
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 
            'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are', 
            'was', 'were', 'be', 'been', 'being', 'have', 'has', 
            'had', 'do', 'does', 'did', 'will', 'would', 'could', 
            'should', 'may', 'might', 'can', 'this', 'that', 'these', 
            'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they',
            'what', 'which', 'who', 'when', 'where', 'why', 'how',
            'all', 'each', 'every', 'both', 'few', 'more', 'most',
            'other', 'some', 'such', 'no', 'nor', 'not', 'only',
            'own', 'same', 'so', 'than', 'too', 'very', 'just'
        ])
        
        words = re.findall(r'\b[a-z]{4,}\b', text.lower())
        filtered_words = [w for w in words if w not in stop_words]
        word_freq = Counter(filtered_words)
        return word_freq.most_common(top_n)
    
    def calculate_readability(self, text):
        """Calculate Flesch Reading Ease score"""
        if not text or len(text.strip()) == 0:
            return 0
        
        sentences = len(re.findall(r'[.!?]+', text))
        if sentences == 0:
            sentences = 1
            
        words = len(text.split())
        if words == 0:
            return 0
            
        syllables = sum(self.count_syllables(word) for word in text.split())
        
        # Flesch Reading Ease formula
        flesch = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
        return max(0, min(100, flesch))
    
    def count_syllables(self, word):
        """Rough syllable count"""
        word = word.lower()
        count = 0
        vowels = 'aeiouy'
        if len(word) == 0:
            return 0
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith('e'):
            count -= 1
        if count == 0:
            count += 1
        return count
    
    def detect_schema(self, html_text):
        """Check if page has structured data"""
        if not html_text:
            return False
        return 'application/ld+json' in html_text.lower() or 'schema.org' in html_text.lower()
    
    def analyze_page(self, page_data):
        """Analyze a single page using YOUR advanced scoring system"""
        text = page_data.get('text', '')
        title = page_data.get('title', '')
        description = page_data.get('description', '')
        
        print(f"\n   📄 Analyzing: {page_data.get('url', 'Unknown URL')}")
        print(f"      Title: {title[:50]}...")
        print(f"      Words: {page_data.get('word_count', 0)}")
        
        # Extract keywords
        keywords = self.extract_keywords(text, top_n=15)
        print(f"      Keywords extracted: {len(keywords)}")
        
        # Calculate readability
        flesch_score = self.calculate_readability(text)
        print(f"      Readability (Flesch): {flesch_score:.1f}")
        
        # Count images without alt
        images = page_data.get('images', [])
        images_missing_alt = sum(1 for img in images if not img.get('alt', '').strip())
        
        # Count links
        links = page_data.get('links', [])
        links_count = len(links)
        
        # Detect structured data
        has_schema = self.detect_schema(page_data.get('raw_html', ''))
        
        # Prepare headings for YOUR scoring system
        headings_list = []
        headings_dict = page_data.get('headings', {})
        
        for h1 in headings_dict.get('h1', []):
            headings_list.append({'tag': 'h1', 'text': h1})
        for h2 in headings_dict.get('h2', []):
            headings_list.append({'tag': 'h2', 'text': h2})
        for h3 in headings_dict.get('h3', []):
            headings_list.append({'tag': 'h3', 'text': h3})
        
        print(f"      H1 tags: {len(headings_dict.get('h1', []))}")
        print(f"      H2 tags: {len(headings_dict.get('h2', []))}")
        
        # Build features dict for YOUR scoring system
        features = {
            'title': title,
            'meta_description': description,
            'word_count': page_data.get('word_count', 0),
            'headings': headings_list,
            'images_missing_alt': images_missing_alt,
            'links_count': links_count,
            'has_schema': has_schema,
            'readability': {
                'flesch': flesch_score
            }
        }
        
        # Use YOUR advanced scoring system from scorer/scoring.py
        print(f"      🎯 Computing score with YOUR scoring system...")
        score_result = compute_overall_score(features)
        
        print(f"      ✅ Overall Score: {score_result['overall_score']}")
        print(f"      📊 Breakdown:")
        print(f"         - Content: {score_result['breakdown']['content']}")
        print(f"         - Technical: {score_result['breakdown']['technical']}")
        print(f"         - OnPage: {score_result['breakdown']['onpage']}")
        print(f"      ⚠️  Issues: {len(score_result['notes'])}")
        
        # Build final result with YOUR scoring
        return {
            'url': page_data['url'],
            'title': title,
            'word_count': page_data.get('word_count', 0),
            'keywords': [{'word': k[0], 'count': k[1]} for k in keywords],
            'seo_score': {
                'score': score_result['overall_score'],
                'breakdown': score_result['breakdown'],
                'issues': score_result['notes']
            },
            'readability': flesch_score,
            'h1_count': len(headings_dict.get('h1', [])),
            'h2_count': len(headings_dict.get('h2', [])),
            'h3_count': len(headings_dict.get('h3', [])),
            'images_count': len(images),
            'images_without_alt': images_missing_alt,
            'has_schema': has_schema
        }
    
    def generate_report(self, all_results):
        """Generate final SEO report with YOUR advanced metrics"""
        if not all_results:
            return self._empty_report()
        
        total_pages = len(all_results)
        avg_score = sum(r['seo_score']['score'] for r in all_results) / total_pages
        
        print(f"\n📊 Generating final report...")
        print(f"   Pages analyzed: {total_pages}")
        print(f"   Average score: {avg_score:.1f}")
        
        # Aggregate keywords from ALL pages
        all_keywords = {}
        for result in all_results:
            for kw in result['keywords']:
                word = kw['word']
                all_keywords[word] = all_keywords.get(word, 0) + kw['count']
        
        top_keywords = sorted(all_keywords.items(), key=lambda x: x[1], reverse=True)[:20]
        print(f"   Unique keywords found: {len(all_keywords)}")
        print(f"   Top keywords: {[k[0] for k in top_keywords[:5]]}")
        
        # Aggregate all issues from all pages
        all_issues = []
        for result in all_results:
            all_issues.extend(result['seo_score']['issues'])
        
        issue_counts = Counter(all_issues)
        print(f"   Total issues found: {len(all_issues)}")
        
        # Calculate breakdown averages
        avg_content = sum(r['seo_score']['breakdown']['content'] for r in all_results) / total_pages
        avg_technical = sum(r['seo_score']['breakdown']['technical'] for r in all_results) / total_pages
        avg_onpage = sum(r['seo_score']['breakdown']['onpage'] for r in all_results) / total_pages
        
        return {
            'summary': {
                'total_pages': total_pages,
                'average_seo_score': round(avg_score, 1),
                'total_words': sum(r['word_count'] for r in all_results),
                'total_images': sum(r['images_count'] for r in all_results),
                'avg_readability': round(sum(r['readability'] for r in all_results) / total_pages, 1)
            },
            'top_keywords': [{'word': k[0], 'count': k[1]} for k in top_keywords],
            'common_issues': [{'issue': k, 'count': v} for k, v in issue_counts.most_common()],
            'pages': all_results,
            'technical_score': {
                'overall_seo': round(avg_score, 1),
                'content_quality': round(avg_content, 1),
                'technical_seo': round(avg_technical, 1),
                'onpage_seo': round(avg_onpage, 1)
            }
        }
    
    def _empty_report(self):
        """Return empty report structure"""
        return {
            'summary': {
                'total_pages': 0,
                'average_seo_score': 0,
                'total_words': 0,
                'total_images': 0,
                'avg_readability': 0
            },
            'top_keywords': [],
            'common_issues': [],
            'pages': [],
            'technical_score': {
                'overall_seo': 0,
                'content_quality': 0,
                'technical_seo': 0,
                'onpage_seo': 0
            }
        }