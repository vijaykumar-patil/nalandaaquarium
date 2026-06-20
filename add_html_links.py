import glob
import re

html_links = """
    <div style="margin-top: 15px; font-size: 0.9em; text-align: center;">
      <a href="index.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Home</a> | 
      <a href="store.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Full Store</a> | 
      <a href="store-fishes.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Fishes</a> | 
      <a href="store-aquariums.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Aquariums</a> | 
      <a href="blog.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Blog</a>
    </div>
"""

files = glob.glob("*.html") + glob.glob("*.py")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "href=\"store-fishes.html\"" not in content and "All Rights Reserved" in content:
        # We will insert it before the <p>&copy; or <p style="..."> &copy;
        content = re.sub(r'(<p[^>]*>&copy;[^<]*All Rights Reserved\.</p>)', html_links + r'\n      \1', content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added HTML links to {file}")

print("Done updating SEO links globally!")
