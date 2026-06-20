import glob
import re

seo_content = """
    <div style="margin-bottom: 25px; padding-bottom: 25px; border-bottom: 1px solid rgba(255,255,255,0.05);">
      <h4 style="color: var(--color-teal); margin-bottom: 15px;">Nalanda Aquarium - Bangalore's Premium Aquatic Store</h4>
      <p style="color: #666; font-size: 0.85em; line-height: 1.6; max-width: 1000px; margin: 0 auto;">
        Serving the aquascaping and monster fish keeping community with top-tier products. 
        <strong>Our Live Stock & Custom Builds:</strong> Custom 9x3x2ft Monster Tanks, Blue Diamond Discus, Leopard Snake Skin Discus, Red Checkerboard, Super Reds, Melons, Koi, and Exotic Freshwater Fishes.
        <strong>Filters & Air Pumps:</strong> Boyu U9900, Dophin AP1302, Hailea AC DC Charger, Eheim Classic 1500xl, Sunsun HW 304B, Dolphin C2400, Sobo WP-707C, Atman, and more.
        <strong>Lighting & Heaters:</strong> Chihiros LED Light C361, Neo-Helios S3 Plus Nano, Solar Tropi Color Booster, Eheim Thermocontrol, RS Electrical 300W Heaters, and Dophin AH 1006.
      </p>
    </div>
"""

files = glob.glob("*.html")
files.append("generate_store.py")

for file in files:
    if file.startswith("store-"):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "Nalanda Aquarium - Bangalore's Premium Aquatic Store" in content:
        print(f"Already injected in {file}")
        continue
        
    if "<footer>\n    <div class=\"container\">" in content:
        # Existing footer found! Inject inside the container.
        content = content.replace('<footer>\n    <div class="container">', '<footer>\n    <div class="container">' + seo_content)
    elif "<footer " in content and "class=\"container\"" in content:
        # The new footer I just generated
        # Actually it's better to just leave the ones I just generated since they look good, but they don't have the counter.
        # But wait, my previous script injected a completely new footer into the new blogs! 
        # I should just replace the <p style="color: #555;... with the counter for the newly generated ones if needed, or leave it.
        pass
    else:
        # It's an old file with a different footer format, or no footer.
        pass
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {file}")

