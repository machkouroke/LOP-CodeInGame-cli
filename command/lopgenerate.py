from enum import Enum
from typing import Annotated

import requests
import typer

from generator import generator
from model.Exercise import Exercise
from utilities.request import get_headers
from utilities.variables import get_base_url


class Language(str, Enum):
    PYTHON = "python"
id_exo = "647a9115366d4ba3edb6b380"



def lopgenerate(
        exercise: Annotated[str, typer.Option(help="L'id de l'exercice")],
):
    response = requests.get(
        f"{get_base_url()}/cli/lopgenerate/{exercise}",
        headers=get_headers(),
    )
    if response.status_code == 200:
        try:
            data = Exercise(**response.json())
            print(data)
            # generator[data["language"]](data.get("name", None))
        except FileExistsError:
            print("Le répertoire existe déjà")
    else:
        print(response.json()["detail"])



if __name__ == '__main__':
    typer.run(lopgenerate)
