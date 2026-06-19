import glob
import re

files = glob.glob("*.html")
files.append("generate_store.py")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We will use regex to remove the <a class="floating-wa-button">...</a> block
    # It contains an <svg> block.
    # Pattern to match <a href="..." class="floating-wa-button"...>...</a>
    pattern = r'<a[^>]*class="floating-wa-button"[^>]*>.*?</a>'
    
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed from {file}")

print("Done")
