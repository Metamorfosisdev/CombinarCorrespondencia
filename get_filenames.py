import os

def getFileNames(path=os.getcwd()):
    entries = os.listdir(path)

    try:
        for entry in entries:
            print(entry)
        print("\n")
    except :
        print("Something went wrong")