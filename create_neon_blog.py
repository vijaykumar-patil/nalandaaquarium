import os

with open('blog-solar-tanning.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace meta description
content = content.replace('Learn how solar tanning lights enhance fish coloration, simulating natural sunlight for Arowanas, Discus, and Flowerhorns.', 'Neon Tetras are the crown jewels of any planted aquarium. Learn about their care, diet, and ideal tank conditions in our comprehensive guide.')

# Replace title
content = content.replace('The Magic of Solar Tanning Lights - Nalanda Aquarium', 'A Guide to Neon Tetras: The Jewels of the Planted Tank - Nalanda Aquarium')

# Replace the H2 title inside the body
content = content.replace('The Magic of Solar Tanning Lights', 'A Guide to Neon Tetras: The Jewels of the Planted Tank')

# Replace date
content = content.replace('June 19, 2026', 'June 19, 2026')

# Replace image
content = content.replace('media/Store/lights/Solar%20Tropi%20Color%20Booster.jpeg', 'media/blogs/neon%20Tetra.jpg')
content = content.replace('alt="Solar Tanning Lights"', 'alt="Neon Tetra Flock"')

# Replace article body
old_body_start = '<p>Have you ever wondered how professional breeders get those impossibly vibrant reds'
old_body_end = 'Upgrade your lighting with us today!</p>'

import re
pattern = re.compile(f"{re.escape(old_body_start)}.*?{re.escape(old_body_end)}", re.DOTALL)

new_body = """<p>When you picture a breathtaking, lushly planted aquascape, chances are you immediately envision a shimmering school of tiny blue and red fish darting through the greenery. The <strong>Neon Tetra</strong> (<em>Paracheirodon innesi</em>) is arguably the most recognizable and beloved freshwater fish in the aquarium hobby. Originating from the blackwater streams of the Amazon basin, these tiny jewels bring a unique energy and contrast to any tank.</p>

<h3>Why Choose Neon Tetras?</h3>
<p>Their popularity isn't just about their brilliant iridescent blue stripes and vibrant red tails. Neon tetras are incredibly peaceful, making them the ultimate community fish. They thrive in schools, and watching a group of 10 or more tetras swim in unison is a mesmerizing experience. Furthermore, their small size (growing only to about 1.5 inches) means they don't require massive setups, making them perfect for both beginners and advanced aquascapers alike.</p>

<h3>Ideal Tank Conditions</h3>
<p>To keep your Neon Tetras healthy and vibrant, it is essential to replicate their natural Amazonian habitat:</p>
<ul>
  <li><strong>Water Parameters:</strong> They prefer soft, slightly acidic water. A pH between 6.0 and 7.0 is ideal, though they can adapt to slightly higher ranges. The temperature should be maintained between 22°C and 26°C (72°F - 78°F).</li>
  <li><strong>Tank Size:</strong> While they are small, they are active swimmers. A minimum of 10 gallons is required, but a 20-gallon "long" tank is highly recommended to give them ample horizontal swimming space.</li>
  <li><strong>Environment:</strong> They truly shine in heavily planted tanks with dark substrates. The dark background makes their neon colors pop, while the plants provide essential hiding spots that reduce their stress.</li>
  <li><strong>Lighting:</strong> Dim or diffused lighting is best. Floating plants like Frogbit or Red Root Floaters are excellent for creating the dappled light effect of the Amazon jungle canopy.</li>
</ul>

<h3>Diet and Nutrition</h3>
<p>Neon Tetras are omnivores and are generally not picky eaters. However, because they have very small mouths, their food must be appropriately sized. A high-quality micro-pellet or crushed flake food should form the staple of their diet. To ensure they reach their maximum color potential, supplement their diet with live or frozen foods like Daphnia, baby brine shrimp, or bloodworms.</p>

<h3>Choosing Tank Mates</h3>
<p>Because they are peaceful and small, they must be housed with fish of similar temperaments. Excellent companions include:</p>
<ul>
  <li>Corydoras Catfish</li>
  <li>Otocinclus</li>
  <li>Other small Tetras (like Ember or Rummy-nose)</li>
  <li>Harlequin Rasboras</li>
  <li>Dwarf Gouramis</li>
</ul>
<p><em>Warning:</em> Avoid housing them with large, aggressive, or predatory fish like Angelfish, larger Cichlids, or Oscars. To a large fish, a Neon Tetra is simply an expensive snack.</p>

<h3>Ready to Start Your Planted Tank?</h3>
<p>At Nalanda Aquarium, we stock incredibly healthy, quarantined Neon Tetras ready for your community tank. We also carry a massive selection of aquatic plants, dark soils, and driftwood to help you build the perfect Amazonian biotope. Drop by our store in Bangalore or message us on WhatsApp to check our current live stock!</p>"""

content = pattern.sub(new_body, content)

with open('blog-neon-tetra.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created blog-neon-tetra.html")
