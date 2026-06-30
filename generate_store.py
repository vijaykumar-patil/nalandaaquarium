import os
import urllib.parse

# Define categories and their corresponding folders
categories = {
    'fishes': {'title': 'Live Fishes', 'folder': 'media/Store/fish'},
    'aquariums': {'title': 'Custom Aquariums', 'folder': 'media/Store/aquarium'},
    'lights': {'title': 'Lighting Systems', 'folder': 'media/Store/lights'},
    'filters': {'title': 'Filters & Media', 'folder': 'media/Store/filter'},
    'heaters': {'title': 'Heaters & Chillers', 'folder': 'media/Store/heater'},
    'airpumps': {'title': 'Air Pumps & Accessories', 'folder': 'media/Store/airpumps'},
    'food': {'title': 'Fish Food & Nutrition', 'folder': 'media/Store/food'}
}

html_template_start = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Nalanda Aquarium Store</title>
  <link rel="stylesheet" href="style.css?v=2">
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-TPH1JMNB3K"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
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
        <h2>{title}</h2>
        <p style="text-align: center; margin-bottom: 40px; font-size: 1.1em;">Browse our {title} below. To purchase, click <img src="images/WhatsApp.svg" alt="WhatsApp" style="width: 22px; vertical-align: middle; margin: 0 4px; border-radius: 50%;"> <strong>WhatsApp</strong> in the corner or call 📞 <strong>+91 9686774336</strong>.</p>
        
        <div class="product-category" id="{id}">
          <div class="product-grid">
'''

html_template_end = '''          </div>
        </div>
      </section>
    </div>

    <!-- Right Sidebar for Blogs -->
    <aside id="right-sidebar" class="sticky-sidebar"></aside>
  </main>

  

  

  
<script src="sidebar.js?v=3"></script>
</body>
</html>'''

for cat_id, cat_info in categories.items():
    title = cat_info['title']
    folder = cat_info['folder']
    
    html_content = html_template_start.format(title=title, id=cat_id)

    if os.path.exists(folder):
        all_files = []
        for root, _, filenames in os.walk(folder):
            for filename in filenames:
                rel_dir = os.path.relpath(root, folder)
                if rel_dir == ".":
                    all_files.append(filename)
                else:
                    all_files.append(os.path.join(rel_dir, filename).replace("\\", "/"))
        files = all_files
        files.sort()
        
        # Inject Discus and Koi as the first items in the grid for Fishes
        if cat_id == 'fishes' and os.path.exists("stock.txt"):
            with open("stock.txt", "r") as sf:
                lines = sf.readlines()
            
            discus_html = '<div class="product-card" style="padding: 20px; text-align: left; background: #caf0f8; border: 2px solid var(--color-primary);"><h4 style="color: var(--color-primary); margin-top: 0; border-bottom: 1px solid rgba(0,51,102,0.2); padding-bottom: 8px;">Discus In Stock</h4><ul style="list-style: none; padding: 0; margin-bottom: 0; font-size: 0.9em; margin-top: 10px;">'
            koi_html = '<div style="grid-column: 1 / -1; height: 0;"></div><div class="product-card" style="padding: 20px; text-align: left; background: #caf0f8; border: 2px solid var(--color-primary);"><h4 style="color: var(--color-primary); margin-top: 0; border-bottom: 1px solid rgba(0,51,102,0.2); padding-bottom: 8px;">Koi & Goldfish In Stock</h4><ul style="list-style: none; padding: 0; margin-bottom: 0; font-size: 0.9em; margin-top: 10px;">'
            
            capture_discus = False
            capture_koi = False
            
            for line in lines:
                line = line.strip()
                if not line: continue
                
                if line.startswith("Discus :"):
                    capture_discus = True
                    capture_koi = False
                    continue
                elif line.startswith("Gold fish / Koi carp:") or line.startswith("Thai imported Gold:"):
                    capture_discus = False
                    capture_koi = True
                    continue
                elif line.endswith(":") or line.endswith(" :"):
                    capture_discus = False
                    capture_koi = False
                    continue
                
                if capture_discus:
                    if " - " in line:
                        p = line.split(" - ")
                        discus_html += f'<li style="margin-bottom: 6px; padding-left: 20px; text-indent: -20px;"><span style="color: var(--color-primary); margin-right: 8px; font-weight: bold;">✔</span> <strong>{p[0]}</strong> - {p[1]}</li>'
                    else:
                        discus_html += f'<li style="margin-bottom: 6px; padding-left: 20px; text-indent: -20px;"><span style="color: var(--color-primary); margin-right: 8px; font-weight: bold;">✔</span> <strong>{line}</strong></li>'
                elif capture_koi:
                    if " - " in line:
                        p = line.split(" - ")
                        koi_html += f'<li style="margin-bottom: 6px; padding-left: 20px; text-indent: -20px;"><span style="color: var(--color-primary); margin-right: 8px; font-weight: bold;">✔</span> <strong>{p[0]}</strong> - {p[1]}</li>'
                    else:
                        koi_html += f'<li style="margin-bottom: 6px; padding-left: 20px; text-indent: -20px;"><span style="color: var(--color-primary); margin-right: 8px; font-weight: bold;">✔</span> <strong>{line}</strong></li>'
                        
            discus_html += '</ul></div>\n'
            koi_html += '</ul></div>\n'
            
        import re
        def generate_card(file, folder, cat_id):
            ext = os.path.splitext(file)[1].lower()
            name_no_ext = os.path.splitext(os.path.basename(file))[0]
            
            # Clean up trailing numbers used for uniqueness
            display_title = re.sub(r'[\s\-]*\d+$', '', name_no_ext).strip()
            
            encoded_file = urllib.parse.quote(file)
            filepath = f"{folder}/{encoded_file}"
            
            # hardware vs livestock styles
            is_hardware = cat_id in ['lights', 'filters', 'heaters', 'airpumps', 'food']
            img_style = "width: 100%; height: 200px; object-fit: contain; padding: 15px; background: #fff; box-sizing: border-box; border-radius: 8px 8px 0 0; margin-bottom: 15px;" if is_hardware else "width: 100%; height: 200px; object-fit: cover; border-radius: 8px 8px 0 0; margin-bottom: 15px;"

            # Special case for the monster tank
            if cat_id == 'aquariums' and '9x3x2ft' in file.lower() and ext == '.mp4':
                poster = ""
                if os.path.exists(f"{folder}/Custom 9x3x2ft .png"):
                    poster = f'poster="{folder}/Custom%209x3x2ft%20.png"'
                
                return f'''            <div style="grid-column: 1 / -1; background: linear-gradient(135deg, var(--color-primary), var(--color-teal)); border-radius: 12px; padding: 20px; color: white; display: flex; flex-wrap: wrap; gap: 30px; box-shadow: 0 8px 25px rgba(0,0,0,0.2); position: relative; overflow: hidden; margin-bottom: 20px;">
              <div style="position: absolute; top: 15px; left: -35px; background: #ff4757; color: white; padding: 5px 40px; transform: rotate(-45deg); font-weight: bold; font-size: 0.9em; z-index: 10; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">GREAT DEAL</div>
              <div style="flex: 1; min-width: 300px; position: relative; z-index: 1;">
                <video controls {poster} style="width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                  <source src="{filepath}" type="video/mp4">
                  Your browser does not support the video tag.
                </video>
              </div>
              <div style="flex: 1; min-width: 300px; display: flex; flex-direction: column; justify-content: center; z-index: 1;">
                <h3 style="color: #4afffe; font-size: 1.8em; margin-bottom: 15px; margin-top: 0; line-height: 1.2;">9ft x 3ft x 2ft Monster Showpiece Tank</h3>
                <p style="font-size: 1.1em; line-height: 1.6; margin-bottom: 20px;"><strong>THE ULTIMATE SHOWPIECE AQUARIUM IS FOR SALE!</strong> Ever wanted a true monster tank? This custom-built beast is the perfect centerpiece for a dream reef, massive monster fish setup, or a breathtaking planted aquascape.</p>
                <p style="font-size: 1.1em; line-height: 1.6; margin-bottom: 25px;">Custom tanks this size rarely hit the market. Don't miss out! DM us right now for price, glass specs, and details! SHARE this video with a fellow fishkeeper who needs a major upgrade!</p>
                <a href="https://wa.me/916360782002?text=I'm%20interested%20in%20the%209x3x2ft%20Monster%20Tank!" target="_blank" style="display: inline-block; background: #25D366; color: white; padding: 12px 25px; border-radius: 50px; text-decoration: none; font-weight: bold; font-size: 1.1em; align-self: flex-start; transition: transform 0.2s ease; box-shadow: 0 4px 10px rgba(37,211,102,0.4);">
                  <img src="images/WhatsApp.svg" style="width: 20px; vertical-align: middle; margin-right: 8px;"> DM for Price
                </a>
              </div>
            </div>\n'''
            elif cat_id == 'aquariums' and '9x3x2ft' in file.lower() and ext in ['.png', '.jpg', '.jpeg']:
                return ""

            if ext in ['.mp4', '.mov']:
                return f'''            <div class="product-card">
              <video controls style="{img_style}">
                <source src="{filepath}" type="video/mp4">
                Your browser does not support the video tag.
              </video>
              <h4>{display_title}</h4>
            </div>\n'''
            elif ext in ['.jpg', '.jpeg', '.png', '.webp']:
                return f'''            <div class="product-card">
              <img src="{filepath}" alt="{name_no_ext}" style="{img_style}">
              <h4>{display_title}</h4>
            </div>\n'''
            return ""

        if cat_id == 'fishes':
            discus_files = []
            koi_files = []
            flowerhorn_files = []
            other_files = []
            
            for file in files:
                dir_lower = os.path.dirname(file).lower()
                name_lower = file.lower()
                
                # Prioritize directory matching if it exists
                if 'koi' in dir_lower or 'gold' in dir_lower:
                    koi_files.append(file)
                elif 'discus' in dir_lower:
                    discus_files.append(file)
                elif 'flowerhorn' in dir_lower:
                    flowerhorn_files.append(file)
                else:
                    # Fallback to name matching just in case
                    if 'koi' in name_lower or 'gold' in name_lower or 'oranda' in name_lower:
                        koi_files.append(file)
                    elif 'discus' in name_lower or 'blue' in name_lower or 'melon' in name_lower or 'red' in name_lower or 'leopard' in name_lower or 'snake' in name_lower or 'checkerboard' in name_lower or 'turquoise' in name_lower:
                        discus_files.append(file)
                    elif 'flowerhorn' in name_lower or 'trimac' in name_lower:
                        flowerhorn_files.append(file)
                    else:
                        other_files.append(file)
            
            html_content += discus_html
            for file in discus_files:
                html_content += generate_card(file, folder, cat_id)
                
            html_content += koi_html
            for file in koi_files:
                html_content += generate_card(file, folder, cat_id)
                
            if flowerhorn_files:
                html_content += '<div style="grid-column: 1 / -1; height: 0;"></div><div class="product-card" style="padding: 20px; text-align: left; background: #caf0f8; border: 2px solid var(--color-primary);"><h4 style="color: var(--color-primary); margin-top: 0; border-bottom: 1px solid rgba(0,51,102,0.2); padding-bottom: 8px;">Flowerhorns In Stock</h4><p style="font-size: 0.9em; margin-bottom: 0;">Check out our premium grade imported Flowerhorns!</p></div>\n'
                for file in flowerhorn_files:
                    html_content += generate_card(file, folder, cat_id)
                    
            if other_files:
                html_content += '<div style="grid-column: 1 / -1; height: 0;"></div><div class="product-card" style="padding: 20px; text-align: left; background: #caf0f8; border: 2px solid var(--color-primary);"><h4 style="color: var(--color-primary); margin-top: 0; border-bottom: 1px solid rgba(0,51,102,0.2); padding-bottom: 8px;">Other Exotic Fishes</h4><p style="font-size: 0.9em; margin-bottom: 0;">We carry a wide variety of exotic and community fishes.</p></div>\n'
                for file in other_files:
                    html_content += generate_card(file, folder, cat_id)
                
        else:
            for file in files:
                html_content += generate_card(file, folder, cat_id)

    # Close product grid before adding the stock list
    html_content += '''          </div>\n        </div>\n'''

    # Add the mega stock list at the very bottom
    if cat_id == 'fishes':
        stock_html = ""
        if os.path.exists("stock.txt"):
            with open("stock.txt", "r") as sf:
                lines = sf.readlines()
            
            stock_html += '''
        <div style="margin-top: 60px; padding-top: 40px; border-top: 2px solid rgba(0,51,102,0.1);">
          <h3 style="color: var(--color-primary); margin-bottom: 30px; font-size: 2em; text-align: center;">🔥 Full Live Stock Availability</h3>
          <div class="service-grid">
'''
            current_category = ""
            skip_current = False
            for line in lines:
                line = line.strip()
                if not line or line.lower().startswith("available stock"):
                    continue
                
                if line.endswith(":") or line.endswith(" :"):
                    cat_name = line.replace(":", "").strip()
                    
                    if cat_name in ["Discus", "Gold fish / Koi carp", "Thai imported Gold"]:
                        skip_current = True
                        continue
                    else:
                        skip_current = False
                        
                    if current_category:
                        stock_html += "</ul></article>\n"
                    current_category = cat_name
                    stock_html += f'<article class="service" style="text-align: left;">'
                    stock_html += f'<h4 style="color: var(--color-primary); margin-bottom: 15px; font-size: 1.2em; border-bottom: 1px solid rgba(0,51,102,0.2); padding-bottom: 8px;">{cat_name}</h4>\n'
                    stock_html += '<ul style="list-style: none; padding-left: 10px; margin-bottom: 0; color: var(--color-text); font-size: 0.95em;">\n'
                else:
                    if current_category and not skip_current:
                        if " - " in line:
                            parts = line.split(" - ")
                            item_name = parts[0]
                            size = parts[1]
                            stock_html += f'<li style="margin-bottom: 8px; padding-left: 20px; text-indent: -20px;"><span style="color: var(--color-primary); margin-right: 8px; font-weight: bold;">✔</span> <strong>{item_name}</strong> &mdash; {size}</li>\n'
                        else:
                            stock_html += f'<li style="margin-bottom: 8px; padding-left: 20px; text-indent: -20px;"><span style="color: var(--color-primary); margin-right: 8px; font-weight: bold;">✔</span> <strong>{line}</strong></li>\n'
            
            if current_category:
                stock_html += "</ul></article>\n"
            
            stock_html += '''
          </div>
        </div>
'''
        html_content += stock_html

    # We only append the closing tags since we already closed the grid above
    html_content += '''      </section>
    </div>

    <!-- Right Sidebar for Blogs -->
    <aside id="right-sidebar" class="sticky-sidebar"></aside>
  </main>

  <!-- WhatsApp Floating Button -->
  <a href="https://wa.me/916360782002?text=Hi%20Nalanda%20Aquarium%2C%20I%20am%20interested%20in%20your%20services." class="whatsapp-float" target="_blank" aria-label="Chat on WhatsApp">
    <img src="images/WhatsApp.svg" alt="WhatsApp" class="whatsapp-icon">
  </a>

  

  
<script src="sidebar.js?v=3"></script>
</body>
</html>'''
    
    with open(f"store-{cat_id}.html", "w", encoding="utf-8") as f:
        f.write(html_content)

print("Generated all store category pages successfully.")
