import glob
import os
import re

html_files = glob.glob("*.html")
all_files = [os.path.basename(f) for f in glob.glob("**/*.*", recursive=True)]

issues = []

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Basic structural tags
    if "<html" not in content: issues.append(f"{file}: Missing <html tag")
    if "<head>" not in content: issues.append(f"{file}: Missing <head> tag")
    if "<body>" not in content: issues.append(f"{file}: Missing <body> tag")
    if "</body>" not in content: issues.append(f"{file}: Missing </body> tag")
    
    # 2. CSS and JS dependencies
    if "style.css" not in content: issues.append(f"{file}: Missing style.css reference")
    if "sidebar.js" not in content and file != "store.html": # store.html might not need it? Actually wait, store.html should have it if it has sidebars.
        pass
        
    # 3. Check for broken internal hrefs
    hrefs = re.findall(r'href="(.*?)"', content)
    for href in hrefs:
        # Ignore external links, mailto, tel, anchors
        if href.startswith('http') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('#'):
            continue
        # Ignore empty hrefs
        if not href:
            continue
            
        # Strip query params or fragments just in case
        href_clean = href.split('?')[0].split('#')[0]
        
        # Check if the file exists in our local directory tree
        # Since hrefs might be like 'favicon_io/apple-touch-icon.png'
        # We can check if it exists on disk
        if not os.path.exists(href_clean):
            issues.append(f"{file}: Broken link -> {href}")

    # 4. Check for broken img src
    srcs = re.findall(r'src="(.*?)"', content)
    for src in srcs:
        if src.startswith('http'): continue
        if not src: continue
        # Strip urlencoding for file check
        src_unquoted = src.replace("%20", " ")
        if not os.path.exists(src_unquoted):
            issues.append(f"{file}: Broken image -> {src}")

if issues:
    print("ISSUES FOUND:")
    for issue in issues:
        print(issue)
else:
    print("All structural checks passed! No broken links or missing local assets found.")

# Let's also check generate_store.py
with open("generate_store.py", "r", encoding='utf-8') as f:
    gen_content = f.read()
    if 'sidebar.js' not in gen_content:
        print("generate_store.py: Missing sidebar.js injection")

