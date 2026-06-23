from bs4 import BeautifulSoup

with open("store-fishes.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

for category in soup.find_all("div", class_="product-category"):
    grid = category.find("div", class_="product-grid")
    if grid:
        cards = grid.find_all("div", class_="product-card", recursive=False)
        if not cards: continue
        
        # Sort cards by the text in the <h4> tag
        # Use natural sorting if there are numbers? Or just alphabetical.
        import re
        def sort_key(card):
            h4 = card.find("h4")
            title = h4.text.strip().lower() if h4 else ""
            # Natural sort extraction
            def convert(text): return int(text) if text.isdigit() else text
            return [convert(c) for c in re.split('([0-9]+)', title)]
            
        sorted_cards = sorted(cards, key=sort_key)
        
        # Clear the grid
        grid.clear()
        
        # Re-append the sorted cards with newlines for formatting
        grid.append("\n")
        for card in sorted_cards:
            grid.append(card)
            grid.append("\n")

with open("store-fishes.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Sorted fishes in each category.")
