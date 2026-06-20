import glob
import re
import os

# 1. Read the footer HTML
with open('footer_snippet.txt', 'r', encoding='utf-8') as f:
    footer_html = f.read()

# Make sure footer HTML does not contain backticks that would break JS template literal
footer_html = footer_html.replace('`', '\\`')

# Ensure script logic for year is removed since we'll handle it in JS
footer_html = re.sub(r'<script>.*?</script>', '', footer_html, flags=re.DOTALL)

# 2. Append footer injection to sidebar.js
with open('sidebar.js', 'r', encoding='utf-8') as f:
    sidebar_js = f.read()

if 'insertAdjacentHTML' not in sidebar_js:
    injection_code = f"""
    const footerHTML = `{footer_html}`;
    document.body.insertAdjacentHTML('beforeend', footerHTML);
    const yearSpan = document.getElementById("year");
    if (yearSpan) {{
        yearSpan.textContent = new Date().getFullYear();
    }}
"""
    # Insert it right before the closing of DOMContentLoaded
    sidebar_js = sidebar_js.replace('});\n', injection_code + '});\n')
    with open('sidebar.js', 'w', encoding='utf-8') as f:
        f.write(sidebar_js)
    print("Added footer to sidebar.js")

# 3. Strip footer from all HTML files
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip footer and any trailing script tags associated with it
    new_content = re.sub(r'<footer.*?</footer>', '', content, flags=re.DOTALL)
    new_content = re.sub(r'<script>\s*document\.getElementById\("year"\)\.textContent = new Date\(\)\.getFullYear\(\);\s*</script>', '', new_content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Stripped footer from {file}")

# 4. Strip footer from generate_store.py
with open('generate_store.py', 'r', encoding='utf-8') as f:
    gen_store = f.read()

new_gen_store = re.sub(r'<footer.*?</footer>', '', gen_store, flags=re.DOTALL)
new_gen_store = re.sub(r'<script>\s*document\.getElementById\("year"\)\.textContent = new Date\(\)\.getFullYear\(\);\s*</script>', '', new_gen_store, flags=re.DOTALL)

if new_gen_store != gen_store:
    with open('generate_store.py', 'w', encoding='utf-8') as f:
        f.write(new_gen_store)
    print("Stripped footer from generate_store.py")

# 5. Modify inject_all_products_seo.py to only target sidebar.js
with open('inject_all_products_seo.py', 'r', encoding='utf-8') as f:
    inject_py = f.read()

# Change glob.glob("*.html") + glob.glob("*.py") to just ["sidebar.js"]
inject_py = re.sub(r'target_files = glob\.glob\("\*\.html"\) \+ glob\.glob\("\*\.py"\)', 'target_files = ["sidebar.js"]', inject_py)

with open('inject_all_products_seo.py', 'w', encoding='utf-8') as f:
    f.write(inject_py)
print("Updated inject_all_products_seo.py to target sidebar.js only")

