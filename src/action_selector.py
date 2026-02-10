from src.get_SteamVR_path import real_case_path, find_steam_path
from src.check_current_icons import check_current_icons
from src.wands.custom_wands_set import custom_wands_set
from src.wands.default_wands_set import default_wands_set

from src.clear import clear

def action_selector():

    usr_change = None

    while True:

        if not usr_change:
            
            clear()

            print("Please select what you want to change : ")
            print("1. Vive Controllers")
            print("2. Quest Pro controllers")
            print("3. Quest 3")
            print("0. Exit")

            usr_choice = input()

            match usr_choice:
                case "1":
                    usr_change = "Wands"
                case "2":
                    usr_change = "Touch Pro"
                case "3":
                    usr_change = "Quest 3"
                case "0":
                    clear()
                    break
                case _:
                    clear()
                    print("Invalid Choice.")
                    input("Press Enter to Continue.")
                    usr_change = None

        elif usr_change:

            clear()

            if usr_change == "Wands":
                text_1 = "Use custom Vive Controllers icons"
                text_2 = "Use default Vive Controllers icons"
            elif usr_change == "Touch Pro":
                text_1 = "Use Quest Pro controllers icons"
                text_2 = "Use default Quest controllers icons"
            elif usr_change == "Quest 3":
                text_1 = "Use custom Quest 3 icons"
                text_2 = "Use default Quest icons"

            print(f"Current SteamVR path : {real_case_path(find_steam_path())}\steamapps\common\SteamVR")
            print(f"Current icons : {check_current_icons(usr_change)}\n")

            print("Please make a selection : ")
            print(f"1. {text_1}")
            print(f"2. {text_2} ")
            print("3. Switch element selection")
            print("0. Exit")

            usr_choice = input()

            match usr_choice:
                case "1":
                    if usr_change == "Wands":
                        custom_wands_set()
                case "2":
                    if usr_change == "Wands":
                        default_wands_set()
                case "3":
                    usr_change = None
                    continue
                case "0":
                    clear()
                    break
                case _:
                    clear()
                    print("Invalid Choice.")
                    input("Press Enter to Continue.")