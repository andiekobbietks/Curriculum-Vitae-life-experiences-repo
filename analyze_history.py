import sqlite3
import os
from datetime import datetime, timedelta

temp_path = os.environ.get('TEMP', '/tmp')
history_path = os.path.join(temp_path, 'ChromeHistory')

conn = sqlite3.connect(history_path)
cursor = conn.cursor()

# Get last week's most visited sites
print("\n" + "="*90)
print("YOUR BROWSING ACTIVITY - LAST 7 DAYS")
print("="*90 + "\n")

cursor.execute('''
    SELECT url, title, visit_count, 
           datetime(last_visit_time/1000000-11644473600, "unixepoch", "localtime") as last_visit
    FROM urls 
    WHERE last_visit_time > (strftime('%s', 'now', '-7 days') * 1000000 + 11644473600000000)
    ORDER BY visit_count DESC
    LIMIT 35
''')

print(f"{'Visits':<8} {'Last Visit':<20} {'Site':<35} {'Title'}")
print("-"*90)

for row in cursor.fetchall():
    url, title, visits, last_visit = row
    title = (title[:40] + '...') if title and len(title) > 40 else (title or 'No title')
    if url.startswith('http'):
        domain = url.split('/')[2].replace('www.', '')[:35]
    else:
        domain = url[:35]
    print(f"{visits:<8} {last_visit:<20} {domain:<35} {title}")

# Get total time by domain (approximation based on visits)
print("\n" + "="*90)
print("TOP DOMAINS BY ENGAGEMENT")
print("="*90 + "\n")

cursor.execute('''
    SELECT 
        CASE 
            WHEN url LIKE '%github%' THEN 'github.com'
            WHEN url LIKE '%google%ai%studio%' OR url LIKE '%aistudio%' THEN 'Google AI Studio'
            WHEN url LIKE '%chat.openai%' OR url LIKE '%chatgpt%' THEN 'ChatGPT'
            WHEN url LIKE '%youtube%' THEN 'youtube.com'
            WHEN url LIKE '%linkedin%' THEN 'linkedin.com'
            WHEN url LIKE '%stackoverflow%' THEN 'stackoverflow.com'
            WHEN url LIKE '%docs.google%' THEN 'Google Docs'
            WHEN url LIKE '%drive.google%' THEN 'Google Drive'
            WHEN url LIKE '%mail.google%' OR url LIKE '%gmail%' THEN 'Gmail'
            WHEN url LIKE '%outlook%' THEN 'Outlook'
            WHEN url LIKE '%twitter%' OR url LIKE '%x.com%' THEN 'Twitter/X'
            WHEN url LIKE '%shopify%' THEN 'Shopify'
            WHEN url LIKE '%wordpress%' THEN 'WordPress'
            WHEN url LIKE '%netlify%' THEN 'Netlify'
            WHEN url LIKE '%overleaf%' THEN 'Overleaf'
            WHEN url LIKE '%aws%' THEN 'AWS'
            WHEN url LIKE '%azure%' THEN 'Azure'
            ELSE substr(replace(replace(url, 'https://', ''), 'http://', ''), 1, instr(replace(replace(url, 'https://', ''), 'http://', ''), '/') - 1)
        END as domain,
        SUM(visit_count) as total_visits
    FROM urls
    WHERE last_visit_time > (strftime('%s', 'now', '-7 days') * 1000000 + 11644473600000000)
    GROUP BY domain
    HAVING total_visits > 2
    ORDER BY total_visits DESC
    LIMIT 20
''')

print(f"{'Domain':<35} {'Visits':<10} {'Est. Activity Level'}")
print("-"*60)

for row in cursor.fetchall():
    domain, visits = row
    if domain:
        # Rough activity level
        if visits > 50:
            level = "🔥 HEAVY USE"
        elif visits > 20:
            level = "⚡ FREQUENT"
        elif visits > 10:
            level = "📊 MODERATE"
        else:
            level = "📌 OCCASIONAL"
        print(f"{domain:<35} {visits:<10} {level}")

conn.close()
