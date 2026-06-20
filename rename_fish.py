import os

folder = r"C:\Users\vijay\git\nalandaaquarium\media\Store\fish"

# Mapping of old file names to corrected new names
corrections = {
    "Red melon and blue diamond discus.mp4": "Red Melon and Blue Diamond Discus.mp4",
    "white butterfly.mp4": "White Butterfly.mp4",
    "flowerhorn.mp4": "Flowerhorn.mp4",
    "Show grade avalible for sale Golden base or Golden trimac.mp4": "Show Grade Available for Sale - Golden Base or Golden Trimac.mp4",
    "Super Red Raflesia 5Inch aviable last 2 pcs.jpeg": "Super Red Rafflesia 5 Inch - Available Last 2 Pcs.jpeg",
    "5- 5.5inch red flora super raflesia discus.mp4": "5 to 5.5 Inch Red Flora Super Rafflesia Discus.mp4",
    "Red raflesia & Jaquar Raflesia 5inch.mp4": "Red Rafflesia & Jaguar Rafflesia 5 Inch.mp4",
    "Butterfly without light discus 4.5inch.mp4": "Butterfly Without Light Discus 4.5 Inch.mp4",
    "Red checkerboard 2.5 - 3inch.mp4": "Red Checkerboard 2.5 - 3 Inch.mp4"
}

for old_name, new_name in corrections.items():
    old_path = os.path.join(folder, old_name)
    new_path = os.path.join(folder, new_name)
    
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found: {old_name}")

