import glob

html_links = """
    <div style="margin-top: 15px; font-size: 0.9em; text-align: center;">
      <a href="index.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Home</a> | 
      <a href="store.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Full Store</a> | 
      <a href="store-fishes.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Fishes</a> | 
      <a href="store-aquariums.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Aquariums</a> | 
      <a href="blog.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Blog</a>
    </div>
"""

target_string = '<p>&copy; 1962–<span id="year"></span> Nalanda Aquarium. All Rights Reserved.</p>'

files = glob.glob("*.html") + glob.glob("*.py")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if target_string in content and "margin: 0 10px;\">Fishes</a>" not in content:
        new_content = content.replace(target_string, html_links + "\n      " + target_string)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected links into {file}")

print("Done injecting safely!")
