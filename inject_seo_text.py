import glob
import re

seo_content = """
    <div style="margin-bottom: 25px; padding-bottom: 25px; border-bottom: 1px solid rgba(255,255,255,0.05);">
      <h4 style="color: var(--color-teal); margin-bottom: 15px;">Nalanda Aquarium - Bangalore's Premium Aquatic Store</h4>
      <p style="color: #666; font-size: 0.85em; line-height: 1.6; max-width: 1000px; margin: 0 auto;">
        Serving the aquascaping and monster fish keeping community with top-tier products. 
                <details style="margin-top: 15px; cursor: pointer; text-align: left; background: rgba(0,0,0,0.02); padding: 10px; border-radius: 5px; border: 1px solid rgba(0,0,0,0.05);">
          <summary style="color: var(--color-teal); font-weight: bold; outline: none; list-style: none;">&#9662; View Our Complete Stock Index</summary>
          <div style="margin-top: 10px; font-size: 0.9em; line-height: 1.5;">
            <strong>All Products & Stock:</strong> 5 to 5.5 Inch Red Flora Super Rafflesia Discus, Ashkanani, Atman, Atman, Atman2, Blue rim red cover 4 Inch, Blue rim red cover discus, Blues discus, Boyu U9900, Butterfly Without Light Discus 4.5 Inch, Chihiros LED light C361, Chihiros LED light C361 1, Chihiros LED light C361 2, Custom 9x3x2ft , Dolphin 970F, Dolphin C1600, Dolphin C2400, Dolphin CF 11508, Dolphin CF 300, Dolphin F2000, Dolphin F800, Dophin AH 1006 200W, Dophin AP1302, Dophin AP1501, Eheim classic 150, Eheim classic 1500xl, Eheim classic 350, Eheim pickup200, Eheim thermocontrol, Eruption, Eruption2, External Filter AQ-901F-UV, External Filter AQ-901F-UV1, Filter, Fluval FX6, Frozen Blood Worms, Hailea AC DC Charger, Hailea1, Hailea2, High body turquoise, Hikari Cichlid Excel, Hikari Cichlid Gold, Hikari Economy, Hikari Food Sticks, Humpy Head, Humpy Head and Ever Red, Intan Bits Slowly Sinking Crumble, Intan Cichlid Pellets, Intan Faux Worms Slow Sinking Sticks, Intan Goldfish Pellets, Koi1, Koi2, Koi3, Koi4, Koi5, Koi6, Light, Melons, Neo-Helios S3 plus Nano, RS Electrical RS 300W, RSElectrical1, RSElectrical2, Red Checkerboard 2.5 - 3 Inch, Red Rafflesia & Jaguar Rafflesia 5 Inch, Red checkerboard, Red melon and blue diamond discus, Red melon and red butterflies, Show Grade Available for Sale - Golden Base or Golden Trimac, Shrimpe-e, Sobo, Sobo AL-180 COB, Sobo AL-280 COB, Sobo WP-707C, Sobo WP-707C 1, Solar Tropi Color Booster, Solar Tropi Color Booster all, Solar Tropi Color Booster1, Sunsun, Sunsun HW 304B, Sunsun JP-024F, Super Red Rafflesia 5 Inch - Available Last 2 Pcs, Super Reds Yellows, Super red melon, Taiyo Pro-Rich Arowans and large Carnivous, Taiyo Pro-Rich Red Parrot, TetraBits Complete, TetraMin Flakes, TetraMin Flakes 2, Tropical Treats Life Medium Fish, Tropical Treats Life Small Fish, Vayinato, custom 9x3x2ft, flowerhorn, optimun, optimun 2, optimun Super premium formula, white butterfly
          </div>
        </details>
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

