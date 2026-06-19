import glob

files = glob.glob("*.html")
files.append("generate_store.py")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace style.css with style.css?v=2
    # Ensure we don't accidentally make it style.css?v=2?v=2
    content = content.replace('href="style.css"', 'href="style.css?v=2"')
    content = content.replace('href="style.css?v=2?v=2"', 'href="style.css?v=2"')
    
    content = content.replace('src="sidebar.js"', 'src="sidebar.js?v=2"')
    content = content.replace('src="sidebar.js?v=2?v=2"', 'src="sidebar.js?v=2"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cache busting tags added!")
