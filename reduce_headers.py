import os

blog_files = [
    'blog-solar-tanning.html',
    'blog-custom-aquarium.html',
    'blog-freshwater-fish.html',
    'blog-filtration.html'
]

for file in blog_files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Reduce h2 size
    content = content.replace('font-size: 2.2em;', 'font-size: 1.8em;')
    
    # Reduce h3 size
    content = content.replace('font-size: 1.5em;', 'font-size: 1.3em;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Reduced header sizes in {file}")
