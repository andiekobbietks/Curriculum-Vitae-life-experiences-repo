import sqlite3
import os
from datetime import datetime, timedelta
from collections import defaultdict

temp_path = os.environ.get('TEMP', '/tmp')
history_path = os.path.join(temp_path, 'ChromeHistory')

conn = sqlite3.connect(history_path)
cursor = conn.cursor()

print("\n" + "="*100)
print("COMPREHENSIVE LEARNING & WORKFLOW ANALYSIS")
print("="*100)

# 1. YouTube Learning Content
print("\n" + "="*100)
print("📚 YOUTUBE LEARNING - Videos Watched")
print("="*100 + "\n")

cursor.execute('''
    SELECT title, visit_count, datetime(last_visit_time/1000000-11644473600, "unixepoch", "localtime")
    FROM urls 
    WHERE url LIKE '%youtube.com/watch%' 
    AND last_visit_time > (strftime('%s', 'now', '-30 days') * 1000000 + 11644473600000000)
    AND title NOT LIKE '%YouTube%' OR title LIKE '%)%'
    ORDER BY visit_count DESC
    LIMIT 50
''')

youtube_videos = cursor.fetchall()
for row in youtube_videos:
    title, visits, last_visit = row
    if title and 'YouTube' not in title:
        title = title.replace(' - YouTube', '').strip()
        print(f"  [{visits:2} views] {title[:90]}")

# 2. Documentation & Tutorials
print("\n" + "="*100)
print("📖 DOCUMENTATION & TUTORIALS VISITED")
print("="*100 + "\n")

cursor.execute('''
    SELECT url, title, visit_count
    FROM urls 
    WHERE (url LIKE '%docs.%' OR url LIKE '%documentation%' OR url LIKE '%tutorial%' 
           OR url LIKE '%learn%' OR url LIKE '%guide%' OR url LIKE '%how-to%'
           OR url LIKE '%readme%' OR url LIKE '%wiki%' OR url LIKE '%/docs/%')
    AND last_visit_time > (strftime('%s', 'now', '-30 days') * 1000000 + 11644473600000000)
    ORDER BY visit_count DESC
    LIMIT 40
''')

for row in cursor.fetchall():
    url, title, visits = row
    if title:
        domain = url.split('/')[2] if url.startswith('http') else url[:30]
        title = title[:60] + '...' if len(title) > 60 else title
        print(f"  [{visits:2}x] {domain[:25]:<25} | {title}")

# 3. AI Tools Usage
print("\n" + "="*100)
print("🤖 AI TOOLS & PLATFORMS EXPLORED")
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
    ('OpenAI', '%openai.com%'),
    ('Gemini', '%gemini.google%'),
    ('Copilot', '%copilot%'),
    ('Midjourney', '%midjourney%'),
    ('Cursor', '%cursor.%'),
    ('v0.dev', '%v0.dev%'),
    ('Bolt', '%bolt.new%'),
    ('Stitch (Google)', '%stitch.withgoogle%'),
]

for name, pattern in ai_platforms:
    cursor.execute(f'''
        SELECT COUNT(*), SUM(visit_count)
        FROM urls 
        WHERE url LIKE '{pattern}'
        AND last_visit_time > (strftime('%s', 'now', '-30 days') * 1000000 + 11644473600000000)
    ''')
    pages, visits = cursor.fetchone()
    if visits and visits > 0:
        print(f"  {name:<25} | {visits:>5} visits across {pages:>3} pages")

# 4. GitHub Activity
print("\n" + "="*100)
print("💻 GITHUB REPOSITORIES & ACTIVITY")
print("="*100 + "\n")

cursor.execute('''
    SELECT url, title, visit_count
    FROM urls 
    WHERE url LIKE '%github.com%'
    AND last_visit_time > (strftime('%s', 'now', '-30 days') * 1000000 + 11644473600000000)
    AND url NOT LIKE '%/assets/%'
    ORDER BY visit_count DESC
    LIMIT 35
''')

for row in cursor.fetchall():
    url, title, visits = row
    # Extract repo path
    parts = url.replace('https://github.com/', '').split('/')
    if len(parts) >= 2:
        repo = '/'.join(parts[:2])
    else:
        repo = parts[0] if parts else url
    title = (title or 'No title')[:50]
    print(f"  [{visits:2}x] {repo[:40]:<40} | {title}")

# 5. Tech Stack / Tools
print("\n" + "="*100)
print("🛠️ TECHNOLOGIES & TOOLS RESEARCHED")
print("="*100 + "\n")

tech_keywords = {
    'LaTeX/Overleaf': ['overleaf', 'latex', 'texlive'],
    'Python': ['python.org', 'pypi', 'pip install'],
    'JavaScript/Node': ['nodejs', 'npmjs', 'javascript'],
    'React': ['reactjs', 'react.dev'],
    'AWS': ['aws.amazon', 'amazonaws'],
    'Azure': ['azure.microsoft', 'portal.azure'],
    'Docker': ['docker.com', 'dockerhub'],
    'Kubernetes': ['kubernetes.io', 'k8s'],
    'Terraform': ['terraform', 'hashicorp'],
    'Shopify': ['shopify'],
    'WordPress': ['wordpress'],
    'Netlify': ['netlify'],
    'Vercel': ['vercel'],
    'Supabase': ['supabase'],
    'Firebase': ['firebase'],
    'Tailwind': ['tailwindcss'],
    'Bootstrap': ['bootstrap'],
}

for tech, patterns in tech_keywords.items():
    total = 0
    for pattern in patterns:
        cursor.execute(f'''
            SELECT SUM(visit_count)
            FROM urls 
            WHERE url LIKE '%{pattern}%'
            AND last_visit_time > (strftime('%s', 'now', '-30 days') * 1000000 + 11644473600000000)
        ''')
        result = cursor.fetchone()[0]
        if result:
            total += result
    if total > 0:
        print(f"  {tech:<25} | {total:>5} visits")

# 6. Career & Professional Development
print("\n" + "="*100)
print("💼 CAREER & PROFESSIONAL DEVELOPMENT")
print("="*100 + "\n")

cursor.execute('''
    SELECT title, visit_count
    FROM urls 
    WHERE url LIKE '%linkedin.com%'
    AND last_visit_time > (strftime('%s', 'now', '-30 days') * 1000000 + 11644473600000000)
    AND (title LIKE '%job%' OR title LIKE '%career%' OR title LIKE '%hiring%' 
         OR title LIKE '%application%' OR title LIKE '%apply%' OR title LIKE '%position%'
         OR title LIKE '%Grow%' OR title LIKE '%Learning%')
    ORDER BY visit_count DESC
    LIMIT 15
''')

for row in cursor.fetchall():
    title, visits = row
    if title:
        print(f"  [{visits:2}x] {title[:80]}")

# 7. Startup & Business
print("\n" + "="*100)
print("🚀 STARTUP & BUSINESS ACTIVITY")
print("="*100 + "\n")

startup_sites = [
    ('%microsoft.com/startups%', 'Microsoft for Startups'),
    ('%ycombinator%', 'Y Combinator'),
    ('%stripe%', 'Stripe (Payments)'),
    ('%shopify%', 'Shopify'),
    ('%notion%', 'Notion'),
    ('%pitch.%', 'Pitch Decks'),
    ('%canva%', 'Canva (Design)'),
    ('%figma%', 'Figma'),
    ('%trello%', 'Trello'),
    ('%asana%', 'Asana'),
    ('%slack%', 'Slack'),
    ('%calendly%', 'Calendly'),
    ('%typeform%', 'Typeform'),
    ('%airtable%', 'Airtable'),
]

for pattern, name in startup_sites:
    cursor.execute(f'''
        SELECT SUM(visit_count)
        FROM urls 
        WHERE url LIKE '{pattern}'
        AND last_visit_time > (strftime('%s', 'now', '-30 days') * 1000000 + 11644473600000000)
    ''')
    visits = cursor.fetchone()[0]
    if visits and visits > 0:
        print(f"  {name:<30} | {visits:>5} visits")

# 8. Search Queries (from Google)
print("\n" + "="*100)
print("🔎 RECENT SEARCH TOPICS (Google/Perplexity)")
print("="*100 + "\n")

cursor.execute('''
    SELECT url, visit_count
    FROM urls 
    WHERE (url LIKE '%google.com/search%' OR url LIKE '%perplexity.ai/search%')
    AND last_visit_time > (strftime('%s', 'now', '-14 days') * 1000000 + 11644473600000000)
    ORDER BY last_visit_time DESC
    LIMIT 30
''')

import urllib.parse
for row in cursor.fetchall():
    url, visits = row
    try:
        parsed = urllib.parse.urlparse(url)
        query_params = urllib.parse.parse_qs(parsed.query)
        query = query_params.get('q', query_params.get('query', ['']))[0]
        if query and len(query) > 3:
            print(f"  • {query[:90]}")
    except:
        pass

# 9. Time Analysis
print("\n" + "="*100)
print("⏰ ACTIVITY BY TIME OF DAY")
print("="*100 + "\n")

cursor.execute('''
    SELECT 
        CASE 
            WHEN cast(strftime('%H', datetime(last_visit_time/1000000-11644473600, 'unixepoch', 'localtime')) as integer) BETWEEN 0 AND 5 THEN 'Night (12am-6am)'
            WHEN cast(strftime('%H', datetime(last_visit_time/1000000-11644473600, 'unixepoch', 'localtime')) as integer) BETWEEN 6 AND 11 THEN 'Morning (6am-12pm)'
            WHEN cast(strftime('%H', datetime(last_visit_time/1000000-11644473600, 'unixepoch', 'localtime')) as integer) BETWEEN 12 AND 17 THEN 'Afternoon (12pm-6pm)'
            ELSE 'Evening (6pm-12am)'
        END as time_period,
        COUNT(*) as visits
    FROM urls
    WHERE last_visit_time > (strftime('%s', 'now', '-7 days') * 1000000 + 11644473600000000)
    GROUP BY time_period
    ORDER BY visits DESC
''')

for row in cursor.fetchall():
    period, visits = row
    bar = '█' * (visits // 100)
    print(f"  {period:<25} | {visits:>5} | {bar}")

conn.close()

print("\n" + "="*100)
print("END OF ANALYSIS")
print("="*100 + "\n")
