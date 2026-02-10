from src.action_selector import action_selector
from src.get_SteamVR_path import get_SteamVR_path
from src.check_SteamVR_running import check_SteamVR_running

def main():
    check_SteamVR_running()
    get_SteamVR_path()
    action_selector()

if __name__ == "__main__":
    main()