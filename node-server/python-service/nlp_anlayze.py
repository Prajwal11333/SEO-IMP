import re
from collections import Counter
import spacy
from textblob import TextBlob

class NLPAnalyzer:
    def __init__(self):
        # Load spaCy model (download first: python -m spacy download en_core_web_sm)
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            print("Warning: spaCy model not found. Using basic analysis.")
            self.nlp = None
    
    def extract_keywords(self, text, top_n=20):
        """Extract keywords using frequency analysis"""
        # Remove common stop words
        stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 
                         'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are', 
                         'was', 'were', 'be', 'been', 'being', 'have', 'has', 
                         'had', 'do', 'does', 'did', 'will', 'would', 'could', 
                         'should', 'may', 'might', 'can', 'this', 'that', 'these', 
                         'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'])
        
        # Clean and tokenize
        words = re.findall(r'\b[a-z]{3,}\b', text.lower())
        filtered_words = [w for w in words if w not in stop_words]
        
        # Count frequencies
        word_freq = Counter(filtered_words)
        return word_freq.most_common(top_n)
    
    def extract_entities(self, text):
        """Extract named entities using spaCy"""
        if not self.nlp:
            return []
        
        doc = self.nlp(text[:1000000])  # Limit text length
        entities = []
        for ent in doc.ents:
            entities.append({
                'text': ent.text,
                'label': ent.label_
            })
        return entities
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of the text"""
        try:
            blob = TextBlob(text[:5000])  # Limit for performance
            polarity = blob.sentiment.polarity
            
            if polarity > 0.1:
                sentiment = "positive"
            elif polarity < -0.1:
                sentiment = "negative"
            else:
                sentiment = "neutral"
            
            return {
                'polarity': round(polarity, 2),
                'sentiment': sentiment
            }
        except:
            return {'polarity': 0, 'sentiment': 'neutral'}
    
    def calculate_readability(self, text):
        """Calculate readability score"""
        sentences = text.count('.') + text.count('!') + text.count('?')
        words = len(text.split())
        
        if sentences == 0 or words == 0:
            return 0
        
        # Simple readability metric
        avg_words_per_sentence = words / sentences
        
        # Flesch Reading Ease approximation
        score = 206.835 - 1.015 * avg_words_per_sentence
        score = max(0, min(100, score))
        
        return round(score, 1)
    
    def analyze_page(self, page_data):
        """Analyze a single page"""
        text = page_data['text']
        
        # Extract keywords
        keywords = self.extract_keywords(text, top_n=15)
        
        # Extract entities
        entities = self.extract_entities(text)
        
        # Analyze sentiment
        sentiment = self.analyze_sentiment(text)
        
        # Calculate readability
        readability = self.calculate_readability(text)
        
        # SEO Score calculation
        seo_score = self.calculate_seo_score(page_data)
        
        return {
            'url': page_data['url'],
            'title': page_data['title'],
            'word_count': page_data['word_count'],
            'keywords': [{'word': k[0], 'count': k[1]} for k in keywords],
            'entities': entities[:10],
            'sentiment': sentiment,
            'readability': readability,
            'seo_score': seo_score,
            'headings_count': {
                'h1': len(page_data['headings']['h1']),
                'h2': len(page_data['headings']['h2']),
                'h3': len(page_data['headings']['h3'])
            },
            'images_count': len(page_data['images']),
            'images_without_alt': sum(1 for img in page_data['images'] if not img['alt'])
        }
    
    def calculate_seo_score(self, page_data):
        """Calculate basic SEO score"""
        score = 100
        issues = []
        
        # Title check
        if not page_data['title']:
            score -= 10
            issues.append('Missing title tag')
        elif len(page_data['title']) < 30 or len(page_data['title']) > 60:
            score -= 5
            issues.append('Title length not optimal')
        
        # Meta description
        if not page_data['description']:
            score -= 10
            issues.append('Missing meta description')
        elif len(page_data['description']) < 120 or len(page_data['description']) > 160:
            score -= 5
            issues.append('Meta description length not optimal')
        
        # H1 tags
        if len(page_data['headings']['h1']) == 0:
            score -= 10
            issues.append('Missing H1 tag')
        elif len(page_data['headings']['h1']) > 1:
            score -= 5
            issues.append('Multiple H1 tags')
        
        # Images without alt
        if page_data['images']:
            alt_ratio = sum(1 for img in page_data['images'] if img['alt']) / len(page_data['images'])
            if alt_ratio < 0.5:
                score -= 10
                issues.append('Many images missing alt text')
        
        # Word count
        if page_data['word_count'] < 300:
            score -= 10
            issues.append('Content too short')
        
        return {
            'score': max(0, score),
            'issues': issues
        }
    
    def generate_report(self, all_results):
        """Generate final SEO report"""
        total_pages = len(all_results)
        avg_score = sum(r['seo_score']['score'] for r in all_results) / total_pages if total_pages > 0 else 0
        
        # Aggregate keywords from all pages
        all_keywords = {}
        for result in all_results:
            for kw in result['keywords']:
                word = kw['word']
                all_keywords[word] = all_keywords.get(word, 0) + kw['count']
        
        top_keywords = sorted(all_keywords.items(), key=lambda x: x[1], reverse=True)[:20]
        
        # Aggregate issues
        all_issues = []
        for result in all_results:
            all_issues.extend(result['seo_score']['issues'])
        
        issue_counts = Counter(all_issues)
        
        return {
            'summary': {
                'total_pages': total_pages,
                'average_seo_score': round(avg_score, 1),
                'total_words': sum(r['word_count'] for r in all_results),
                'total_images': sum(r['images_count'] for r in all_results)
            },
            'top_keywords': [{'word': k[0], 'count': k[1]} for k in top_keywords],
            'common_issues': [{'issue': k, 'count': v} for k, v in issue_counts.most_common()],
            'pages': all_results,
            'technical_score': {
                'on_page_seo': round(avg_score, 1),
                'content_quality': self.calculate_content_score(all_results),
                'mobile_friendly': 85,  # Placeholder
                'performance': 78  # Placeholder
            }
        }
    
    def calculate_content_score(self, results):
        """Calculate content quality score"""
        avg_readability = sum(r['readability'] for r in results) / len(results) if results else 0
        avg_word_count = sum(r['word_count'] for r in results) / len(results) if results else 0
        
        score = 50
        if avg_readability > 60:
            score += 20
        if avg_word_count > 500:
            score += 20
        
        return min(100, score)