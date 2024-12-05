import json

def writeJson(path: str, content: dict) -> None:
    try:
        with open(path, mode="r") as file:
            File = json.load(file)
        File.update(content)
        with open(path, mode="w") as updateFile:
            json.dump(File, updateFile, indent=4)
    except Exception as error:
        print(error)
        
if __name__ == "__main__":
    writeJson("db/db.json", {"49" : {"content": "test"}})