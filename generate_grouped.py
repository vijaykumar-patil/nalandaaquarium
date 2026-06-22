import os
import urllib.parse
import glob
import re

template_stones = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stones, Pebbles & Gravel - Nalanda Aquarium Store</title>
  <link rel="stylesheet" href="style.css?v=2">
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-TPH1JMNB3K"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-TPH1JMNB3K');
  </script>
</head>
<body>
  <header>
    <div class="container header-flex">
      <a href="index.html">
        <img src="images/logo.png" alt="Nalanda Aquarium Logo" class="logo">
      </a>
      <div>
        <h1><a href="index.html" style="text-decoration: none; color: inherit;">Nalanda Aquarium</a></h1>
        <p class="tagline">Since 1962 — Crafting Long-Lasting, Durable Aquariums</p>
      </div>
    </div>
  </header>

  <main class="global-layout-grid">
    <!-- Left Sidebar for Store & Stock -->
    <aside id="left-sidebar" class="sticky-sidebar"></aside>

    <div class="main-column">
      <section>
        <h2>Stones, Pebbles, Marbles & Gravel</h2>
        <p style="text-align: center; margin-bottom: 40px; font-size: 1.1em;">Browse our selection below. To purchase, click <img src="images/WhatsApp.svg" alt="WhatsApp" style="width: 22px; vertical-align: middle; margin: 0 4px; border-radius: 50%;"> <strong>WhatsApp</strong> in the corner or call 📞 <strong>+91 9686774336</strong>.</p>
        
{content}
      </section>
    </div>

    <!-- Right Sidebar for Blogs -->
    <aside id="right-sidebar" class="sticky-sidebar"></aside>
  </main>

  <!-- WhatsApp Floating Button -->
  <a href="https://wa.me/916360782002?text=Hi%20Nalanda%20Aquarium%2C%20I%20am%20interested%20in%20your%20services." class="whatsapp-float" target="_blank" aria-label="Chat on WhatsApp">
    <img src="images/WhatsApp.svg" alt="WhatsApp" class="whatsapp-icon">
  </a>

<script src="sidebar.js?v=2"></script>
</body>
</html>
"""

template_fishes = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Live Fishes - Nalanda Aquarium Store</title>
  <link rel="stylesheet" href="style.css?v=2">
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-TPH1JMNB3K"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-TPH1JMNB3K');
  </script>
</head>
<body>
  <header>
    <div class="container header-flex">
      <a href="index.html">
        <img src="images/logo.png" alt="Nalanda Aquarium Logo" class="logo">
      </a>
      <div>
        <h1><a href="index.html" style="text-decoration: none; color: inherit;">Nalanda Aquarium</a></h1>
        <p class="tagline">Since 1962 — Crafting Long-Lasting, Durable Aquariums</p>
      </div>
    </div>
  </header>

  <main class="global-layout-grid">
    <!-- Left Sidebar for Store & Stock -->
    <aside id="left-sidebar" class="sticky-sidebar"></aside>

    <div class="main-column">
      <section>
        <h2>Live Fishes</h2>
        <p style="text-align: center; margin-bottom: 40px; font-size: 1.1em;">Browse our Live Fishes below. To purchase, click <img src="images/WhatsApp.svg" alt="WhatsApp" style="width: 22px; vertical-align: middle; margin: 0 4px; border-radius: 50%;"> <strong>WhatsApp</strong> in the corner or call 📞 <strong>+91 9686774336</strong>.</p>
        
{content}
      </section>
    </div>

    <!-- Right Sidebar for Blogs -->
    <aside id="right-sidebar" class="sticky-sidebar"></aside>
  </main>

  <!-- WhatsApp Floating Button -->
  <a href="https://wa.me/916360782002?text=Hi%20Nalanda%20Aquarium%2C%20I%20am%20interested%20in%20your%20services." class="whatsapp-float" target="_blank" aria-label="Chat on WhatsApp">
    <img src="images/WhatsApp.svg" alt="WhatsApp" class="whatsapp-icon">
  </a>

<script src="sidebar.js?v=2"></script>
</body>
</html>
"""

def make_stones():
    base_dir = r"C:\Users\vijay\git\nalandaaquarium\media\Store\Stones and Gravel"
    
    all_images = glob.glob(os.path.join(base_dir, "**", "*.*"), recursive=True)
    all_images = [img for img in all_images if img.lower().endswith(('.jpeg', '.jpg', '.png'))]
    all_images.sort()
    
    categories = {"Stones": [], "Pebbles": [], "Marbles": [], "Gravel": []}
    
    for img_path in all_images:
        filename = os.path.basename(img_path)
        lower_name = filename.lower()
        if "marble" in lower_name:
            categories["Marbles"].append(img_path)
        elif "gravel" in lower_name:
            categories["Gravel"].append(img_path)
        elif "pebble" in lower_name:
            categories["Pebbles"].append(img_path)
        else:
            categories["Stones"].append(img_path)
            
    content = ""
    for cat_name, items in categories.items():
        if not items: continue
        content += f'        <h3 style="margin-top: 30px;">{cat_name}</h3>\n'
        content += f'        <div class="product-category" id="{cat_name.lower()}">\n'
        content += f'          <div class="product-grid">\n'
        
        for img_path in items:
            rel_path = os.path.relpath(img_path, r"C:\Users\vijay\git\nalandaaquarium")
            rel_url = rel_path.replace("\\", "/")
            parts = rel_url.split('/')
            encoded_parts = [urllib.parse.quote(p) for p in parts]
            encoded_url = "/".join(encoded_parts)
            
            filename = os.path.basename(img_path)
            name_without_ext = os.path.splitext(filename)[0]
            display_name = re.sub(r'([a-zA-Z]+)(\d+)', r'\1 \2', name_without_ext).capitalize()
            
            content += f'''            <div class="product-card">
              <img src="{encoded_url}" alt="{display_name}" style="width: 100%; height: 200px; object-fit: contain; padding: 15px; background: #fff; box-sizing: border-box; border-radius: 8px 8px 0 0; margin-bottom: 15px;">
              <h4>{display_name}</h4>
            </div>\n'''
            
        content += f'          </div>\n        </div>\n'
        
    with open(r"C:\Users\vijay\git\nalandaaquarium\store-stones.html", "w", encoding="utf-8") as f:
        f.write(template_stones.replace("{content}", content))
        
def make_fishes():
    base_dir = r"C:\Users\vijay\git\nalandaaquarium\media\Store\fish"
    
    subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    content = ""
    for folder in subdirs:
        cat_name = folder.replace("fish", "Fish").title()
        if cat_name == "Flowerhorn": cat_name = "Flowerhorn"
        
        items = glob.glob(os.path.join(base_dir, folder, "**", "*.*"), recursive=True)
        items = [item for item in items if item.lower().endswith(('.jpeg', '.jpg', '.png', '.mp4'))]
        items.sort()
        
        if not items: continue
        
        content += f'        <h3 style="margin-top: 30px;">{cat_name}</h3>\n'
        content += f'        <div class="product-category" id="{folder.replace(" ", "")}">\n'
        content += f'          <div class="product-grid">\n'
        
        for img_path in items:
            rel_path = os.path.relpath(img_path, r"C:\Users\vijay\git\nalandaaquarium")
            rel_url = rel_path.replace("\\", "/")
            parts = rel_url.split('/')
            encoded_parts = [urllib.parse.quote(p) for p in parts]
            encoded_url = "/".join(encoded_parts)
            
            filename = os.path.basename(img_path)
            name_without_ext = os.path.splitext(filename)[0]
            display_name = name_without_ext
            
            ext = os.path.splitext(filename)[1].lower()
            if ext == '.mp4':
                content += f'''            <div class="product-card">
              <video controls style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px 8px 0 0; margin-bottom: 15px;">
                <source src="{encoded_url}" type="video/mp4">
                Your browser does not support the video tag.
              </video>
              <h4>{display_name}</h4>
            </div>\n'''
            else:
                content += f'''            <div class="product-card">
              <img src="{encoded_url}" alt="{display_name}" style="width: 100%; height: 200px; object-fit: contain; padding: 15px; background: #fff; box-sizing: border-box; border-radius: 8px 8px 0 0; margin-bottom: 15px;">
              <h4>{display_name}</h4>
            </div>\n'''
            
        content += f'          </div>\n        </div>\n'
        
    with open(r"C:\Users\vijay\git\nalandaaquarium\store-fishes.html", "w", encoding="utf-8") as f:
        f.write(template_fishes.replace("{content}", content))

if __name__ == '__main__':
    make_stones()
    make_fishes()
    print("Done generating grouped pages.")
