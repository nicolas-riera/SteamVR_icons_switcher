import os
import shutil

from src.get_SteamVR_path import real_case_path, find_steam_path
from src.clear import clear

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE = os.path.join(BASE_DIR, "..", "..", "assets", "Quest controllers", "default", "icons")

DESTINATION = os.path.join(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "drivers", "oculus", "resources", "icons"))

CUSTOM_SENSOR = os.path.join(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "drivers", "oculus", "resources", "icons", "custom_controller_sensor"))

def default_quest_controller_set():

    clear()

    shutil.copytree(SOURCE, DESTINATION, dirs_exist_ok=True)

    if os.path.exists(CUSTOM_SENSOR):
        os.remove(str(CUSTOM_SENSOR))

    print("Success")
    input("Press Enter to continue.")