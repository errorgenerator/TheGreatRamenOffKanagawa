#!/usr/bin/python3

import os
import signal
import sys
import time

home_key = "HOME"
state_flag_file = os.getenv(home_key) + "/.config/hypr/scripts/tmp/.ac_power"

def signal_handler(sig, frame):
    sys.exit(0)

def get_state():
    state = os.popen("cat /sys/class/power_supply/ACAD/online").read().replace('\n', '')
    return state

def set_state_flag_file():
    if get_state() == "1":
        if not os.path.exists(state_flag_file):    
            open(state_flag_file, 'x')
    elif os.path.exists(state_flag_file) and get_state() == "0":
        os.remove(state_flag_file)
    else:
        return

def main():
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        time.sleep(5)
        set_state_flag_file()


if __name__ == "__main__":
    main()