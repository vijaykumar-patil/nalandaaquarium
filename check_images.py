import glob
import re
import os
import urllib.parse

html_files = glob.glob("*.html")
missing_images = []

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    images = re.findall(r'src="([^"]+)"', content)
    for img in images:
        if img.startswith('media/') or img.startswith('images/'):
            # decode url encoded paths like %20
            decoded_path = urllib.parse.unquote(img)
            if not os.path.exists(decoded_path):
                missing_images.append((file, img))

if missing_images:
    print("Found missing images:")
    for f, img in missing_images:
        print(f"File: {f} -> Missing: {img}")
else:
    print("No missing images found.")
