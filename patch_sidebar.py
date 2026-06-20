import re

with open('footer_snippet.txt', 'r', encoding='utf-8') as f:
    footer_html = f.read()

# Make sure footer HTML does not contain backticks
footer_html = footer_html.replace('`', '\\`')

# Remove inline scripts
footer_html = re.sub(r'<script>.*?</script>', '', footer_html, flags=re.DOTALL)

with open('sidebar.js', 'r', encoding='utf-8') as f:
    sidebar_js = f.read()

injection_code = f"""
    const footerHTML = `{footer_html}`;
    document.body.insertAdjacentHTML('beforeend', footerHTML);
    const yearSpan = document.getElementById("year");
    if (yearSpan) {{
        yearSpan.textContent = new Date().getFullYear();
    }}
"""

parts = sidebar_js.rsplit('});', 1)
sidebar_js = parts[0] + injection_code + '});' + parts[1]

with open('sidebar.js', 'w', encoding='utf-8') as f:
    f.write(sidebar_js)
print('Successfully patched sidebar.js')
