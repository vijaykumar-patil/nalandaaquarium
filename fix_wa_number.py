import os
import glob

files = glob.glob("*.html") + glob.glob("*.js")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "919686774336" in content:
        content = content.replace("919686774336", "916360782002")
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated WA number in {file}")
