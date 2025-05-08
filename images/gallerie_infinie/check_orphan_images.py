import os
import re
import json

# Chemins
dossier_images = '.'
js_images = 'images_gallerie_infinie.js'
js_desc = 'descriptions_gallerie_infinie.js'
meta_json = 'image_metadata.json'

# 1. Images référencées dans JS
with open(js_images, 'r', encoding='utf-8') as f:
    js_content = f.read()
    images_list = re.findall(r'"([^"]+\.jpg)"', js_content)
    images_set = set(images_list)

# 2. Images présentes dans le dossier
images_dossier = {f for f in os.listdir(dossier_images) if f.lower().endswith('.jpg')}

# 3. Descriptions référencées
with open(js_desc, 'r', encoding='utf-8') as f:
    desc_content = f.read()
    desc_dict = re.findall(r'"([^"]+\.jpg)"\s*:', desc_content)
    desc_set = set(desc_dict)

# 4. Métadonnées (optionnel)
try:
    with open(meta_json, 'r', encoding='utf-8') as f:
        meta = json.load(f)
        meta_set = set(meta.keys())
except FileNotFoundError:
    meta_set = set()

# Vérifications
manquantes_dossier = images_set - images_dossier
orphelines_dossier = images_dossier - images_set
orphelines_desc = desc_set - images_set
orphelines_meta = meta_set - images_set

print("--- Vérification de la galerie infinie ---")
print(f"Images référencées dans JS : {len(images_set)}")
print(f"Images présentes dans le dossier : {len(images_dossier)}")
print(f"Descriptions référencées : {len(desc_set)}")
if meta_set:
    print(f"Images dans image_metadata.json : {len(meta_set)}")
print()
if manquantes_dossier:
    print("Images référencées mais absentes du dossier :")
    for img in sorted(manquantes_dossier):
        print(f"  - {img}")
else:
    print("Aucune image référencée n'est absente du dossier.")

if orphelines_dossier:
    print("\nImages présentes dans le dossier mais non référencées :")
    for img in sorted(orphelines_dossier):
        print(f"  - {img}")
else:
    print("\nAucune image orpheline dans le dossier.")

if orphelines_desc:
    print("\nDescriptions orphelines (pas d'image correspondante) :")
    for img in sorted(orphelines_desc):
        print(f"  - {img}")
else:
    print("\nAucune description orpheline.")

if meta_set:
    if orphelines_meta:
        print("\nEntrées orphelines dans image_metadata.json :")
        for img in sorted(orphelines_meta):
            print(f"  - {img}")
    else:
        print("\nAucune entrée orpheline dans image_metadata.json.")
print("\nVérification terminée.") 