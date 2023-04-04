import os
import subprocess

# Fonction pour augmenter ou diminuer le volume du fichier vidéo
def ajuster_volume(fichier_video, db):
    # Déterminer si l'utilisateur veut augmenter ou baisser le volume
    choix = input("Voulez-vous augmenter ou baisser le volume ? (a/b) ")
    if choix.lower() == 'a':
        # Augmenter le volume
        commande = f"ffmpeg -i '{fichier_video}' -vcodec copy -af 'volume={db}dB' -f mp4 output.mp4"
    elif choix.lower() == 'b':
        # Baisser le volume
        commande = f"ffmpeg -i '{fichier_video}' -vcodec copy -af 'volume=-{db}dB' -f mp4 output.mp4"
    else:
        print("Choix invalide.")
        return

    # Exécuter la commande FFmpeg pour ajuster le volume
    subprocess.run(commande, shell=True)

    # Afficher un message de confirmation
    print(f"Le fichier vidéo '{fichier_video}' a été ajusté de {db}dB.")

# Obtenir le chemin complet du script
script_path = os.path.abspath(__file__)

# Obtenir le chemin complet du dossier contenant le script
script_dir = os.path.dirname(script_path)

# Obtenir la liste des fichiers dans le dossier contenant le script
fichiers = os.listdir(script_dir)

# Afficher la liste des fichiers dans le dossier contenant le script
print("Liste des fichiers dans le dossier :", fichiers)

# Filtrer la liste des fichiers pour ne garder que les fichiers vidéo
fichiers_video = [f for f in fichiers if f.endswith(('.mkv', '.mp4', '.avi', '.webm'))]

# Vérifier qu'il y a au moins un fichier vidéo dans le dossier
if len(fichiers_video) == 0:
    print("Il n'y a pas de fichiers vidéo dans ce dossier.")
    exit()

# Si plusieurs fichiers vidéo, demander à l'utilisateur lequel utiliser
if len(fichiers_video) > 1:
    print("Plusieurs fichiers vidéo ont été trouvés :")
    for i, f in enumerate(fichiers_video):
        print(f"{i+1}. {f}")
    choix = input("Sélectionnez le fichier à ajuster (1-{len(fichiers_video)}) : ")
    try:
        choix = int(choix)
        if choix < 1 or choix > len(fichiers_video):
            raise ValueError
    except ValueError:
        print("Choix invalide.")
        exit()
    fichier_video = fichiers_video[choix-1]
else:
    fichier_video = fichiers_video[0]

# Demander le nombre de décibels à ajuster à l'utilisateur
db = input("Combien de décibels voulez-vous ajuster ? ")

# Appeler la fonction pour ajuster le volume du fichier vidéo
ajuster_volume(fichier_video, db)

