import json
import re

def extract_images_from_js(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Extract array content between square brackets
        match = re.search(r'\[(.*?)\]', content, re.DOTALL)
        if match:
            array_content = match.group(1)
            # Split by commas and clean up
            images = [img.strip().strip('"') for img in array_content.split(',')]
            return [img for img in images if img]  # Remove empty strings
    return []

def extract_descriptions_from_js(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Extract object content between curly braces
        match = re.search(r'\{(.*?)\}', content, re.DOTALL)
        if match:
            object_content = match.group(1)
            # Extract keys
            keys = re.findall(r'"([^"]+)":', object_content)
            return keys
    return []

# Read both files
images = extract_images_from_js('images_gallerie_infinie.js')
descriptions = extract_descriptions_from_js('descriptions_gallerie_infinie.js')

# Find missing descriptions
missing_descriptions = [img for img in images if img not in descriptions]

print(f"Nombre total d'images: {len(images)}")
print(f"Nombre total de descriptions: {len(descriptions)}")
print(f"Nombre d'images sans description: {len(missing_descriptions)}")
print("\nImages sans description:")
for img in missing_descriptions:
    print(f"- {img}") 