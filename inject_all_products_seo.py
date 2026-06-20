import os
import urllib.parse
import glob

# Collect all product titles
store_dir = 'media/Store'
all_products = []

for root, _, files in os.walk(store_dir):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.webp')):
            name_no_ext = os.path.splitext(file)[0]
            display_title = urllib.parse.unquote(name_no_ext)
            all_products.append(display_title)

# Join them into a comma-separated string
all_products_string = ", ".join(sorted(all_products))

new_seo_block = f"""                <details style="margin-top: 15px; cursor: pointer; text-align: left; background: rgba(0,0,0,0.02); padding: 10px; border-radius: 5px; border: 1px solid rgba(0,0,0,0.05);">
          <summary style="color: var(--color-teal); font-weight: bold; outline: none; list-style: none;">&#9662; View Our Complete Stock Index</summary>
          <div style="margin-top: 10px; font-size: 0.9em; line-height: 1.5;">
            <strong>All Products & Stock:</strong> {all_products_string}
"""

print(f"Generated SEO block with {len(all_products)} products.")

# We need to replace the old stock list in all HTML files and python files
# The old block looks like:
# <strong>Our Live Stock & Custom Builds:</strong> Custom 9x3x2ft Monster Tanks, Blue Diamond Discus, Leopard Snake Skin Discus, Red Checkerboard, Red Super Rafflesia Discus, Super Reds, Red flora and Super Rafflesia, Koi, and Exotic Freshwater Fishes.
#         <strong>Filters & Air Pumps:</strong> Boyu U9900, Dophin AP1302, Hailea AC DC Charger, Eheim Classic 1500xl, Sunsun HW 304B, Dolphin C2400, Sobo WP-707C, Atman, and more.
#         <strong>Lighting & Heaters:</strong> Chihiros LED Light C361, Neo-Helios S3 Plus Nano, Solar Tropi Color Booster, Eheim Thermocontrol, RS Electrical 300W Heaters, and Dophin AH 1006.

import re

target_files = ["sidebar.js"]

# Let's find the exact block to replace using regex
for file in target_files:
    if file == os.path.basename(__file__):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Regex to match the three strong tags block
    pattern = r'<strong>All Products & Stock:</strong>.*?(?=</div>)'
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_seo_block.strip(), content, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected all products into {file}")

print("Done injecting full product SEO list globally!")
