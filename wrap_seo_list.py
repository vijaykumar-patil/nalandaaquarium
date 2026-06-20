import glob
import re

html_details_start = """        <details style="margin-top: 15px; cursor: pointer; text-align: left; background: rgba(0,0,0,0.02); padding: 10px; border-radius: 5px; border: 1px solid rgba(0,0,0,0.05);">
          <summary style="color: var(--color-teal); font-weight: bold; outline: none; list-style: none;">&#9662; View Our Complete Stock Index</summary>
          <div style="margin-top: 10px; font-size: 0.9em; line-height: 1.5;">
            <strong>All Products & Stock:</strong>"""

html_details_end = """          </div>
        </details>"""

files = glob.glob("*.html") + glob.glob("*.py")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "<strong>All Products & Stock:</strong>" in content and "<details" not in content:
        # Replace the <strong> part with details start
        content = content.replace("<strong>All Products & Stock:</strong>", html_details_start)
        
        # In the files, the last item is "white butterfly". The string looks like "..., white butterfly\n      </p>"
        # We need to insert html_details_end right after "white butterfly"
        content = re.sub(r'(white butterfly)(\s*</p>)', r'\1' + '\n' + html_details_end + r'\2', content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Wrapped SEO list in {file}")

print("Done wrapping SEO lists in a toggle!")
