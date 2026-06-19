import glob
import re

seo_footer = """
<footer style="background: var(--color-bg); padding: 40px 20px; text-align: center; border-top: 1px solid rgba(255,255,255,0.05); margin-top: 50px;">
  <div class="container">
    <h4 style="color: var(--color-teal); margin-bottom: 15px;">Nalanda Aquarium - Bangalore's Premium Aquatic Store</h4>
    <p style="color: #666; font-size: 0.85em; line-height: 1.6; max-width: 1000px; margin: 0 auto;">
      Serving the aquascaping and monster fish keeping community with top-tier products. 
      <strong>Our Live Stock & Custom Builds:</strong> Custom 9x3x2ft Monster Tanks, Blue Diamond Discus, Leopard Snake Skin Discus, Red Checkerboard, Super Reds, Melons, Koi, and Exotic Freshwater Fishes.
      <strong>Filters & Air Pumps:</strong> Boyu U9900, Dophin AP1302, Hailea AC DC Charger, Eheim Classic 1500xl, Sunsun HW 304B, Dolphin C2400, Sebo WP-707C, Atman, and more.
      <strong>Lighting & Heaters:</strong> Chihiros LED Light C361, Neo-Helios S3 Plus Nano, Solar Tropi Color Booster, Eheim Thermocontrol, RS Electrical 300W Heaters, and Dophin AH 1006.
    </p>
    <p style="color: #555; font-size: 0.8em; margin-top: 15px;">&copy; 2026 Nalanda Aquarium. All Rights Reserved. Located in Bangalore, India.</p>
  </div>
</footer>
"""

# Update all standard HTML files
html_files = glob.glob("*.html")
for file in html_files:
    if file.startswith("store-"):
        continue # skip generated ones, we'll update generate_store.py
    
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    if "<footer" in html:
        print(f"Footer already exists in {file}")
        continue
        
    # Inject before the sidebar.js script tag or before </body>
    if '<script src="sidebar.js"></script>' in html:
        html = html.replace('<script src="sidebar.js"></script>', seo_footer + '\n  <script src="sidebar.js"></script>')
    else:
        html = html.replace('</body>', seo_footer + '\n</body>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Added SEO footer to {file}")

# Update generate_store.py
gen_file = "generate_store.py"
with open(gen_file, 'r', encoding='utf-8') as f:
    gen_content = f.read()

if "<footer" not in gen_content:
    if '<script src="sidebar.js"></script>' in gen_content:
        gen_content = gen_content.replace('<script src="sidebar.js"></script>', seo_footer + '\n  <script src="sidebar.js"></script>')
    else:
        gen_content = gen_content.replace('</body>', seo_footer + '\n</body>')
        
    with open(gen_file, 'w', encoding='utf-8') as f:
        f.write(gen_content)
    print(f"Added SEO footer to {gen_file}")

