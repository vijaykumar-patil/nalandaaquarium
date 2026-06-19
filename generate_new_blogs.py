import os
import urllib.parse
from datetime import datetime

blogs = [
    {
        "filename": "blog-aquascaping.html",
        "title": "The Ultimate Guide to Aquascaping for Beginners in Bangalore",
        "date": "January 10, 2026",
        "description": "A step-by-step guide on how to set up a beautiful planted tank (choosing substrate, driftwood, and low-tech plants).",
        "image": "media/Store/aquarium/4 feet moulded aquarium with stand.jpg",
        "content": """
            <p>Aquascaping is the beautiful art of arranging aquatic plants, rocks, cave work, or driftwood in an aesthetically pleasing manner within an aquarium—in effect, gardening under water. For beginners in Bangalore, setting up your first planted tank might seem daunting, but it doesn't have to be!</p>
            <h3>1. Choosing the Right Substrate</h3>
            <p>Your plants need nutrients to grow. A high-quality aquasoil is essential for heavy root feeders. If you're starting with easy plants like Anubias or Java Fern, you can even attach them directly to driftwood or rocks without needing special soil.</p>
            <h3>2. Hardscape (Wood and Rocks)</h3>
            <p>The "bones" of your aquascape are made of driftwood and rocks (like Dragon Stone or Seiryu Stone). Take your time playing with the arrangement before adding water. A classic beginner layout is the "Island" style, where all the hardscape is clustered in the middle.</p>
            <h3>3. Low-Tech Plants</h3>
            <p>If you don't want to invest in CO2 injection right away, start with low-tech plants. Anubias, Java Moss, Cryptocoryne, and Amazon Swords are incredibly hardy and do well in standard lighting conditions.</p>
        """,
        "cta_title": "Book Professional Aquascaping Services in Bangalore",
        "cta_desc": "Don't want to build it yourself? Book our Professional Aquascaping & Maintenance Service to have a breathtaking planted tank designed right in your living room!",
        "cta_wa": "Hi Nalanda Aquarium, I want to book an aquascaping service!",
        "cta_btn_text": "Book an Aquascaper",
        "cta_link": "index.html"
    },
    {
        "filename": "blog-monster-fishes.html",
        "title": "Top 5 Monster Fishes for Your Custom Aquarium",
        "date": "February 14, 2026",
        "description": "An exciting showcase of high-end, impressive fish like Asian Arowanas, Flowerhorns, and Stingrays.",
        "image": "media/Store/fish/koi.jpeg",
        "content": """
            <p>If you've recently upgraded to a massive custom aquarium (over 150 gallons), you might be looking to step away from tiny tetras and enter the world of "Monster Fish Keeping." Here are our top 5 favorites for serious hobbyists.</p>
            <h3>1. Asian Arowana (The Dragon Fish)</h3>
            <p>Considered a symbol of luck and prosperity, the Asian Arowana is the king of the aquarium. With their large metallic scales and barbels, they look like swimming dragons. They require pristine water and a very large footprint.</p>
            <h3>2. Flowerhorn Cichlid</h3>
            <p>Known for their vibrant colors and the massive "kok" (nuchal hump) on their heads, Flowerhorns are incredibly interactive fish. They will often follow your finger and "beg" for food. They are, however, very aggressive and usually need to be kept alone.</p>
            <h3>3. Freshwater Stingrays</h3>
            <p>Originating from the Amazon basin, freshwater stingrays are bottom-dwellers that require massive floor space. They are sensitive to water parameters but are absolutely mesmerizing to watch glide across fine sand.</p>
        """,
        "cta_title": "Buy Monster Fish & Custom Tanks in Bangalore",
        "cta_desc": "Looking to upgrade to a monster tank? Browse our custom aquariums online or contact us to place a special order for Arowanas, Flowerhorns, and massive aquarium setups!",
        "cta_wa": "Hi Nalanda Aquarium, I want to order a monster fish or custom tank!",
        "cta_btn_text": "Browse Custom Tanks",
        "cta_link": "store-aquariums.html"
    },
    {
        "filename": "blog-water-changes.html",
        "title": "How Often Should You Change Your Aquarium Water?",
        "date": "March 22, 2026",
        "description": "Answers one of the most Googled questions by beginners. Explains the nitrogen cycle, ammonia spikes, and why water changes are critical.",
        "image": "media/Store/filter/Sobo internal filter wp-1000f.jpg",
        "content": """
            <p>One of the most common questions we get at Nalanda Aquarium is: "How often do I actually need to change the water?" The answer depends on your tank size, filtration, and bioload, but here is a general guide.</p>
            <h3>The Golden Rule: 25% Every Week</h3>
            <p>For most standard community aquariums, changing 20% to 25% of the water once a week is perfect. This removes built-up nitrates (which your filter cannot remove) and replenishes essential minerals in the water.</p>
            <h3>Why Not 100%?</h3>
            <p>Never change all of your water at once! Doing so can shock your fish due to sudden shifts in temperature and pH. It can also disrupt the beneficial bacteria living in your substrate and filter.</p>
            <h3>The Role of Filtration</h3>
            <p>Your filter handles ammonia and nitrites, but nitrates will slowly build up over time. The only way to remove nitrates (unless you have a heavily planted tank) is through physical water changes.</p>
        """,
        "cta_title": "Professional Aquarium Cleaning in Bangalore",
        "cta_desc": "Tired of carrying heavy buckets? Let the experts handle it. Chat with us on WhatsApp to book our hassle-free Cleaning & Maintenance services!",
        "cta_wa": "Hi Nalanda Aquarium, I need someone to clean my aquarium!",
        "cta_btn_text": "Book Cleaning Service",
        "cta_link": "index.html"
    },
    {
        "filename": "blog-bangalore-water.html",
        "title": "Navigating Bangalore Tap Water: Keeping Your Fish Safe",
        "date": "April 05, 2026",
        "description": "Explains how to deal with hard water, chloramine, and seasonal fluctuations specific to the city's water supply.",
        "image": "media/Store/filter/Sponge filter small.jpeg",
        "content": """
            <p>Bangalore's water supply can vary wildly depending on whether you rely on Cauvery water or a local borewell. For aquarium hobbyists, this unpredictability means you must be vigilant about water treatment.</p>
            <h3>The Threat of Chlorine and Chloramine</h3>
            <p>Municipal water is heavily treated with chlorine and chloramine to make it safe for human consumption. However, these chemicals will instantly kill your fish and the beneficial bacteria in your filter. Always use a high-quality water conditioner before adding tap water to your tank.</p>
            <h3>Borewell Water and Hardness (GH/KH)</h3>
            <p>If you use borewell water in Bangalore, it is likely very hard with a high pH. While African Cichlids and Guppies love this water, sensitive fish like Discus or Neon Tetras may struggle. Consider mixing in RO (Reverse Osmosis) water to soften it.</p>
        """,
        "cta_title": "Buy Water Conditioners & Filters in Bangalore",
        "cta_desc": "Protect your fish from harsh tap water. Browse our top-rated filters and media, or talk to our experts for advice on water conditioners and RO setups.",
        "cta_wa": "Hi Nalanda Aquarium, I need help treating my aquarium water!",
        "cta_btn_text": "Shop Filters",
        "cta_link": "store-filters.html"
    },
    {
        "filename": "blog-heaters.html",
        "title": "Choosing the Right Heater for Tropical Fish",
        "date": "May 18, 2026",
        "description": "A practical guide explaining what wattage heater you need based on the size of your tank.",
        "image": "media/Store/heater/Sobo heater 300 watts.jpg",
        "content": """
            <p>During Bangalore's cooler winter months, the ambient temperature in your home can drop significantly. For tropical fish that require water temperatures between 24°C to 28°C, a reliable aquarium heater isn't a luxury—it's a necessity for survival.</p>
            <h3>What Wattage Do I Need?</h3>
            <p>A general rule of thumb is 1 to 1.5 watts per liter of water (or 3 to 5 watts per gallon). For example, a 100-liter tank will require a 100W or 150W heater. Using a heater that is too weak will cause it to run constantly and eventually burn out.</p>
            <h3>Placement Matters</h3>
            <p>Always place your heater near the filter intake or output. This ensures that the heated water is evenly distributed throughout the tank rather than creating localized "hot spots."</p>
        """,
        "cta_title": "Buy Aquarium Heaters in Bangalore",
        "cta_desc": "Don't let your tropical fish freeze this winter. Browse our reliable, shatter-proof aquarium heaters in-store and keep your fish healthy and active!",
        "cta_wa": "Hi Nalanda Aquarium, I need help choosing the right heater!",
        "cta_btn_text": "Shop Heaters",
        "cta_link": "store-heaters.html"
    },
    {
        "filename": "blog-sump-vs-canister.html",
        "title": "Sump Filters vs. Canister Filters: Which is Best?",
        "date": "June 10, 2026",
        "description": "A deep dive into high-end filtration. Explains the pros and cons of both systems for people with very large aquariums.",
        "image": "media/Store/filter/Sobo top filter wp 880f.jpg",
        "content": """
            <p>When you graduate to tanks larger than 75 gallons, standard hang-on-back and internal filters just won't cut it anymore. You are generally left with two high-end choices: Canister Filters or Sump Systems.</p>
            <h3>Canister Filters: Quiet and Compact</h3>
            <p>Canister filters sit underneath the tank and use hoses to pull water in and push it out. They are excellent because they run nearly silently, are very energy efficient, and don't require complicated plumbing. However, cleaning them can be a messy chore.</p>
            <h3>Sump Filters: Ultimate Customization</h3>
            <p>A sump is essentially a second, smaller aquarium placed beneath the main tank. Water overflows into the sump, passes through various filter media, and is pumped back up. Sumps increase the total water volume, hide heaters and skimmers, and offer unmatched biological filtration. They do, however, require plumbing and can be noisy if not tuned correctly.</p>
        """,
        "cta_title": "Shop High-End Aquarium Filters in Bangalore",
        "cta_desc": "Ready to upgrade your filtration? Browse our canister filters online or contact us to design and build a custom sump system for your monster tank.",
        "cta_wa": "Hi Nalanda Aquarium, I want to upgrade my filtration system to a canister or sump!",
        "cta_btn_text": "Browse Filters",
        "cta_link": "store-filters.html"
    }
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{description}">
  <title>{title} - Nalanda Aquarium</title>
  <link rel="stylesheet" href="style.css">
  <style>
    .blog-article {{
      max-width: 800px;
      margin: 0 auto;
      padding: 40px 20px;
      background: var(--color-white);
      border-radius: 12px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.05);
      margin-top: 40px;
      margin-bottom: 60px;
    }}
    .blog-article h2 {{
      font-size: 1.8em;
      color: var(--color-primary);
      margin-bottom: 10px;
      text-align: left;
    }}
    .blog-meta {{
      color: #666;
      font-size: 0.9em;
      margin-bottom: 30px;
      padding-bottom: 15px;
      border-bottom: 1px solid #eee;
    }}
    .blog-hero-img {{
      width: 100%;
      height: 400px;
      object-fit: contain;
      background: #f9f9f9;
      border-radius: 10px;
      margin-bottom: 30px;
    }}
    .blog-article p {{
      font-size: 1.1em;
      line-height: 1.8;
      color: var(--color-text);
      margin-bottom: 25px;
    }}
    .blog-article h3 {{
      color: var(--color-teal);
      margin-top: 40px;
      margin-bottom: 15px;
      font-size: 1.3em;
    }}
    .back-btn {{
      display: inline-block;
      margin-top: 20px;
      margin-bottom: 20px;
      color: var(--color-primary);
      text-decoration: none;
      font-weight: bold;
    }}
    .back-btn:hover {{
      color: var(--color-teal);
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <header>
    <div class="container header-flex">
      <a href="index.html">
        <img src="images/logo.png" alt="Nalanda Aquarium Logo" class="logo">
      </a>
      <div>
        <h1><a href="index.html" style="text-decoration: none; color: inherit;">Nalanda Aquarium</a></h1>
        <p class="tagline">Since 1962 — Crafting Long-Lasting, Durable Aquariums</p>
      </div>
    </div>
  </header>

    <main class="global-layout-grid">
    <!-- Left Sidebar for Store & Stock -->
    <aside id="left-sidebar" class="sticky-sidebar"></aside>

    <div class="main-column">
    <div class="container">
      <a href="blog.html" class="back-btn">&larr; Back to Blog</a>
      
      <article class="blog-article">
        <h2>{title}</h2>
        <div class="blog-meta">Published on {date} | By Nalanda Experts</div>
        
        <img src="{image}" alt="{title}" class="blog-hero-img">
        
        {content}
        
        <div style="margin-top: 50px; background: #eaf8f8; border-left: 5px solid var(--color-teal); padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
          <h3 style="margin-top: 0; color: var(--color-primary); font-size: 1.5em; margin-bottom: 15px;">{cta_title}</h3>
          <p style="font-size: 1.1em; color: var(--color-text); margin-bottom: 25px;">{cta_desc}</p>
          <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <a href="https://wa.me/916360782002?text={encoded_wa}" target="_blank" style="display: inline-flex; align-items: center; background: #25D366; color: white; padding: 12px 25px; border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 1.1em; transition: transform 0.2s ease; box-shadow: 0 4px 10px rgba(37,211,102,0.3);">
              <img src="images/WhatsApp.svg" style="width: 22px; margin-right: 10px;"> Chat on WhatsApp
            </a>
            <a href="{cta_link}" style="display: inline-flex; align-items: center; background: var(--color-primary); color: white; padding: 12px 25px; border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 1.1em; transition: transform 0.2s ease;">
              {cta_btn_text}
            </a>
          </div>
        </div>
      </article>
    </div>
    </div>

    <!-- Right Sidebar for Blogs -->
    <aside id="right-sidebar" class="sticky-sidebar"></aside>
  </main>

  <script src="sidebar.js"></script>
</body>
</html>"""

# 1. Generate the HTML files
for b in blogs:
    html = template.format(
        title=b["title"],
        description=b["description"],
        date=b["date"],
        image=b["image"],
        content=b["content"],
        cta_title=b["cta_title"],
        cta_desc=b["cta_desc"],
        encoded_wa=urllib.parse.quote(b["cta_wa"]),
        cta_btn_text=b["cta_btn_text"],
        cta_link=b["cta_link"]
    )
    with open(b["filename"], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {b['filename']}")

print("All blogs generated!")
