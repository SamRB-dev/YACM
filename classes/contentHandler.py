# -*- coding: utf-8 -*-
import pyperclip, datetime

class contentHanlder:
    def __init__(self) -> None:
        self.__contentType:list = ["url", "file", "text"]
        self.pclip:object = pyperclip
    
    def defineContentType__(self) -> str:
        if self.pclip.paste().startswith("http://") or self.pclip.paste().startswith("https://"):
            return self.__contentType[0]
        elif self.pclip.paste().startswith("file:///"):
            return self.__contentType[1]
        else:
            return self.__contentType[2]
            
if __name__ == "__main__":
    handler = contentHanlder()
    print(handler.defineContentType__())