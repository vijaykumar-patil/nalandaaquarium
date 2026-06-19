import os
import glob

left_sidebar = '''  <main class="global-layout-grid">
    <!-- Left Sidebar for Store & Stock -->
    <aside class="sticky-sidebar">
      <div class="sidebar-title">Store & Stock</div>
      
      <a href="store-fishes.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Fishes</h5>
      </a>
      <a href="store-aquariums.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Aquariums</h5>
      </a>
      <a href="store-lights.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Lights</h5>
      </a>
      <a href="store-filters.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Filters</h5>
      </a>
      <a href="store-heaters.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Heaters</h5>
      </a>
      <a href="store-airpumps.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Air Pumps</h5>
      </a>
    </aside>

    <div class="main-column">'''

right_sidebar = '''    </div>

    <!-- Right Sidebar for Blogs -->
    <aside class="sticky-sidebar">
      <div class="sidebar-title">Our Latest Blogs</div>
      <a href="blog-solar-tanning.html" class="sidebar-item">
        <span class="sidebar-item-tag">June 19, 2026</span>
        <h5>The Magic of Solar Tanning Lights</h5>
      </a>
      <a href="blog-custom-aquarium.html" class="sidebar-item">
        <span class="sidebar-item-tag">October 15, 2025</span>
        <h5>How to Set Up Your First Custom Aquarium</h5>
      </a>
      <a href="blog-freshwater-fish.html" class="sidebar-item">
        <span class="sidebar-item-tag">November 02, 2025</span>
        <h5>Top 5 Freshwater Fish for Beginners</h5>
      </a>
      <a href="blog-filtration.html" class="sidebar-item">
        <span class="sidebar-item-tag">December 10, 2025</span>
        <h5>The Importance of Proper Filtration</h5>
      </a>
    </aside>
  </main>'''

blog_files = [
    'blog.html',
    'blog-solar-tanning.html',
    'blog-custom-aquarium.html',
    'blog-freshwater-fish.html',
    'blog-filtration.html'
]

for file in blog_files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'class="global-layout-grid"' in content:
        print(f"Already updated {file}")
        continue
        
    # Replace <main> with the left sidebar + <div class="main-column">
    content = content.replace('<main>', left_sidebar)
    
    # Replace </main> with the closing div + right sidebar + </main>
    content = content.replace('</main>', right_sidebar)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {file}")
