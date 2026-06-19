import re

blogs = [
    {
        "filename": "blog-solar-tanning.html",
        "title": "The Magic of Solar Tanning Lights",
        "date": "June 19, 2026",
        "description": "Have you ever wondered how professional breeders get those impossibly vibrant reds, deep blues, and brilliant golds on their Arowanas, Flowerhorns, and Discus? The secret isn't just genetics or diet—it's specialized lighting.",
        "image": "media/Store/lights/Solar Tropi Color Booster.jpeg"
    },
    {
        "filename": "blog-sump-vs-canister.html",
        "title": "Sump Filters vs. Canister Filters: Which is Best?",
        "date": "June 10, 2026",
        "description": "A deep dive into high-end filtration. Explains the pros and cons of both systems for people with very large aquariums.",
        "image": "media/Store/filter/Sobo top filter wp 880f.jpg"
    },
    {
        "filename": "blog-heaters.html",
        "title": "Choosing the Right Heater for Tropical Fish",
        "date": "May 18, 2026",
        "description": "A practical guide explaining what wattage heater you need based on the size of your tank to prevent ich and stress.",
        "image": "media/Store/heater/Sobo heater 300 watts.jpg"
    },
    {
        "filename": "blog-bangalore-water.html",
        "title": "Navigating Bangalore Tap Water: Keeping Your Fish Safe",
        "date": "April 05, 2026",
        "description": "Explains how to deal with hard water, chloramine, and seasonal fluctuations specific to the city's water supply.",
        "image": "media/Store/filter/Sponge filter small.jpeg"
    },
    {
        "filename": "blog-water-changes.html",
        "title": "How Often Should You Change Your Aquarium Water?",
        "date": "March 22, 2026",
        "description": "Answers one of the most Googled questions by beginners. Explains the nitrogen cycle, ammonia spikes, and why water changes are critical.",
        "image": "media/Store/filter/Sobo internal filter wp-1000f.jpg"
    },
    {
        "filename": "blog-monster-fishes.html",
        "title": "Top 5 Monster Fishes for Your Custom Aquarium",
        "date": "February 14, 2026",
        "description": "An exciting showcase of high-end, impressive fish like Asian Arowanas, Flowerhorns, and Stingrays.",
        "image": "media/Store/fish/koi.jpeg"
    },
    {
        "filename": "blog-aquascaping.html",
        "title": "The Ultimate Guide to Aquascaping for Beginners",
        "date": "January 10, 2026",
        "description": "A step-by-step guide on how to set up a beautiful planted tank (choosing substrate, driftwood, and low-tech plants).",
        "image": "media/Store/aquarium/4 feet moulded aquarium with stand.jpg"
    },
    {
        "filename": "blog-filtration.html",
        "title": "The Importance of Proper Filtration",
        "date": "December 10, 2025",
        "description": "Never underestimate the power of a good filter. It is the life support system of your aquarium.",
        "image": "media/Store/filter/Sobo top filter wp 880f.jpg"
    },
    {
        "filename": "blog-freshwater-fish.html",
        "title": "Top 5 Freshwater Fish for Beginners",
        "date": "November 02, 2025",
        "description": "Starting your first aquarium? Here are the hardiest and most vibrant fish to ensure your success.",
        "image": "media/Store/fish/gold.jpeg"
    },
    {
        "filename": "blog-custom-aquarium.html",
        "title": "How to Set Up Your First Custom Aquarium",
        "date": "October 15, 2025",
        "description": "A step-by-step guide on planning, sizing, and cycling your very first custom tank build.",
        "image": "media/Store/aquarium/1.5 feet tank.jpg"
    }
]

# 1. Update sidebar.js rightSidebarHTML
sidebar_items = ""
for b in blogs:
    sidebar_items += f"""
      <a href="{b['filename']}" class="sidebar-item">
        <span class="sidebar-item-tag">{b['date']}</span>
        <h5>{b['title']}</h5>
      </a>"""

with open('sidebar.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace the rightSidebarHTML block
pattern = r'(const rightSidebarHTML = `\n      <div class="sidebar-title">Our Latest Blogs</div>)(.*?)(    `;)'
replacement = r'\1' + sidebar_items + r'\n\3'
new_js = re.sub(pattern, replacement, js_content, flags=re.DOTALL)

with open('sidebar.js', 'w', encoding='utf-8') as f:
    f.write(new_js)

# 2. Update blog.html feed
blog_feed = ""
for b in blogs:
    blog_feed += f"""
          <article class="blog-post">
            <img src="{b['image']}" alt="{b['title']}">
            <div class="blog-content">
              <h3>{b['title']}</h3>
              <span class="date">{b['date']}</span>
              <p>{b['description']}</p>
              <a href="{b['filename']}" class="read-more">Read Full Article &rarr;</a>
            </div>
          </article>"""

with open('blog.html', 'r', encoding='utf-8') as f:
    blog_html = f.read()

feed_pattern = r'(<div class="blog-list">)(.*?)(        </div>\n      </div>\n    </section>)'
feed_replacement = r'\1\n' + blog_feed + r'\n\3'
new_blog_html = re.sub(feed_pattern, feed_replacement, blog_html, flags=re.DOTALL)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(new_blog_html)

print("Updated sidebar.js and blog.html with all 10 blogs!")
