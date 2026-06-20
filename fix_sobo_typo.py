import glob
import os

files = glob.glob("*.html") + glob.glob("*.py") + glob.glob("*.txt")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "Sobo" in content or "sobo" in content:
        content = content.replace("Sobo", "Sobo")
        content = content.replace("sobo", "sobo")
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated Sobo typo in {file}")

print("Done fixing Sobo to Sobo globally!")
