#!/usr/bin/python3

import sys
import os 
import socket


hyprland_instance_signature = os.getenv("HYPRLAND_INSTANCE_SIGNATURE")
home_key = "HOME"
hyprland_socket = "/tmp/hypr/" + hyprland_instance_signature + "/.socket2.sock"
wallpaper_path = os.getenv(home_key) + "/Pictures/kanagawa_bowl.jpg" 

def subscribe_to_socket():
    clientsocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    clientsocket.connect(hyprland_socket)
    buffer = ''
    while True:
        buffer = clientsocket.recv(1024).decode("utf-8")
        if buffer.startswith("monitoradded>>") or buffer.startswith("monitorremoved>>"):
            re_set_wallpapers()
        

def re_set_wallpapers():
    os.popen("hyprctl dispatch exec 'swww img " + wallpaper_path + " --no-resize'").close()

def main():
    subscribe_to_socket()


if __name__ == "__main__":
    main()