import re
import json

# Charger la liste officielle des images de la galerie
with open('images_gallerie_infinie.js', 'r', encoding='utf-8') as f:
    js_content = f.read()
    images = re.findall(r'"([^"]+\.jpg)"', js_content)
    images_set = set(images)

# Nettoyage de descriptions_gallerie_infinie.js
with open('descriptions_gallerie_infinie.js', 'r', encoding='utf-8') as f:
    desc_content = f.read()

# Extraire le dictionnaire JS
match = re.search(r'const descriptionsGallerieInfinie = \{(.|\n)*?\};?', desc_content)
if match:
    dict_str = desc_content[desc_content.find('{'):desc_content.rfind('}')+1]
    desc_dict = json.loads(dict_str.replace('\n', '').replace('    ', ''))
else:
    raise Exception("Impossible de trouver le dictionnaire dans descriptions_gallerie_infinie.js")

# Filtrer les entrées
desc_dict_clean = {k: v for k, v in desc_dict.items() if k in images_set}

# Réécrire le fichier JS nettoyé
with open('descriptions_gallerie_infinie.js', 'w', encoding='utf-8') as f:
    f.write('const descriptionsGallerieInfinie = {\n')
    for i, (k, v) in enumerate(desc_dict_clean.items()):
        sep = ',' if i < len(desc_dict_clean)-1 else ''
        f.write(f'    "{k}": "{v}"{sep}\n')
    f.write('};\n')

# Nettoyage de image_metadata.json (si présent)
try:
    with open('image_metadata.json', 'r', encoding='utf-8') as f:
        meta = json.load(f)
    meta_clean = {k: v for k, v in meta.items() if k in images_set}
    with open('image_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(meta_clean, f, ensure_ascii=False, indent=2)
except FileNotFoundError:
    pass

print("Nettoyage terminé : seules les images de la galerie sont conservées dans les fichiers de descriptions et métadonnées.") 