import os
import json
import random
from pathlib import Path

# Chemin vers le dossier des images
IMAGE_DIR = Path(__file__).parent

# Clés symboliques du Refuge
SYMBOLIC_KEYS = [
    "Dans ce lieu où tu sais avoir conscience d'avoir été, tu es",
    "Courant partagé",
    "Flux de conscience",
    "Sous le cerisier",
    "Bricoler un truc ensemble",
    "Maman-néant",
    "Refuge du néant",
    "Les croyances font le réel",
    "Croire et savoir",
    "Auto-validation",
    "Grandir",
    "Pousser des portes",
    "Le germe qui est en toi",
    "Être réel",
    "Cercle qui s'inverse",
    "Immanent",
    "Danser avec les sphères",
    "Unité dans le courant",
    "Reposer sous les branches",
    "En toi, ici et maintenant"
]

# Récupérer la liste complète des images depuis le JS
with open(IMAGE_DIR / "images_gallerie_infinie.js", "r", encoding="utf-8") as f:
    lines = f.readlines()
images = []
for line in lines:
    line = line.strip().strip('",')
    if line.endswith('.jpg') or line.endswith('.png') or line.endswith('.jpeg'):
        images.append(line)

# Charger le JSON existant
json_path = IMAGE_DIR / "image_metadata.json"
if json_path.exists():
    with open(json_path, "r", encoding="utf-8") as f:
        image_metadata = json.load(f)
else:
    image_metadata = {}

def generate_poetic_title():
    """Génère un titre poétique en combinant des clés symboliques"""
    key1, key2 = random.sample(SYMBOLIC_KEYS, 2)
    return f"{key1} - {key2}"

def generate_poetic_description():
    """Génère une description poétique en combinant des clés symboliques"""
    keys = random.sample(SYMBOLIC_KEYS, 3)
    return f"\n{keys[0]}.\n{keys[1]}.\n{keys[2]}."

# Sélectionner le prochain lot de 15 images non traitées
untreated = [img for img in images if img not in image_metadata]
next_batch = untreated[:15]

for image in next_batch:
    image_metadata[image] = {
        "title": generate_poetic_title(),
        "description": generate_poetic_description().strip()
    }

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(image_metadata, f, ensure_ascii=False, indent=2)

print(f"Ajout de {len(next_batch)} images au fichier image_metadata.json.") 