import fileinput
#send the file and the word to find
def searchWord(path, word):
    #open file
    file = open(path, "r")
    word = (word)
    if(word in file.read()):

        
        replacement = input("Enter the replacement word: \n") 
        print("search: "+word +" replace: "+ replacement)
        
        with fileinput.FileInput(path, inplace= True, ) as file:
            for line in file:
                print(line.replace(word,replacement), end="")

        #file = open(path, "w")
        #file.write(data)
        #file.close()

    else:
        print("Your word did not match the search")
        file.close()