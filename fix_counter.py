import glob
import re

html_files = glob.glob("*.html")
html_files.append("generate_store.py")

counter_html = '<p id="visit-counter" style="text-align: center; color: #555; font-size: 0.9em; margin-top: 10px;">Site visits: <span id="count">Loading...</span></p>'

for file in html_files:
    if file.startswith("store-"):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 2. Inject counter HTML if missing
    if "id=\"visit-counter\"" not in content:
        # Let's insert just before </footer>
        if "</footer>" in content:
            # We want to place it inside the container ideally, but placing before </footer> is fine.
            # Actually, most have <p style="color: #555...>&copy; 2026...</p>
            # We can insert after the copy block or before </div>\n  </footer>
            
            # Let's try to find the container div close
            content = content.replace("</footer>", counter_html + "\n  </footer>")
            print(f"Injected into {file}")
        else:
            print(f"Could not find </footer> in {file}")

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Counter HTML added to missing files.")
