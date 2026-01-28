import sqlite3
import os
from datetime import datetime, timedelta
from collections import defaultdict

temp_path = os.environ.get('TEMP', '/tmp')
history_path = os.path.join(temp_path, 'ChromeHistory')

conn = sqlite3.connect(history_path)
cursor = conn.cursor()

# December 1, 2025 onwards
start_date = "2025-12-01"

print("\n" + "="*100)
print("COMPREHENSIVE LEARNING & WORKFLOW ANALYSIS")
print(f"Period: December 2025 - January 2026")
print("="*100)

# 1. YouTube Learning Content
print("\n" + "="*100)
print("📚 YOUTUBE LEARNING - Videos Watched (Dec 2025 - Now)")
print("="*100 + "\n")

cursor.execute('''
    SELECT title, url, visit_count, datetime(last_visit_time/1000000-11644473600, "unixepoch", "localtime")
    FROM urls 
    WHERE url LIKE '%youtube.com/watch%' 
    AND last_visit_time > (strftime('%s', ?) * 1000000 + 11644473600000000)
    ORDER BY visit_count DESC
    LIMIT 80
''', (start_date,))

youtube_videos = cursor.fetchall()
print(f"{'Views':<8} {'Title'}")
print("-"*95)
for row in youtube_videos:
    title, url, visits, last_visit = row
    if title:
        title = title.replace(' - YouTube', '').strip()
        if len(title) > 3 and 'YouTube' not in title:
            print(f"[{visits:>4}]   {title[:88]}")

# 2. Documentation & Tutorials
print("\n" + "="*100)
print("📖 DOCUMENTATION & TUTORIALS (Dec 2025 - Now)")
print("="*100 + "\n")

cursor.execute('''
    SELECT url, title, visit_count
    FROM urls 
    WHERE (url LIKE '%docs.%' OR url LIKE '%documentation%' OR url LIKE '%tutorial%' 
           OR url LIKE '%learn%' OR url LIKE '%guide%' OR url LIKE '%how-to%'
           OR url LIKE '%readme%' OR url LIKE '%/docs/%' OR url LIKE '%developer%')
    AND last_visit_time > (strftime('%s', ?) * 1000000 + 11644473600000000)
    AND title IS NOT NULL AND title != ''
    ORDER BY visit_count DESC
    LIMIT 60
''', (start_date,))

print(f"{'Visits':<8} {'Domain':<30} {'Title'}")
print("-"*95)
for row in cursor.fetchall():
    url, title, visits = row
    if title and len(title) > 3:
        domain = url.split('/')[2] if url.startswith('http') else url[:30]
        domain = domain.replace('www.', '')[:28]
        title = title[:55] + '...' if len(title) > 55 else title
        print(f"[{visits:>4}]   {domain:<30} {title}")

# 3. AI Tools Usage
print("\n" + "="*100)
print("🤖 AI TOOLS & PLATFORMS (Dec 2025 - Now)")
print("="*100 + "\n")

ai_platforms = [
    ('Google AI Studio', '%aistudio.google%'),
    ('ChatGPT', '%chatgpt.com%'),
    ('Perplexity', '%perplexity.ai%'),
    ('NotebookLM', '%notebooklm%'),
    ('Lovable.dev', '%lovable.dev%'),
    ('Claude/Anthropic', '%claude%'),
    ('Hugging Face', '%huggingface%'),
    ('Replicate', '%replicate%'),
    ('OpenAI Platform', '%openai.com%'),
    ('Gemini', '%gemini.google%'),
    ('GitHub Copilot', '%copilot%'),
    ('Midjourney', '%midjourney%'),
    ('Cursor AI', '%cursor.%'),
    ('v0.dev (Vercel)', '%v0.dev%'),
    ('Bolt.new', '%bolt.new%'),
    ('Stitch (Google)', '%stitch.withgoogle%'),
    ('Replit', '%replit%'),
    ('Poe', '%poe.com%'),
    ('Character AI', '%character.ai%'),
    ('Groq', '%groq%'),
    ('Together AI', '%together.ai%'),
    ('Cohere', '%cohere%'),
]

print(f"{'Platform':<25} {'Pages':<8} {'Visits':<10} {'Intensity'}")
print("-"*60)
for name, pattern in ai_platforms:
    cursor.execute(f'''
        SELECT COUNT(*), SUM(visit_count)
        FROM urls 
        WHERE url LIKE '{pattern}'
        AND last_visit_time > (strftime('%s', ?) * 1000000 + 11644473600000000)
    ''', (start_date,))
    pages, visits = cursor.fetchone()
    if visits and visits > 0:
        if visits > 500:
            intensity = "🔥🔥🔥 HEAVY"
        elif visits > 200:
            intensity = "🔥🔥 HIGH"
        elif visits > 50:
            intensity = "🔥 MODERATE"
        else:
            intensity = "📌 LIGHT"
        print(f"{name:<25} {pages:<8} {visits:<10} {intensity}")

# 4. GitHub Activity
print("\n" + "="*100)
print("💻 GITHUB REPOSITORIES & ACTIVITY (Dec 2025 - Now)")
print("="*100 + "\n")

cursor.execute('''
    SELECT url, title, visit_count
    FROM urls 
    WHERE url LIKE '%github.com%'
    AND last_visit_time > (strftime('%s', ?) * 1000000 + 11644473600000000)
    AND url NOT LIKE '%/assets/%'
    AND url NOT LIKE '%githubusercontent%'
    ORDER BY visit_count DESC
    LIMIT 50
''', (start_date,))

print(f"{'Visits':<8} {'Repository/Page':<45} {'Title'}")
print("-"*100)
for row in cursor.fetchall():
    url, title, visits = row
    parts = url.replace('https://github.com/', '').split('/')
    if len(parts) >= 2:
        repo = '/'.join(parts[:2])[:43]
    else:
        repo = (parts[0] if parts else url)[:43]
    title = ((title or 'No title')[:45] + '..') if title and len(title) > 45 else (title or '')
    print(f"[{visits:>4}]   {repo:<45} {title}")

# 5. All websites by category
print("\n" + "="*100)
print("🌐 TOP WEBSITES BY CATEGORY (Dec 2025 - Now)")
print("="*100 + "\n")

cursor.execute('''
    SELECT 
        CASE 
            WHEN url LIKE '%github%' THEN 'GitHub'
            WHEN url LIKE '%linkedin%' THEN 'LinkedIn'
            WHEN url LIKE '%youtube%' THEN 'YouTube'
            WHEN url LIKE '%google.com%' OR url LIKE '%googleapis%' THEN 'Google Services'
            WHEN url LIKE '%docs.google%' THEN 'Google Docs'
            WHEN url LIKE '%aistudio%' OR url LIKE '%notebooklm%' OR url LIKE '%chatgpt%' OR url LIKE '%perplexity%' OR url LIKE '%lovable%' THEN 'AI Tools'
            WHEN url LIKE '%telegram%' OR url LIKE '%whatsapp%' THEN 'Messaging'
            WHEN url LIKE '%instagram%' OR url LIKE '%twitter%' OR url LIKE '%x.com%' THEN 'Social Media'
            WHEN url LIKE '%mail%' OR url LIKE '%outlook%' THEN 'Email'
            WHEN url LIKE '%notion%' OR url LIKE '%figma%' OR url LIKE '%canva%' THEN 'Productivity'
            WHEN url LIKE '%netlify%' OR url LIKE '%vercel%' OR url LIKE '%render%' THEN 'Deployment'
            WHEN url LIKE '%azure%' OR url LIKE '%aws%' THEN 'Cloud'
            ELSE 'Other'
        END as category,
        SUM(visit_count) as total_visits
    FROM urls
    WHERE last_visit_time > (strftime('%s', ?) * 1000000 + 11644473600000000)
    GROUP BY category
    ORDER BY total_visits DESC
''', (start_date,))

print(f"{'Category':<25} {'Visits':<10} {'Visual'}")
print("-"*70)
for row in cursor.fetchall():
    category, visits = row
    bar = '█' * min(int(visits / 100), 40)
    print(f"{category:<25} {visits:<10} {bar}")

# 6. Specific Learning Topics
print("\n" + "="*100)
print("📚 SPECIFIC LEARNING TOPICS DETECTED (Dec 2025 - Now)")
print("="*100 + "\n")

learning_topics = {
    'Machine Learning/AI': ['machine learning', 'neural', 'llm', 'transformer', 'gpt', 'gemini', 'langchain', 'embedding'],
    'Computer Vision': ['segment anything', 'sam', 'yolo', 'opencv', 'image recognition', 'object detection'],
    'Web Development': ['react', 'nextjs', 'tailwind', 'typescript', 'javascript', 'css', 'html', 'frontend'],
    'Cloud/DevOps': ['azure', 'aws', 'docker', 'kubernetes', 'terraform', 'ci/cd', 'deploy'],
    'APIs & Integration': ['api', 'rest', 'graphql', 'webhook', 'oauth', 'authentication'],
    'Databases': ['sql', 'postgres', 'mongodb', 'supabase', 'firebase', 'database'],
    'Python': ['python', 'pip', 'pandas', 'numpy', 'fastapi', 'django', 'flask'],
    'Mobile Development': ['android', 'ios', 'react native', 'flutter', 'mobile'],
    'LaTeX/Documents': ['latex', 'overleaf', 'tex', 'typeset'],
    'Startup/Business': ['startup', 'founder', 'venture', 'pitch', 'investor', 'business model'],
}

for topic, keywords in learning_topics.items():
    total = 0
    for kw in keywords:
        cursor.execute('''
            SELECT SUM(visit_count)
            FROM urls 
            WHERE (LOWER(url) LIKE ? OR LOWER(title) LIKE ?)
            AND last_visit_time > (strftime('%s', ?) * 1000000 + 11644473600000000)
        ''', (f'%{kw}%', f'%{kw}%', start_date))
        result = cursor.fetchone()[0]
        if result:
            total += result
    if total > 0:
        bar = '█' * min(int(total / 20), 30)
        print(f"{topic:<25} {total:>6} visits  {bar}")

# 7. Search History
print("\n" + "="*100)
print("🔎 SEARCH QUERIES (Dec 2025 - Now)")
print("="*100 + "\n")

cursor.execute('''
    SELECT url, datetime(last_visit_time/1000000-11644473600, "unixepoch", "localtime")
    FROM urls 
    WHERE (url LIKE '%google.com/search%' OR url LIKE '%perplexity.ai/search%' OR url LIKE '%bing.com/search%')
    AND last_visit_time > (strftime('%s', ?) * 1000000 + 11644473600000000)
    ORDER BY last_visit_time DESC
    LIMIT 60
''', (start_date,))

import urllib.parse
searches = []
for row in cursor.fetchall():
    url, timestamp = row
    try:
        parsed = urllib.parse.urlparse(url)
        query_params = urllib.parse.parse_qs(parsed.query)
        query = query_params.get('q', query_params.get('query', ['']))[0]
        if query and len(query) > 3 and query not in searches:
            searches.append(query)
            print(f"  • {query[:90]}")
    except:
        pass

# 8. Career & Jobs
print("\n" + "="*100)
print("💼 CAREER & JOB SEARCH ACTIVITY (Dec 2025 - Now)")
print("="*100 + "\n")

cursor.execute('''
    SELECT title, visit_count, datetime(last_visit_time/1000000-11644473600, "unixepoch", "localtime")
    FROM urls 
    WHERE (url LIKE '%linkedin.com%job%' OR url LIKE '%indeed%' OR url LIKE '%glassdoor%' 
           OR title LIKE '%job%' OR title LIKE '%career%' OR title LIKE '%hiring%' OR title LIKE '%apply%')
    AND last_visit_time > (strftime('%s', ?) * 1000000 + 11644473600000000)
    ORDER BY visit_count DESC
    LIMIT 30
''', (start_date,))

for row in cursor.fetchall():
    title, visits, timestamp = row
    if title and len(title) > 5:
        print(f"  [{visits:>3}x] {title[:85]}")

# 9. Courses & Educational Platforms
print("\n" + "="*100)
print("🎓 COURSES & EDUCATIONAL PLATFORMS (Dec 2025 - Now)")
print("="*100 + "\n")

edu_sites = [
    ('%coursera%', 'Coursera'),
    ('%udemy%', 'Udemy'),
    ('%edx%', 'edX'),
    ('%pluralsight%', 'Pluralsight'),
    ('%linkedin.com/learning%', 'LinkedIn Learning'),
    ('%freecodecamp%', 'FreeCodeCamp'),
    ('%codecademy%', 'Codecademy'),
    ('%skillshare%', 'Skillshare'),
    ('%brilliant%', 'Brilliant'),
    ('%khanacademy%', 'Khan Academy'),
    ('%datacamp%', 'DataCamp'),
    ('%santander%', 'Santander X'),
    ('%futurelearn%', 'FutureLearn'),
    ('%aws.training%', 'AWS Training'),
    ('%learn.microsoft%', 'Microsoft Learn'),
]

for pattern, name in edu_sites:
    cursor.execute(f'''
        SELECT SUM(visit_count), COUNT(*)
        FROM urls 
        WHERE url LIKE '{pattern}'
        AND last_visit_time > (strftime('%s', ?) * 1000000 + 11644473600000000)
    ''', (start_date,))
    visits, pages = cursor.fetchone()
    if visits and visits > 0:
        print(f"  {name:<25} {visits:>5} visits across {pages:>3} pages")

# 10. Time analysis
print("\n" + "="*100)
print("⏰ ACTIVITY TIMELINE (Dec 2025 - Now)")
print("="*100 + "\n")

cursor.execute('''
    SELECT 
        strftime('%Y-%m-%d', datetime(last_visit_time/1000000-11644473600, 'unixepoch', 'localtime')) as day,
        COUNT(*) as page_visits,
        SUM(visit_count) as total_visits
    FROM urls
    WHERE last_visit_time > (strftime('%s', ?) * 1000000 + 11644473600000000)
    GROUP BY day
    ORDER BY day DESC
    LIMIT 60
''', (start_date,))

print(f"{'Date':<15} {'Pages':<10} {'Visits':<10} {'Activity'}")
print("-"*60)
for row in cursor.fetchall():
    day, pages, visits = row
    bar = '█' * min(int(visits / 50), 30)
    print(f"{day:<15} {pages:<10} {visits:<10} {bar}")

conn.close()

print("\n" + "="*100)
print("END OF EXTENDED ANALYSIS (Dec 2025 - Jan 2026)")
print("="*100 + "\n")
