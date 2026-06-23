from bs4 import BeautifulSoup
import os, glob, urllib.parse

with open("store-fishes.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

existing_files = set()
for img in soup.find_all("img"):
    if img.has_attr("src") and "media/Store/fish" in img["src"]:
        existing_files.add(urllib.parse.unquote(img["src"]))
for source in soup.find_all("source"):
    if source.has_attr("src") and "media/Store/fish" in source["src"]:
        existing_files.add(urllib.parse.unquote(source["src"]))

base_dir = r"media/Store/fish"
all_files = glob.glob(os.path.join(base_dir, "**", "*.*"), recursive=True)

added = 0

for file_path in all_files:
    file_path = file_path.replace("\\", "/")
    if not file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4')): continue
    
    # Normalise paths for comparison
    if file_path not in existing_files:
        print(f"Adding new file: {file_path}")
        encoded_url = "/".join(urllib.parse.quote(p) for p in file_path.split("/"))
        filename = os.path.basename(file_path)
        name = os.path.splitext(filename)[0]
        
        if file_path.lower().endswith('.mp4'):
            card_html = f'<div class="product-card"><video controls style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px 8px 0 0; margin-bottom: 15px;"><source src="{encoded_url}" type="video/mp4">Your browser does not support the video tag.</video><h4>{name}</h4></div>'
        else:
            card_html = f'<div class="product-card"><img src="{encoded_url}" alt="{name}" style="width: 100%; height: 200px; object-fit: contain; padding: 15px; background: #fff; box-sizing: border-box; border-radius: 8px 8px 0 0; margin-bottom: 15px;"><h4>{name}</h4></div>'
            
        card_soup = BeautifulSoup(card_html, "html.parser").div
        
        cat_id = "others"
        if "arowana" in file_path.lower(): cat_id = "arowana"
        elif "discus" in file_path.lower(): cat_id = "discusfish"
        elif "flowerhorn" in file_path.lower(): cat_id = "flowerhorn"
        elif "koi" in file_path.lower(): cat_id = "koi&amp;goldfish"
        
        # BeautifulSoup automatically decodes &amp; in find, so let's check exact match
        if cat_id == "koi&amp;goldfish":
            cat_div = soup.find("div", id="koi&goldfish")
        else:
            cat_div = soup.find("div", id=cat_id)
            
        if cat_div:
            grid = cat_div.find("div", class_="product-grid")
            if grid:
                grid.append(card_soup)
                added += 1

if added > 0:
    with open("store-fishes.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"Successfully added {added} new fishes.")
else:
    print("No new fishes found.")
