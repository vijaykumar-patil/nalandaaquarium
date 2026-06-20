import glob

ga_snippet = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-TPH1JMNB3K"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-TPH1JMNB3K');
  </script>
"""

html_files = glob.glob("*.html")
html_files.append("generate_store.py")

for file in html_files:
    if file.startswith("store-"):
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "G-TPH1JMNB3K" in content:
        print(f"GA already in {file}")
        continue
        
    if "</head>" in content:
        content = content.replace("</head>", ga_snippet + "</head>")
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added GA to {file}")
    else:
        print(f"Warning: </head> not found in {file}")

print("GA script injection complete.")
