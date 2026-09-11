import os
import zipfile
from PIL import Image

logo_path = 'images/logo.png'
if not os.path.exists(logo_path):
    raise FileNotFoundError(f"Logo not found at {logo_path}")

logo = Image.open(logo_path)
bbox = logo.getbbox()
crop = logo.crop(bbox)

def make_icon(size):
    if size <= 32:
        padding_ratio = 0.0
    elif size <= 64:
        padding_ratio = 0.02
    else:
        padding_ratio = 0.04
        
    target_dim = int(size * (1.0 - 2 * padding_ratio))
    w, h = crop.size
    scale = target_dim / max(w, h)
    new_w = max(1, int(round(w * scale)))
    new_h = max(1, int(round(h * scale)))
    resized = crop.resize((new_w, new_h), Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    offset = ((size - new_w) // 2, (size - new_h) // 2)
    canvas.paste(resized, offset, resized)
    return canvas

os.makedirs('favicon_io', exist_ok=True)

# Generate individual icons
icon16 = make_icon(16)
icon32 = make_icon(32)
icon48 = make_icon(48)
icon180 = make_icon(180)
icon192 = make_icon(192)
icon512 = make_icon(512)

icon16.save('favicon_io/favicon-16x16.png', format='PNG')
icon32.save('favicon_io/favicon-32x32.png', format='PNG')
icon180.save('favicon_io/apple-touch-icon.png', format='PNG')
icon192.save('favicon_io/android-chrome-192x192.png', format='PNG')
icon512.save('favicon_io/android-chrome-512x512.png', format='PNG')

# Generate multi-size ICO containing 48x48, 32x32, 16x16
icon48.save('favicon_io/favicon.ico', format='ICO', append_images=[icon32, icon16])
icon48.save('favicon.ico', format='ICO', append_images=[icon32, icon16])

# Update site.webmanifest
manifest_content = '''{
    "name": "Nalanda Aquarium",
    "short_name": "Nalanda Aquarium",
    "icons": [
        {
            "src": "/favicon_io/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/favicon_io/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "theme_color": "#ffffff",
    "background_color": "#ffffff",
    "display": "standalone"
}
'''
with open('favicon_io/site.webmanifest', 'w', encoding='utf-8') as f:
    f.write(manifest_content.strip())

# Update favicon_io.zip
with zipfile.ZipFile('favicon_io.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for filename in [
        'apple-touch-icon.png',
        'favicon-32x32.png',
        'favicon-16x16.png',
        'favicon.ico',
        'site.webmanifest',
        'android-chrome-192x192.png',
        'android-chrome-512x512.png'
    ]:
        z.write(os.path.join('favicon_io', filename), arcname=filename)

# Update HTML files
import glob, re
target_block = """  <link rel="apple-touch-icon" sizes="180x180" href="favicon_io/apple-touch-icon.png?v=2">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon_io/favicon-32x32.png?v=2">
  <link rel="icon" type="image/png" sizes="16x16" href="favicon_io/favicon-16x16.png?v=2">
  <link rel="shortcut icon" href="favicon_io/favicon.ico?v=2">
  <link rel="manifest" href="favicon_io/site.webmanifest">"""

html_files = [f for f in glob.glob('*.html') if not f.startswith('google')]
updated_count = 0
for f in sorted(html_files):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'favicon_io' in c:
        pattern = r'[ \t]*<link[^>]*href=["\']favicon_io/[^>]*>[\s\S]*?<link[^>]*href=["\']favicon_io/site\.webmanifest["\'][^>]*>'
        m = re.search(pattern, c)
        if m:
            c = c[:m.start()] + target_block + c[m.end():]
            updated_count += 1
    else:
        if '</head>' in c:
            c = c.replace('</head>', target_block + '\n</head>')
            updated_count += 1
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)

print(f"Favicons generated and {updated_count} HTML files updated!")

