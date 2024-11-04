#! /bin/python3
# -*- coding: utf-8 -*-

from pynput import keyboard
import time, sys

def on_press(key):
    try:
        print(f"{key.char} pressed")
    except Exception as e:
        print(key)

def on_release(key):
    try:
        print(f"{key.char} released")
        if key == keyboard.Key.esc:
            return False
    except Exception as e:
        print(key)
    
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

if __name__ == "__main__":
    try:
        while True:
            time.sleep(1)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        # listener.stop()
        # sys.exit(0)
        pass
