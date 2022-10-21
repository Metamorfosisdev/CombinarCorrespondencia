#update register 
def searchId ():

    #Id send it for the client
    id = "1,"

    #Save ids in the db
    with open("DB.txt", "r", encoding="utf-8") as f:
        ids = []
        for line in f:
            ids.append(line.split(None, 1)[0])

    #Search if the id exist the coma is with the id

    if id in ids:

        print("the value exist")

        #Found the line in the txt file
        pos = 0

        for i in ids:
            if i == id:
                break
            pos = pos + 1

        #position to the line to update
        print("The value exist in: " + str(pos))

        #Printing the line to update
        doc = open("DB.txt", "r", encoding= "utf-8")
        line = doc.readlines()
        doc.close()
        print(line[pos])

        #Update the file
        update(pos)

    else:
        print("the value does not exist")

def update(line):
    #new = input("What would you like to update: \n")


    with open("DB.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    #New data to update
    newdata = data[line].replace("DIRECTOR" ,"PRESIDENTE")

    #Assing the new data
    data[line] = newdata

    #Write in the DB.txt
    with open("DB.txt", "w", encoding="utf-8") as f:
        f.writelines(data)


    print("data updated: " + newdata)

    

searchId()

