import os
import re

replacements = {
    "media/Store/aquarium/4 feet moulded aquarium with stand.jpg": "media/Store/aquarium/Custom 9x3x2ft .png",
    "media/Store/fish/koi.jpeg": "media/Store/fish/red discus.jpeg",
    "media/Store/filter/Sobo internal filter wp-1000f.jpg": "media/Store/filter/Eheim pickup200.jpeg",
    "media/Store/filter/Sponge filter small.jpeg": "media/Store/filter/Filter.jpeg",
    "media/Store/heater/Sobo heater 300 watts.jpg": "media/Store/heater/RS Electrical RS 300W.jpeg",
    "media/Store/filter/Sobo top filter wp 880f.jpg": "media/Store/filter/Dolphin C2400.jpeg",
    "media/Store/fish/gold.jpeg": "media/Store/fish/red discus.jpeg",
    "media/Store/aquarium/1.5 feet tank.jpg": "media/Store/aquarium/Custom 9x3x2ft .png",
    # Just in case:
    "media/Store/aquarium/4%20feet%20moulded%20aquarium%20with%20stand.jpg": "media/Store/aquarium/Custom%209x3x2ft%20.png"
}

import glob
files = glob.glob("*.html")

for file in files:
    if file.startswith("store-"): continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    for old_img, new_img in replacements.items():
        content = content.replace(old_img, new_img)
        
    if original != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed images in {file}")

print("Done fixing images!")
