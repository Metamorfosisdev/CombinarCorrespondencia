import shutil
import os

#Function for change the Path 

def changePath(file, dir):
    current_path = os.getcwd()
    src_path = current_path + "\\" + file
    dst_path = current_path + "\\" + dir + "\\" + file 

    try:
        shutil.move(src_path, dst_path)
        print(file + " INTO " + dir + " SUCCESSFULLY \n")
    except FileNotFoundError:
        print("FileNotFoundError")
    except :
        print("Something went wrong")
    

