#update register 
def searchId (id, action):



    #Save ids in the db
    with open("DB.txt", "r", encoding="utf-8") as f:
        ids = []
        for line in f:
            ids.append(line.split(None, 1)[0])

    #Search if the id exist the coma is with the id

    if id in ids:


        #Found the line in the txt file
        pos = 0

        for i in ids:
            if i == id:
                break
            pos = pos + 1

        

        #Printing the line to update
        doc = open("DB.txt", "r", encoding= "utf-8")
        line = doc.readlines()
        doc.close()
        print(line[pos])

        #Update the register
        if action == 'update':
            update(pos)
        
        #Delete the register
        if action == 'delete':
            delete(pos)
        

    else:
        print("the value does not exist")

def update(line):
    old = input("What would you like to update: \n")
    new = input("What would be the new value? \n")

    with open("DB.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    #New data to update
    newdata = data[line].replace(old , new)

    #Assing the new data
    data[line] = newdata

    #Write in the DB.txt
    with open("DB.txt", "w", encoding="utf-8") as f:
        f.writelines(data)


    print("data updated: " + newdata)

    with open("updates.txt", "a", encoding="utf-8") as f:
        f.write(newdata)
    

def delete(delreg):
    print("line to delete: " + str(delreg))
    

    try: 
        with open("DB.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        deletefile = lines[delreg]
        pos = 0
        with open("DB.txt", "w", encoding="utf-8") as fw:

            for line in lines:

                if pos != int(delreg):
                    fw.write(line)

                pos += 1

            with open("deletes.txt", "a", encoding="utf-8") as f:
                f.write(deletefile)
            
            print("Register deleted successfully")

    except:
        print("Something went wrong with the DB file")

