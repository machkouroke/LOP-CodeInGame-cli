from enumerations import Enum
from typing import Annotated

import requests
import typer

from utilities.variables import get_base_url


class DownloadKind(str, Enum):
    solve = 'solve'
    template = 'template'


def lopdownload(
        kind: Annotated[DownloadKind ,typer.Option(..., help="Le type de fichier à télécharger")] = DownloadKind.template,
        path: Annotated[str, typer.Option(..., help="Le chemin du fichier à télécharger")] = '.'
):
    print(f"Le type de fichier à télécharger est {kind}")
    response = requests.post(
        f"{get_base_url()}/auth/login",
        json={"mail": mail, "password": password},
    )
    # if args.kind == 'étudiant':
    #     print(f"Téléchargement du fichier '{args.name}' en tant qu'étudiant...")
    #     repertoire_local = args.directory
    #     chemin_fichier = os.path.join(repertoire_local, args.name)
    #     if os.path.exists(chemin_fichier):
    #         #url distant du serveur à compléter
    #         url_distant ='http://localhost:8080/upload'
    #         with open(chemin_fichier, 'rb') as file:
    #             response = requests.post(url_distant, files={'file': file})
    #         if response.status_code == 200:
    #             print(f"Le fichier '{args.name}' a été téléchargé avec succès en tant qu'étudiant.")
    #         else:
    #             print("Erreur lors de l'envoi du fichier au serveur distant.")
    #     else:
    #         print("Le fichier spécifié n'existe pas.")
    # elif args.kind == 'professeur':
    #     print(f"Téléchargement du fichier '{args.name}' en tant que professeur...")
    #     repertoire_local = args.directory
    #     chemin_fichier = os.path.join(repertoire_local, args.name)
    #     if os.path.exists(chemin_fichier):
    #         # url distant du serveur à compléter
    #         url_distant = 'http://localhost:8080/upload'
    #         with open(chemin_fichier, 'rb') as file:
    #             response = requests.post(url_distant, files={'file': file})
    #             print("bye")
    #         if response.status_code == 200:
    #             print(f"Le fichier '{args.name}' a été téléchargé avec succès en tant qu'étudiant.")
    #         else:
    #             print("Erreur lors de l'envoi du fichier au serveur distant.")
    #     else:
    #         print("Le fichier spécifié n'existe pas.")
    # else:
    #     print("Valeur invalide pour l'option --kind. Veuillez spécifier 'étudiant' ou 'professeur'.")

if __name__ == '__main__':
    typer.run(lopdownload)
