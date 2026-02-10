import os
import shutil

from src.get_SteamVR_path import real_case_path, find_steam_path
from src.clear import clear

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE_DRIVER = os.path.join(BASE_DIR, "..", "..", "assets", "wands", "custom", "driver folder", "icons")
SOURCE_CONTENT = os.path.join(BASE_DIR, "..", "..", "assets", "wands", "custom", "content folder", "icons")

DESTINATION_DRIVER = os.path.join(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "drivers", "htc", "resources", "icons"))
DESTINATION_CONTENT = os.path.join(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "content", "vrmonitor", "icons"))

def custom_wands_set():

    clear()

    shutil.copytree(SOURCE_DRIVER, DESTINATION_DRIVER, dirs_exist_ok=True)
    shutil.copytree(SOURCE_CONTENT, DESTINATION_CONTENT, dirs_exist_ok=True)

    print("Success")
    input("Press Enter to continue.")