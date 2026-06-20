import glob
import re

replacements = {
    # Fix the mistake in the previous fix_blog_images.py script
    "media/Store/fish/red discus.jpeg": "media/blogs/Arowana.jpg",
    "media/Store/fish/Koi1.mp4": "media/Store/fish/koi/Koi1.mp4",
}

# The Sobo files exist in the file system, but maybe the HTML is using a different case or something.
# The python script reported:
# store-filters.html -> Missing: media/Store/filter/Sobo%20WP-707C%201.jpeg
# Wait, my check_images.py didn't decode the space properly or os.path.exists failed for some reason?
# Let's fix the known missing ones first.

html_files = glob.glob("*.html")
html_files.append("generate_store.py")

for file in html_files:
    if file.startswith("store-"):
        pass # we can update store generated files directly or just generate_store.py
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    for old_img, new_img in replacements.items():
        content = content.replace(old_img, new_img)
        # Also replace URL encoded versions
        content = content.replace(old_img.replace(" ", "%20"), new_img.replace(" ", "%20"))
        
    if original != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed images in {file}")

print("Done fixing remaining images!")
