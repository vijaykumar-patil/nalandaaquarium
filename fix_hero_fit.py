import glob

files = glob.glob("blog-*.html")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    content = content.replace('object-fit: contain;', 'object-fit: cover;')
    
    # Let's also remove the light grey background from the hero image just in case
    content = content.replace('background: #f9f9f9;', 'background: transparent;')
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Done updating hero images to cover!")
