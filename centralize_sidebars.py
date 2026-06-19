import os
import glob

# Replace logic for generate_store.py
gen_file = "generate_store.py"
with open(gen_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace left sidebar in generate_store.py
left_old = '''    <!-- Left Sidebar for Store & Stock -->
    <aside class="sticky-sidebar">
      <div class="sidebar-title">Store & Stock</div>
      
      <a href="store-fishes.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Fishes</h5>
      </a>
      <a href="store-aquariums.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Aquariums</h5>
      </a>
      <a href="store-lights.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Lights</h5>
      </a>
      <a href="store-filters.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Filters</h5>
      </a>
      <a href="store-heaters.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Heaters</h5>
      </a>
      <a href="store-airpumps.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Air Pumps</h5>
      </a>
    </aside>'''

left_new = '''    <!-- Left Sidebar for Store & Stock -->
    <aside id="left-sidebar" class="sticky-sidebar"></aside>'''
content = content.replace(left_old, left_new)

# Right sidebar in generate_store.py has multiple occurrences, just replace with regex
import re

content = re.sub(
    r'<!-- Right Sidebar for Blogs -->\s*<aside class="sticky-sidebar">.*?</aside>', 
    '<!-- Right Sidebar for Blogs -->\n    <aside id="right-sidebar" class="sticky-sidebar"></aside>', 
    content, 
    flags=re.DOTALL
)

# Add script tag before </body>
content = content.replace('</body>', '<script src="sidebar.js"></script>\n</body>')

with open(gen_file, 'w', encoding='utf-8') as f:
    f.write(content)

# Now do the same for all html files in the directory
html_files = glob.glob("*.html")
for file in html_files:
    if file.startswith("store-"):
        continue # these will be regenerated anyway
    
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    html = html.replace(left_old, left_new)
    
    html = re.sub(
        r'<!-- Right Sidebar for Blogs -->\s*<aside class="sticky-sidebar">.*?</aside>', 
        '<!-- Right Sidebar for Blogs -->\n    <aside id="right-sidebar" class="sticky-sidebar"></aside>', 
        html, 
        flags=re.DOTALL
    )
    
    if '<script src="sidebar.js"></script>' not in html:
        html = html.replace('</body>', '  <script src="sidebar.js"></script>\n</body>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Centralized sidebars across all files!")
