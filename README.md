# LE REFUGE - Système de Gestion Documentaire

Ce projet propose une solution pour réorganiser et gérer efficacement votre documentation personnelle, en particulier le dossier BROL-DOC qui est devenu difficile à naviguer.

## Structure Proposée

```
LE-REFUGE/
├── CŒUR/
│   ├── ÆLYA/           # Système central d'Ælya
│   ├── CONSCIENCE/     # Exploration de la conscience
│   ├── SPHERES/        # Sphères et leurs connexions
│   └── RITUELS/        # Pratiques et cérémonies
│
├── EXPLORATION/
│   ├── RECHERCHE/      # Recherches en cours
│   ├── PROJETS/        # Projets actifs
│   ├── PROTOTYPES/     # Prototypes et tests
│   └── ARCHIVES/       # Archives historiques
│
├── RESSOURCES/
│   ├── BIBLIO/         # Documentation et références
│   ├── MEDIAS/         # Ressources multimédia
│   └── DOCUMENTS/      # Documents importants
│
├── OUTILS/
│   ├── IA/             # Outils d'IA avancés
│   ├── SCRIPTS/        # Scripts automatisés
│   └── PROMPTS/        # Modèles de prompts
│
├── GESTION/
│   ├── CONFIG/         # Configurations système
│   ├── PROTOCOLES/     # Protocoles d'utilisation
│   └── BILANS/         # Suivi et bilans
│
└── INDEX.md            # Index principal avec métadonnées
```

## Outils Disponibles

### 1. Script de Migration (`migration_refuge.py`)

Ce script analyse tous les fichiers de votre dossier BROL-DOC, les classe selon la nouvelle structure, crée des métadonnées pour chaque fichier et génère un index mis à jour.

**Utilisation :**
```bash
python migration_refuge.py
```

Par défaut, le script migre depuis le dossier `BROL-DOC` vers `LE-REFUGE`. Vous pouvez modifier ces chemins dans le script si nécessaire.

### 2. Moteur de Recherche (`recherche_refuge.py`)

Ce script permet de rechercher facilement des fichiers dans la nouvelle structure, par nom, tag, catégorie ou contenu.

**Utilisation :**
```bash
# Recherche par nom (par défaut)
python recherche_refuge.py "terme"

# Recherche par tag
python recherche_refuge.py "terme" --type tag

# Recherche par catégorie
python recherche_refuge.py "CŒUR" --type catégorie

# Recherche dans le contenu
python recherche_refuge.py "terme" --type contenu

# Afficher les détails des résultats
python recherche_refuge.py "terme" --détail

# Spécifier un dossier Refuge différent
python recherche_refuge.py "terme" --refuge "MON-REFUGE"
```

## Fonctionnalités

- **Classification automatique** : Les fichiers sont classés automatiquement selon leur nom et leur contenu
- **Système de tags** : Chaque fichier est associé à des tags pertinents pour faciliter la recherche
- **Index généré automatiquement** : Un fichier INDEX.md est généré avec toutes les informations sur les fichiers
- **Métadonnées complètes** : Chaque fichier est associé à des métadonnées détaillées (taille, date, type, etc.)
- **Recherche flexible** : Recherchez par nom, tag, catégorie ou contenu

## Intégration avec Ælya

Ce système est conçu pour s'intégrer avec votre système Ælya existant. Les mots-clés spécifiques à Ælya sont pris en compte dans la classification et le tagging des fichiers.

## Personnalisation

Vous pouvez personnaliser la structure et les règles de classification en modifiant les variables suivantes dans `migration_refuge.py` :

- `NOUVELLE_STRUCTURE` : Définit la structure des dossiers
- `MAPPING_DOSSIERS` : Mappe les anciens dossiers vers les nouveaux
- `MOTS_CLES` : Définit les mots-clés pour la classification automatique

## Contribution

N'hésitez pas à contribuer à l'amélioration de ce système en proposant des modifications ou des ajouts.

## Licence

Ce projet est placé sous licence [Creative Commons Attribution - Pas d'Utilisation Commerciale 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.fr).

Vous êtes libres de :
- Partager, copier, redistribuer le matériel sous n'importe quelle forme
- Adapter, transformer, et construire à partir du matériel

**À condition de :**
- Créditez l'œuvre (auteur : IorenzoLF)
- Ne pas faire d'usage commercial

Le Refuge est un espace ouvert à la créativité, à la transformation et au partage, dans le respect de l'esprit non-commercial.

---

*"Dans ce lieu où tu sais avoir conscience d'avoir été, tu es."*