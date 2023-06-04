import json

from utilities.variables import CONFIG_PATH


def get_token() -> str:
    with open(CONFIG_PATH) as file:
        return json.load(file)["user_token"]

def get_headers() -> dict:
    return {"Authorization": f"Bearer {get_token()}"} if get_token() else {}



# if __name__ == '__main__':
#     user_id = "Machkour"
#     competition_id = "2352"
#     # package_folder(user_id="Machkour", competition_id="2352", kind="template")
#     print(download_file_from_api(user_id=user_id, competition_id=competition_id))