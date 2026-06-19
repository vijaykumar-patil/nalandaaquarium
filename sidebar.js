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

      <div class="sidebar-title" style="margin-top: 30px;">Our Services</div>
      <a href="https://wa.me/916360782002?text=Hi%20Nalanda%20Aquarium%2C%20I%20am%20interested%20in%20your%20Cleaning%20%26%20Maintenance%20services." target="_blank" class="sidebar-item" style="border-left: 4px solid #25D366; background: rgba(37, 211, 102, 0.1);">
        <span class="sidebar-item-tag" style="color: #25D366;">Professional</span>
        <h5 style="color: #4afffe;">Cleaning & Maintenance</h5>
        <p style="font-size: 0.85em; color: white; margin-top: 5px; margin-bottom: 0; line-height: 1.4;">Expert tank cleaning, deep water changes, filter maintenance, and aquascaping services in Bangalore.</p>
      </a>
    `;

    const rightSidebarHTML = `
      <div class="sidebar-title">Our Latest Blogs</div>
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
});
