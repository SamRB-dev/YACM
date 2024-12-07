# -*- coding: utf-8 -*-
import json, logging
import polars as pl

class contentHanlder:
    def __init__(self) -> None:
        self.__contentType:list = ["url", "directory", "text", "file"]
        self.__path: str = "../db/db.json"
        
    def ReadJson(self) -> dict:
        try:
            with open(self.__path, mode="r") as file:
                jsonFileContent = json.load(file)
                return jsonFileContent
        except Exception as error:
            print(error)  
            
    def defineContentType__(self, data: str) -> str:
        if data.startswith("http://") or data.startswith("https://"):
            return self.__contentType[0]
        elif data.startswith("file:///") and data.endswith("/"):
            return self.__contentType[1]
        else:
            return self.__contentType[2]
            
if __name__ == "__main__":
    print(contentHanlder().defineContentType__("file:///x/"))