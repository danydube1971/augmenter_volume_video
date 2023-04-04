# Augmenter_volume_video
Permet d'augmenter ou de diminuer le volume d'un fichier vidéo sans altérer la qualité vidéo.

Le script permet à l'utilisateur de sélectionner un fichier vidéo dans le dossier contenant le script, 
d'ajuster le volume de ce fichier vidéo en augmentant ou en diminuant le nombre de décibels, et de créer un fichier vidéo de sortie 
au format MP4 avec le même contenu vidéo, pistes audio et sous-titres que le fichier vidéo d'origine.

**Description en détail du script :**

1. Tout d'abord, le script utilise la bibliothèque os pour obtenir le chemin complet du script Python et le chemin complet du dossier contenant le script.
2. Ensuite, il obtient la liste des fichiers dans le dossier contenant le script en utilisant la méthode **os.listdir()**.
3. Le script filtre la liste des fichiers pour ne garder que les fichiers vidéo en utilisant une compréhension de liste et la méthode **str.endswith()**.
4. Si aucun fichier vidéo n'est trouvé, le script affiche un message d'erreur et se termine.
5. Si plusieurs fichiers vidéo sont trouvés, le script demande à l'utilisateur lequel il souhaite ajuster en affichant la liste des fichiers vidéo avec une boucle **for**.
6. Le script demande à l'utilisateur le nombre de décibels qu'il souhaite ajouter ou soustraire au volume du fichier vidéo.
7. Ensuite, le script appelle la fonction **ajuster_volume()** avec le nom du fichier vidéo et le nombre de décibels en tant que paramètres.
8. La fonction **ajuster_volume()** demande à l'utilisateur s'il souhaite augmenter ou baisser le volume du fichier vidéo et utilise la valeur de la réponse pour construire une commande FFmpeg qui ajustera le volume du fichier vidéo en utilisant l'option **-af 'volume=...dB'**.
9. La commande FFmpeg est exécutée en utilisant la méthode **subprocess.run()** et le fichier vidéo de sortie est créé dans le format MP4 en utilisant l'option **-f mp4**.
10. Enfin, la fonction **ajuster_volume()** affiche un message de confirmation pour indiquer que le fichier vidéo a été ajusté avec succès.

----------------

**Comment utiliser ce script**

Placer le script dans le même répertoire que le ou les fichiers vidéos auxquels vous voulez ajuster le volume.

Exécuter le script avec la commande suivante: **python3 "Augmenter le volume d'une vidéo.py"**
