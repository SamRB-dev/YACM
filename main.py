#! /bin/python
import pyperclip, time
from classes.eventHandler import eventHanlder
from pynput import keyboard

    
if __name__ == '__main__':
    handler = eventHanlder()
    listener = keyboard.Listener(on_press=handler.onPressed, on_release=handler.onReleased)
    listener.start()
    try:
        while True:
            pass
    except Exception as e:
        print(e)
    finally:
        listener.stop()
        