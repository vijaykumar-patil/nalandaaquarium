with open('store.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <main> with the grid layout and left sidebar
content = content.replace('<main>\n    <section>', '<main class="global-layout-grid">\n    <!-- Left Sidebar for Store & Stock -->\n    <aside id="left-sidebar" class="sticky-sidebar"></aside>\n\n    <div class="main-column">\n      <section>')

# Replace closing </section>\n  </main> with closing div, right sidebar, and main
content = content.replace('      </div>\n    </section>\n  </main>', '      </div>\n    </section>\n    </div>\n\n    <!-- Right Sidebar for Blogs -->\n    <aside id="right-sidebar" class="sticky-sidebar"></aside>\n  </main>')

with open('store.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated store.html layout.")
