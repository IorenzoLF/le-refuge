import os

# Dossier contenant les images
DOSSIER = '.'
# Fichier de sortie (à la racine du dossier images/gallerie_infinie)
FICHIER_SORTIE = 'images_gallerie_infinie.js'

# Extensions d'images acceptées
EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.webp')

# Lister les fichiers images
fichiers = [f for f in os.listdir(DOSSIER) if f.lower().endswith(EXTENSIONS) and os.path.isfile(os.path.join(DOSSIER, f))]
fichiers.sort()

# Générer le contenu JS
js = 'const imagesGallerieInfinie = [\n'
for f in fichiers:
    js += f'    "{f}",\n'
js += '];\n'

# Écrire le fichier
with open(FICHIER_SORTIE, 'w', encoding='utf-8') as out:
    out.write(js)

print(f"{len(fichiers)} images trouvées. Fichier '{FICHIER_SORTIE}' généré.") 