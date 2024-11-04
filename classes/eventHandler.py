# -*- coding: utf-8 -*-
# Imports
from pynput import keyboard
import logging, time

# init logger
logging.basicConfig(
            filename="log/app.log",
            filemode='a',
            format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
            datefmt="%d-%m-%Y %H:%M"
)


class eventHanlder:
    def __init__(self):
        self.__isCtrlPressed:bool = False
        self.__logging:object = logging.getLogger()
        self.__listener:object = keyboard.Listener(on_press=self.__CtrlPressed, on_release=self.__CtrlReleased)

    
    def __CtrlPressed(self, key:object) -> None:
        '''
            Checks if ctrl is pressed. If yes, then isCtrlPressed is to True, otherwise
            remains False.
        '''
        try:
            # breakpoint()
            if key == keyboard.Key.ctrl:
                self.__isCtrlPressed = True
            if self.__isCtrlPressed and hasattr(key, 'char') and key.char == 'c':
                print("CTRL + C")
        except Exception as error:
            self.__logging.exception(error)
    
    def __CtrlReleased(self,key) -> None:
        try:
            self.__isCtrlPressed = False
            print("CTRL Released")
        except Exception as error:
            self.__logging.exception(error)

    def init(self):
        self.__listener.start()

    def terminate(self):
        self.__listener.stop()

if __name__ == '__main__':
    handler = eventHanlder()
    handler.init()
    try:
        while True:
            # time.sleep(0.5)
            pass
    except Exception as e:
        print(e)
    finally:
        handler.terminate()
        
