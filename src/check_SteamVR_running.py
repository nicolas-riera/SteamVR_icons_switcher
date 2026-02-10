import psutil
import time

def check_SteamVR_running():

    process_name = "vrserver.exe" 

    running = any(proc.name().lower() == process_name.lower() for proc in psutil.process_iter())

    if running:
        print("SteamVR is running. Please close it before running this program.")
        print("Program will exit.")
        time.sleep(5)
        exit()
