import glob

old_text = "Red Checkerboard, Red Super Rafflesia Discus, Super Reds, Melons"
new_text = "Red Checkerboard, Red Super Rafflesia Discus, Super Reds, Melons"

files = glob.glob("*.html") + glob.glob("*.py")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added exact phrase 'Red Super Rafflesia Discus' to {file}")

print("Done updating SEO text globally!")
