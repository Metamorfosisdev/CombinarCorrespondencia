

#send the file with the path 
def showFile(file):
    try:
        file = open(file, mode= "r", encoding="utf-8")
        print(file.read())
        return "true"
    except FileNotFoundError:
        print("THE FILE DOES NOT EXIST")
        return "false"
    except: 
        print("Something went wrong try again")
        return "false"