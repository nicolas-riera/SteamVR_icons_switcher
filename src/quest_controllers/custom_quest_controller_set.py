import os
import shutil

from src.get_SteamVR_path import real_case_path, find_steam_path
from src.clear import clear

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE = os.path.join(BASE_DIR, "..", "..", "assets", "Quest controllers", "custom", "icons")

DESTINATION = os.path.join(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "drivers", "oculus", "resources", "icons"))

def custom_quest_controller_set():

    clear()

    shutil.copytree(SOURCE, DESTINATION, dirs_exist_ok=True)

    print("Success")
    input("Press Enter to continue.")