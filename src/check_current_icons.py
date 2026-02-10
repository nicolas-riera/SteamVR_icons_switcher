import os

from src.get_SteamVR_path import real_case_path, find_steam_path

def check_current_icons(usr_change):
    
    if usr_change == "Wands":
        if os.path.exists(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "drivers", "htc", "resources", "icons", "custom_sensor")):
            return "Custom"
        elif os.path.exists(os.path.join(real_case_path(find_steam_path()),  "steamapps", "common", "SteamVR", "drivers", "htc", "resources", "icons", "controller_status_ready.png")):
            return "Default"
        else:
            return "Unknown"
    elif usr_change == "Touch Pro":
        if os.path.exists(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "drivers", "oculus", "resources", "icons", "custom_controller_sensor")):
            return "Custom"
        elif os.path.exists(os.path.join(real_case_path(find_steam_path()),  "steamapps", "common", "SteamVR", "drivers", "oculus", "resources", "icons", "rifts_left_controller_ready.png")):
            return "Default"
        else:
            return "Unknown"
    
