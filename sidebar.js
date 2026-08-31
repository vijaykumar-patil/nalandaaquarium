document.addEventListener("DOMContentLoaded", function() {
    const leftSidebarHTML = `
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
      
      <a href="store-food.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Fish Food</h5>
      </a>
      <a href="store-stones.html" class="sidebar-item">
        <span class="sidebar-item-tag">Category</span>
        <h5>Stones & Gravel</h5>
      </a>

      <div class="sidebar-title" style="margin-top: 30px;">Our Services</div>
      <a href="https://wa.me/916360782002?text=Hi%20Nalanda%20Aquarium%2C%20I%20am%20interested%20in%20your%20Cleaning%20%26%20Maintenance%20services." target="_blank" class="sidebar-item" style="border-left: 4px solid #25D366; background: rgba(37, 211, 102, 0.1);">
        <span class="sidebar-item-tag" style="color: #25D366;">Professional</span>
        <h5 style="color: #4afffe;">Cleaning & Maintenance</h5>
        <p style="color: white; margin-top: 5px; margin-bottom: 0; line-height: 1.4;">Expert tank cleaning, deep water changes, filter maintenance, and aquascaping services in Bangalore.</p>
      </a>
    `;

    const rightSidebarHTML = `
      <div class="sidebar-title">Our Latest Blogs</div>
      <a href="blog-gravel.html" class="sidebar-item">
        <span class="sidebar-item-tag">June 22, 2026</span>
        <h5>The Essential Guide to Aquarium Substrate</h5>
      </a>
      <a href="blog-solar-tanning.html" class="sidebar-item">
        <span class="sidebar-item-tag">June 19, 2026</span>
        <h5>The Magic of Solar Tanning Lights</h5>
      </a>
      <a href="blog-sump-vs-canister.html" class="sidebar-item">
        <span class="sidebar-item-tag">June 10, 2026</span>
        <h5>Sump Filters vs. Canister Filters: Which is Best?</h5>
      </a>
      <a href="blog-heaters.html" class="sidebar-item">
        <span class="sidebar-item-tag">May 18, 2026</span>
        <h5>Choosing the Right Heater for Tropical Fish</h5>
      </a>
      <a href="blog-bangalore-water.html" class="sidebar-item">
        <span class="sidebar-item-tag">April 05, 2026</span>
        <h5>Navigating Bangalore Tap Water: Keeping Your Fish Safe</h5>
      </a>
      <a href="blog-water-changes.html" class="sidebar-item">
        <span class="sidebar-item-tag">March 22, 2026</span>
        <h5>How Often Should You Change Your Aquarium Water?</h5>
      </a>
      <a href="blog-monster-fishes.html" class="sidebar-item">
        <span class="sidebar-item-tag">February 14, 2026</span>
        <h5>Top 5 Monster Fishes for Your Custom Aquarium</h5>
      </a>
      <a href="blog-aquascaping.html" class="sidebar-item">
        <span class="sidebar-item-tag">January 10, 2026</span>
        <h5>The Ultimate Guide to Aquascaping for Beginners</h5>
      </a>
      <a href="blog-filtration.html" class="sidebar-item">
        <span class="sidebar-item-tag">December 10, 2025</span>
        <h5>The Importance of Proper Filtration</h5>
      </a>
      <a href="blog-freshwater-fish.html" class="sidebar-item">
        <span class="sidebar-item-tag">November 02, 2025</span>
        <h5>Top 5 Freshwater Fish for Beginners</h5>
      </a>
      <a href="blog-custom-aquarium.html" class="sidebar-item">
        <span class="sidebar-item-tag">October 15, 2025</span>
        <h5>How to Set Up Your First Custom Aquarium</h5>
      </a>
    `;

    const leftSidebar = document.getElementById("left-sidebar");
    const rightSidebar = document.getElementById("right-sidebar");

    if (leftSidebar) leftSidebar.innerHTML = leftSidebarHTML;
    if (rightSidebar) rightSidebar.innerHTML = rightSidebarHTML;

    // Dynamic WhatsApp floating button text
    const waButtons = document.querySelectorAll('.whatsapp-float, .floating-wa-button');
    waButtons.forEach(btn => {
        let pageTitle = document.title.split('-')[0].trim();
        let message = `Hi Nalanda Aquarium, I am looking at the "${pageTitle}" page and need some help.`;
        btn.href = `https://wa.me/916360782002?text=${encodeURIComponent(message)}`;
    });
    // === Visit Counter ===
    const counterReadOnlyUrl = 'https://abacus.jasoncameron.dev/get/nalandaaquarium/visits';
    const counterUpUrl = 'https://abacus.jasoncameron.dev/hit/nalandaaquarium/visits';
    
    let urlToFetch = counterReadOnlyUrl;
    try {
      if (!sessionStorage.getItem('counted_visit')) {
        urlToFetch = counterUpUrl;
        sessionStorage.setItem('counted_visit', 'true');
      }
    } catch (e) {
      // Ignore sessionStorage errors (e.g., when third-party cookies are blocked)
      console.warn("sessionStorage access denied", e);
    }

    const footerHTML = `<footer>
    <div class="container">
    <div style="margin-bottom: 25px; padding-bottom: 25px; border-bottom: 1px solid rgba(255,255,255,0.05);">
      <h4 style="color: var(--color-teal); margin-bottom: 15px;">Nalanda Aquarium - Bangalore's Premium Aquatic Store</h4>
      <p style="color: #666; font-size: 0.85em; line-height: 1.6; max-width: 1000px; margin: 0 auto;">
        Serving the aquascaping and monster fish keeping community with top-tier products. 
                <details style="margin-top: 15px; cursor: pointer; text-align: left; background: rgba(0,0,0,0.02); padding: 10px; border-radius: 5px; border: 1px solid rgba(0,0,0,0.05);">
          <summary style="color: var(--color-teal); font-weight: bold; outline: none; list-style: none;">&#9662; View Our Complete Stock Index</summary>
          <div style="margin-top: 10px; font-size: 0.9em; line-height: 1.5;">
            <details style="margin-top: 15px; cursor: pointer; text-align: left; background: rgba(0,0,0,0.02); padding: 10px; border-radius: 5px; border: 1px solid rgba(0,0,0,0.05);">
          <summary style="color: var(--color-teal); font-weight: bold; outline: none; list-style: none;">&#9662; View Our Complete Stock Index</summary>
          <div style="margin-top: 10px; font-size: 0.9em; line-height: 1.5;">
            <strong>All Products & Stock:</strong> Albino Arowana, Albino Geophagus Red Head Tapajos and Oddball Clown Loaches, Albino Platinum Discus, Albino Platinum Discus Display, Arowana Malaysian Golden, Ashkanani, Atman, Atman, Atman2, Blue Diamond Discus, Blue rim red cover 4 Inch, Blue rim red cover discus, Blues discus, Boyu U9900, Brilliant Blue Turquoise Discus, Butterfly Without Light Discus 4.5 Inch, Chihiros LED light C361, Chihiros LED light C361 1, Chihiros LED light C361 2, Cobalt Blue Diamond Discus School, Custom 9x3x2ft , Discus 3, Discus 4, Dolphin 970F, Dolphin C1600, Dolphin C2400, Dolphin CF 11508, Dolphin CF 300, Dolphin F2000, Dolphin F800, Dophin AH 1006 200W, Dophin AP1302, Dophin AP1501, Dream Mahseer Tank, Eheim classic 150, Eheim classic 1500xl, Eheim classic 350, Eheim pickup200, Eheim thermocontrol, Eruption, Eruption2, Exotic Discus Variety Tank, Exotic Mahseer Fish, External Filter AQ-901F-UV, External Filter AQ-901F-UV1, Filter, Flowerhorn (2), Flowerhorn 3, Flowerhorn 4, Fluval FX6, Frozen Blood Worms, Hailea AC DC Charger, Hailea1, Hailea2, High back Golden Arowana, High body turquoise, Hikari Cichlid Excel, Hikari Cichlid Gold, Hikari Economy, Hikari Food Sticks, Humpy Head, Humpy Head and Ever Red, Intan Bits Slowly Sinking Crumble, Intan Cichlid Pellets, Intan Faux Worms Slow Sinking Sticks, Intan Goldfish Pellets, King Kamfa 10.7, Koi1, Koi2, Koi3, Koi4, Koi5, Koi6, Leopard Snakeskin Discus, Light, Neo-Helios S3 plus Nano, Pearl Arowana, RS Electrical RS 300W, RSElectrical1, RSElectrical2, Rare Strain Discus, Red Checkerboard 2.5 - 3 Inch, Red Checkerboard Discus Pair, Red Flora Super Rafflesia Discus 5 to 5.5 Inch , Red Marlboro Discus, Red Melon and Checkerboard Discus School, Red Melon and Yellow Melon Discus, Red Rafflesia & Jaguar Rafflesia 5 Inch, Red TCA, Scorpion Blue Snakeskin, Red Raising Sun Snakeskin, White Pigeon Blood , Snakeskin White, Leopard, Albino golden , Golden, Blue diamond and checkerboard pigeon blood discus fishes, Red Turquoise Discus Pair, Red checkerboard, Red flora and Super Rafflesia, Red melon and blue diamond discus, Red melon and red butterflies, Red tail Golden Arowana, San Merah Red Cover Discus, Show Grade Available for Sale - Golden Base or Golden Trimac, Shrimpe-e, Silver Arowana, Sobo, Sobo AL-180 COB, Sobo AL-280 COB, Sobo WP-707C, Sobo WP-707C 1, Solar Tropi Color Booster, Solar Tropi Color Booster all, Solar Tropi Color Booster1, Solid Red Cover Discus, Stone1, Stone2, Stone3, Stone4, Stone5, Stone6, Stone7, Stone8, Stone9, Sunsun, Sunsun HW 304B, Sunsun JP-024F, Super Red Arowana, Super Red Rafflesia 5 Inch - Available Last 2 Pcs, Super Reds Yellows, Super red melon, Taiyo Pro-Rich Arowans and large Carnivous, Taiyo Pro-Rich Red Parrot, TetraBits Complete, TetraMin Flakes, TetraMin Flakes 2, Tropical Treats Life Medium Fish, Tropical Treats Life Small Fish, Turquoise Snakeskin Discus, VIP Kamfa, VIP Kamfa, VIP Kamfa 2, Vayinato, Yellow Face Red Melon Discus, Yellow Melon Discus, custom 9x3x2ft, flowerhorn, gravel1, gravel10, gravel11, gravel12, gravel13, gravel14, gravel15, gravel16, gravel17, gravel18, gravel19, gravel2, gravel20, gravel21, gravel22, gravel23, gravel24, gravel25, gravel26, gravel27, gravel28, gravel29, gravel3, gravel4, gravel5, gravel6, gravel7, gravel8, gravel9, marbles, marbles10, marbles11, marbles12, marbles13, marbles14, marbles15, marbles16, marbles2, marbles3, marbles4, marbles5, marbles6, marbles7, marbles8, marbles9, optimun, optimun 2, optimun Super premium formula, pebbles1, pebbles10, pebbles11, pebbles12, pebbles13, pebbles14, pebbles15, pebbles16, pebbles17, pebbles18, pebbles19, pebbles2, pebbles20, pebbles21, pebbles22, pebbles23, pebbles24, pebbles25, pebbles26, pebbles27, pebbles28, pebbles29, pebbles3, pebbles30, pebbles31, pebbles32, pebbles33, pebbles34, pebbles4, pebbles5, pebbles6, pebbles7, pebbles8, pebbles9, white butterfly</div>
        </details>
      </p>
    </div>

      
    <div style="margin-top: 15px; font-size: 0.9em; text-align: center;">
      <a href="index.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Home</a> | 
      <a href="store.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Full Store</a> | 
      <a href="store-fishes.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Fishes</a> | 
      <a href="store-aquariums.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Aquariums</a> | 
      <a href="blog.html" style="color: var(--color-teal); text-decoration: none; margin: 0 10px;">Blog</a>
    </div>

      <p>&copy; 1962–<span id="year"></span> Nalanda Aquarium. All Rights Reserved.</p>
      <p id="visit-counter">Site visits: <span id="count">Loading...</span></p>
    </div>
  </footer>`;
    document.body.insertAdjacentHTML('beforeend', footerHTML);
    const yearSpan = document.getElementById("year");
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }
    
    fetch(urlToFetch)
      .then(res => {
        if (!res.ok) throw new Error('Network response was not ok');
        return res.json();
      })
      .then(data => {
        const countSpan = document.getElementById('count');
        if (countSpan) {
            if (data && data.value !== undefined) {
                const totalCount = data.value + 1179;
                countSpan.innerText = totalCount.toLocaleString();
                try {
                    localStorage.setItem('last_known_visit_count', totalCount);
                } catch(e) {}
            } else {
                throw new Error("Invalid data");
            }
        }
      })
      .catch(err => {
        console.error("Counter error:", err);
        const countSpan = document.getElementById('count');
        if (countSpan) {
            let lastKnown = null;
            try {
                lastKnown = localStorage.getItem('last_known_visit_count');
            } catch(e) {}
            
            if (lastKnown) {
                countSpan.innerText = parseInt(lastKnown).toLocaleString();
            } else {
                countSpan.innerText = '1,179';
            }
        }
      });
});
