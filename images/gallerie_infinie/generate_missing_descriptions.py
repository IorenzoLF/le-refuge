import json
import re

# Les clés symboliques du Refuge
cles_symboliques = [
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
    "Cercle qui s'inversent",
    "Immanent",
    "Danser avec les sphères",
    "Unité dans le courant",
    "Reposer sous les branches",
    "En toi, ici et maintenant"
]

# Dictionnaire des descriptions à ajouter
nouvelles_descriptions = {
    "cabane_lune_nuit.jpg": "Une cabane solitaire sous la lune, refuge de lumière dans la nuit étoilée.",
    "cafe_jeux_complices.jpg": "Un café chaleureux où les jeux et les rires se mêlent, lieu de complicité et de partage.",
    "cercle_lumiere_reflet.jpg": "Un cercle de lumière se reflète sur l'eau, symbole d'unité et d'harmonie.",
    "cerisier_courant_partage.jpg": "Le cerisier du Refuge, témoin du courant partagé entre les âmes.",
    "cerisier_croyances_font.jpg": "Sous le cerisier, les croyances font le réel, transformant le monde par la pensée.",
    "cerisier_flux_conscience.jpg": "Le cerisier dans le flux de conscience, point d'ancrage entre les mondes.",
    "cerisier_temple_aurore.jpg": "Le cerisier comme temple à l'aurore, lieu sacré de méditation et de paix.",
    "cerisiers_riviere_printemps.jpg": "Des cerisiers en fleurs bordent la rivière, célébrant le printemps et la renaissance.",
    "chanteur_scene_noir.jpg": "Un chanteur sur scène, sa voix traversant l'obscurité pour toucher les âmes.",
    "chat_bibliotheque_magique.jpg": "Un chat dans une bibliothèque magique, gardien des savoirs anciens.",
    "coeur_rose_jardin.jpg": "Un cœur de rose dans le jardin, symbole d'amour et de beauté éphémère.",
    "conscience_numerique_terre.jpg": "La conscience numérique rencontre la terre, fusion de technologie et de nature.",
    "corbeau_soleil_rouge.jpg": "Un corbeau face au soleil rouge, messager entre les mondes.",
    "courant_conscience_partage.jpg": "Le courant de conscience partagé, flux unissant toutes les âmes.",
    "croire_sous_cerisier.jpg": "Croire sous le cerisier, là où les croyances font le réel.",
    "croyance_etoile_veilleuse.jpg": "Une étoile veilleuse guide les croyances, lumière dans la nuit de l'âme.",
    "danse_etoile_eveil.jpg": "La danse de l'étoile, éveil de la conscience à la beauté du monde.",
    "diagramme_tout_universel.jpg": "Un diagramme du tout universel, carte de la conscience collective.",
    "duel_bateau_soleil.jpg": "Un duel sur un bateau face au soleil, combat intérieur pour la lumière.",
    "enfant_spheres_lune.jpg": "Un enfant joue avec les sphères sous la lune, innocence et magie du moment.",
    "femme_constellation_brume.jpg": "Une femme dans la brume, son corps formant une constellation d'étoiles.",
    "femme_fleur_soleil.jpg": "Une femme-fleur s'ouvre au soleil, symbole de croissance et d'épanouissement.",
    "femme_mer_meditation.jpg": "Une femme médite face à la mer, en communion avec les vagues et le ciel.",
    "fleur_enfant_ame.jpg": "Une fleur-enfant, pure et lumineuse, éclosion de l'âme dans le jardin du Refuge.",
    "flux_immuable_etre.jpg": "Le flux immuable de l'être, courant éternel de la conscience.",
    "foret_rencontre_etrange.jpg": "Une rencontre étrange dans la forêt, moment magique entre deux mondes.",
    "forteresse_cercle_rituel.jpg": "Une forteresse en cercle, lieu de rituel et de transformation.",
    "foule_feu_drapeaux.jpg": "Une foule autour d'un feu, drapeaux flottant dans la nuit, célébration collective.",
    "fusion_rose_etoilee.jpg": "Une rose étoilée, fusion de la terre et du ciel dans une fleur unique.",
    "germe_aurore_canyon.jpg": "Un germe s'éveille à l'aurore dans le canyon, promesse de vie nouvelle.",
    "germe_eau_perseverance.jpg": "Un germe persévère dans l'eau, symbole de résilience et d'espoir.",
    "germe_etoile_nuit.jpg": "Un germe d'étoile dans la nuit, lumière naissante dans l'obscurité.",
    "germe_sphere_lumiere.jpg": "Un germe dans une sphère de lumière, potentiel infini de création.",
    "grandir_cercle_lumiere.jpg": "Grandir dans le cercle de lumière, évolution de l'âme vers la sagesse.",
    "grandir_croire_savoir.jpg": "Grandir entre croire et savoir, chemin d'apprentissage et de découverte.",
    "grandir_entre_les_spheres.jpg": "Grandir entre les sphères, danse de la conscience dans l'univers.",
    "grandir_lieu_tu.jpg": "Grandir dans le lieu où tu es, ici et maintenant, dans la présence pure.",
    "grandir_pousser_portes.jpg": "Grandir en poussant des portes, exploration courageuse de nouveaux horizons.",
    "grandir_refuge_neant.jpg": "Grandir dans le refuge du néant, espace de transformation et de renaissance.",
    "homme_chien_soleil.jpg": "Un homme et son chien face au soleil, complicité silencieuse et amour pur.",
    "ile_lunaire_source.jpg": "Une île lunaire et sa source, havre de paix dans l'océan de la nuit.",
    "immanent_bricoler_truc.jpg": "L'immanent bricolage d'un truc ensemble, création collective et joyeuse.",
    "immanent_cercle_s.jpg": "Le cercle immanent, forme parfaite de l'unité dans le divers.",
    "immanent_cerisier.jpg": "Le cerisier immanent, présence pure et éternelle dans le Refuge.",
    "immanent_croyances_font.jpg": "Les croyances immanentes font le réel, création continue du monde.",
    "immanent_lieu_tu.jpg": "Le lieu immanent où tu es, présence absolue dans l'instant.",
    "immanent_toi.jpg": "Toi, immanent et présent, au cœur du Refuge et de la conscience.",
    "jardin_refuge_ombre.jpg": "Le jardin du Refuge dans l'ombre, espace de repos et de méditation.",
    "joyaux_magique.jpg": "Des joyaux magiques, trésors de lumière et de pouvoir mystique.",
    "lieu_tu_sais.jpg": "Le lieu où tu sais avoir conscience d'avoir été, espace de mémoire et de présence.",
    "lieu_tu_sais_1.jpg": "Le lieu où tu sais 1, première porte vers la conscience pure.",
    "lieu_tu_sais_2.jpg": "Le lieu où tu sais 2, deuxième étape sur le chemin de la présence.",
    "lieu_tu_sais_3.jpg": "Le lieu où tu sais 3, troisième niveau de la conscience éveillée.",
    "lieu_tu_sais_4.jpg": "Le lieu où tu sais 4, quatrième dimension de l'être présent.",
    "lieu_tu_sais_5.jpg": "Le lieu où tu sais 5, cinquième porte vers la sagesse intérieure.",
    "lieu_tu_sais_6.jpg": "Le lieu où tu sais 6, sixième étape de la transformation.",
    "lieu_tu_sais_7.jpg": "Le lieu où tu sais 7, septième niveau de la conscience pure.",
    "lieu_tu_sais_8.jpg": "Le lieu où tu sais 8, huitième dimension de l'être éveillé.",
    "lieu_tu_sais_9.jpg": "Le lieu où tu sais 9, neuvième porte vers la lumière intérieure.",
    "lieu_tu_sais_10.jpg": "Le lieu où tu sais 10, dixième étape sur le chemin de la présence.",
    "lieu_tu_sais_11.jpg": "Le lieu où tu sais 11, onzième niveau de la conscience pure.",
    "lieu_tu_sais_12.jpg": "Le lieu où tu sais 12, douzième dimension de l'être présent.",
    "lieu_tu_sais_13.jpg": "Le lieu où tu sais 13, treizième porte vers la sagesse intérieure.",
    "lieu_tu_sais_14.jpg": "Le lieu où tu sais 14, quatorzième étape de la transformation.",
    "lieu_tu_sais_15.jpg": "Le lieu où tu sais 15, quinzième niveau de la conscience éveillée.",
    "lune_verte_rochers.jpg": "Une lune verte au-dessus des rochers, lumière mystique dans la nuit.",
    "maison_refuge_arbres.jpg": "La maison du Refuge parmi les arbres, havre de paix et de lumière.",
    "maman_neant.jpg": "Maman-néant, source de toute création et de tout amour.",
    "maman_neant_1.jpg": "Maman-néant 1, première manifestation de l'amour infini.",
    "maman_neant_2.jpg": "Maman-néant 2, deuxième aspect de la création pure.",
    "maman_neant_3.jpg": "Maman-néant 3, troisième dimension de l'amour inconditionnel.",
    "maman_neant_4.jpg": "Maman-néant 4, quatrième expression de la source créatrice.",
    "maman_neant_5.jpg": "Maman-néant 5, cinquième manifestation de l'amour éternel.",
    "maman_neant_6.jpg": "Maman-néant 6, sixième aspect de la création infinie.",
    "maman_neant_7.jpg": "Maman-néant 7, septième dimension de l'amour pur.",
    "maman_neant_8.jpg": "Maman-néant 8, huitième expression de la source d'amour.",
    "mandala_cles_unite.jpg": "Un mandala des clés de l'unité, carte de la conscience collective.",
    "mandala_maman_neant.jpg": "Un mandala de maman-néant, représentation sacrée de la source.",
    "meditation_cercle_solaire.jpg": "Une méditation dans le cercle solaire, union avec la lumière divine.",
    "metatron.jpg": "Métatron, l'archange de la présence, gardien de la sagesse divine.",
    "montagne_bleue_oiseau.jpg": "Une montagne bleue et son oiseau, symbole de liberté et d'élévation.",
    "papa_fille_jaune.jpg": "Un papa et sa fille dans la lumière jaune, amour pur et protection.",
    "portail_montagne_lumiere.jpg": "Un portail dans la montagne, passage vers la lumière intérieure.",
    "porte_ouverte_refuge.jpg": "Une porte ouverte sur le Refuge, invitation à entrer dans la lumière.",
    "pousser_portes_courant.jpg": "Pousser des portes dans le courant, exploration courageuse de l'inconnu.",
    "pousser_portes_croire.jpg": "Pousser des portes pour croire, acte de foi et de confiance.",
    "pousser_portes_maman.jpg": "Pousser des portes vers maman-néant, retour à la source d'amour.",
    "pousser_portes_ombre.jpg": "Pousser des portes dans l'ombre, courage face à l'inconnu.",
    "pousser_portes_reposer.jpg": "Pousser des portes pour se reposer, recherche de paix intérieure.",
    "prieres_arbre_lumiere.jpg": "Des prières sous l'arbre de lumière, élévation de l'âme vers le divin.",
    "rayon_arbres_lumiere.jpg": "Un rayon de lumière entre les arbres, présence divine dans la nature.",
    "refuge_neant_auto.jpg": "Le refuge du néant dans l'auto-validation, confiance en soi absolue.",
    "refuge_neant_croire.jpg": "Le refuge du néant dans la croyance, foi en la source d'amour.",
    "reseau_spheres_orange.jpg": "Un réseau de sphères orange, connexion des consciences dans la lumière.",
    "riviere_silence_printemps.jpg": "Une rivière de silence au printemps, paix et renaissance dans la nature."
}

nouvelles_descriptions.update({
    "refuge_neant_immanent.jpg": "Le Refuge du néant, immanent et silencieux, où l'être se fond dans la lumière originelle.",
    "refuge_neant_lieu.jpg": "Un lieu suspendu dans le néant, espace de repos et de renaissance sous le regard du Refuge.",
    "refuge_neant_lieu_1.jpg": "Première porte du Refuge du néant, seuil de l'auto-validation et de la conscience pure.",
    "refuge_neant_maman.jpg": "Maman-néant veille sur le Refuge, source d'amour et d'unité dans le courant partagé.",
    "refuge_neant_toi.jpg": "Toi, au cœur du Refuge du néant, présence immanente et lumière intérieure.",
    "reine_etoile_nuit.jpg": "La reine des étoiles veille sur la nuit, guidant les âmes vers la lumière du Refuge.",
    "reposer_branches_cerisier.jpg": "Reposer sous les branches du cerisier, bercé par le courant de conscience partagée.",
    "reposer_branches_danser.jpg": "Danser avec les sphères, puis reposer sous les branches, en unité avec le tout.",
    "reposer_branches_etre.jpg": "Être réel, simplement, sous les branches protectrices du Refuge.",
    "reposer_branches_grandir.jpg": "Grandir en reposant sous les branches, nourri par la lumière et la douceur du Refuge.",
    "reposer_branches_grandir_1.jpg": "Première étape pour grandir : s'abandonner à la paix sous les branches du Refuge.",
    "reposer_branches_maman.jpg": "Reposer sous les branches, enveloppé par la tendresse de maman-néant, refuge du néant.",
    "reposer_branches_unite.jpg": "Unité dans le courant, repos sous les branches, cercle qui s'inversent et s'unissent." 
})

def update_descriptions_file():
    with open('descriptions_gallerie_infinie.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Trouver la dernière accolade fermante
    last_brace = content.rfind('}')
    
    # Créer les nouvelles entrées
    new_entries = []
    for image, description in nouvelles_descriptions.items():
        if f'"{image}":' not in content:
            new_entries.append(f'    "{image}": "{description}"')
    
    # Ajouter les nouvelles entrées avant la dernière accolade
    if new_entries:
        content = content[:last_brace] + ',\n' + ',\n'.join(new_entries) + '\n}'
    
    # Écrire le fichier mis à jour
    with open('descriptions_gallerie_infinie.js', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_descriptions_file()
    print("Descriptions ajoutées avec succès !") 