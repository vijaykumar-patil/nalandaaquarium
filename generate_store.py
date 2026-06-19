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
  <link rel="stylesheet" href="style.css">
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

  <a href="https://wa.me/916360782002" class="floating-wa-button" target="_blank" rel="noopener noreferrer">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="30" height="30" fill="currentColor">
      <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/>
    </svg>
  </a>

  <footer>
    <div class="container">
    <div style="margin-bottom: 25px; padding-bottom: 25px; border-bottom: 1px solid rgba(255,255,255,0.05);">
      <h4 style="color: var(--color-teal); margin-bottom: 15px;">Nalanda Aquarium - Bangalore's Premium Aquatic Store</h4>
      <p style="color: #666; font-size: 0.85em; line-height: 1.6; max-width: 1000px; margin: 0 auto;">
        Serving the aquascaping and monster fish keeping community with top-tier products. 
        <strong>Our Live Stock & Custom Builds:</strong> Custom 9x3x2ft Monster Tanks, Blue Diamond Discus, Leopard Snake Skin Discus, Red Checkerboard, Super Reds, Melons, Koi, and Exotic Freshwater Fishes.
        <strong>Filters & Air Pumps:</strong> Boyu U9900, Dophin AP1302, Hailea AC DC Charger, Eheim Classic 1500xl, Sunsun HW 304B, Dolphin C2400, Sebo WP-707C, Atman, and more.
        <strong>Lighting & Heaters:</strong> Chihiros LED Light C361, Neo-Helios S3 Plus Nano, Solar Tropi Color Booster, Eheim Thermocontrol, RS Electrical 300W Heaters, and Dophin AH 1006.
      </p>
    </div>

      <p>&copy; 1962–<span id="year"></span> Nalanda Aquarium. All Rights Reserved.</p>
    </div>
  </footer>

  <script>
    document.getElementById("year").textContent = new Date().getFullYear();
  </script>
<script src="sidebar.js"></script>
</body>
</html>'''

for cat_id, cat_info in categories.items():
    title = cat_info['title']
    folder = cat_info['folder']
    
    html_content = html_template_start.format(title=title, id=cat_id)

    if os.path.exists(folder):
        files = os.listdir(folder)
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
            name_no_ext = os.path.splitext(file)[0]
            
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
            other_files = []
            for file in files:
                name_lower = file.lower()
                if 'koi' in name_lower or 'gold' in name_lower or 'oranda' in name_lower:
                    koi_files.append(file)
                elif 'discus' in name_lower or 'blue' in name_lower or 'melon' in name_lower or 'red' in name_lower or 'leopard' in name_lower or 'snake' in name_lower or 'checkerboard' in name_lower or 'turquoise' in name_lower:
                    discus_files.append(file)
                else:
                    other_files.append(file)
            
            html_content += discus_html
            for file in discus_files:
                html_content += generate_card(file, folder, cat_id)
                
            html_content += koi_html
            for file in koi_files:
                html_content += generate_card(file, folder, cat_id)
                
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

  <footer>
    <div class="container">
    <div style="margin-bottom: 25px; padding-bottom: 25px; border-bottom: 1px solid rgba(255,255,255,0.05);">
      <h4 style="color: var(--color-teal); margin-bottom: 15px;">Nalanda Aquarium - Bangalore's Premium Aquatic Store</h4>
      <p style="color: #666; font-size: 0.85em; line-height: 1.6; max-width: 1000px; margin: 0 auto;">
        Serving the aquascaping and monster fish keeping community with top-tier products. 
        <strong>Our Live Stock & Custom Builds:</strong> Custom 9x3x2ft Monster Tanks, Blue Diamond Discus, Leopard Snake Skin Discus, Red Checkerboard, Super Reds, Melons, Koi, and Exotic Freshwater Fishes.
        <strong>Filters & Air Pumps:</strong> Boyu U9900, Dophin AP1302, Hailea AC DC Charger, Eheim Classic 1500xl, Sunsun HW 304B, Dolphin C2400, Sebo WP-707C, Atman, and more.
        <strong>Lighting & Heaters:</strong> Chihiros LED Light C361, Neo-Helios S3 Plus Nano, Solar Tropi Color Booster, Eheim Thermocontrol, RS Electrical 300W Heaters, and Dophin AH 1006.
      </p>
    </div>

      <p>&copy; 1962–<span id="year"></span> Nalanda Aquarium. All Rights Reserved.</p>
    </div>
  </footer>

  <script>
    document.getElementById("year").textContent = new Date().getFullYear();
  </script>
<script src="sidebar.js"></script>
</body>
</html>'''
    
    with open(f"store-{cat_id}.html", "w", encoding="utf-8") as f:
        f.write(html_content)

print("Generated all store category pages successfully.")
