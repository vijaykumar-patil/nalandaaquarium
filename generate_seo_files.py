import glob
import os
from datetime import datetime

DOMAIN = "https://www.nalandaaquarium.com" # Placeholder domain

html_files = glob.glob("*.html")
# Filter out google verification file
html_files = [f for f in html_files if not f.startswith("google")]

sitemap_urls = []
date_str = datetime.now().strftime("%Y-%m-%d")

for file in html_files:
    if file == "index.html":
        priority = "1.0"
        url = DOMAIN + "/"
    elif file in ["store.html", "blog.html"]:
        priority = "0.9"
        url = DOMAIN + "/" + file
    else:
        priority = "0.8"
        url = DOMAIN + "/" + file
        
    sitemap_urls.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{date_str}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>"""

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print("Generated sitemap.xml")

robots_txt = f"""User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""

with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_txt)
print("Generated robots.txt")
