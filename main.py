import os

from db_update import searchId
from add_register import addRegister
from count_lines import newId
from db_menu import dbMenu
from docx_convert import docxConvert
from dircount import countfiles
from change_path import changePath
from show_menu import menu
from get_filenames import getFileNames
from show_file import showFile
from search_word import searchWord
from admin_menu import adminMenu
from pdf_convert import pdfConvert
from split import generateCertificates

def combinar_archivos(folio, persona, persona_folio):

    try:
        with open(folio, 'r', encoding= 'utf-8') as f1, open(persona, 'r', encoding= 'utf-8') as f2, open(persona_folio, 'a', encoding= 'utf-8') as f3:

            f3.write('\n')

            for l1, l2 in zip(f1,f2):
                
                
                l4 = l2.replace('\n', '') + l1.replace('\n', '')
                l4 = l4 + '\n'
                f3.write(l4)
               
                
         
        f1.close()
        f2.close()
        f3.close()

    except FileNotFoundError:
        print("A file could not be found")


#Define txt files for the format 
persona = 'persona.txt'
oficio = 'oficio.txt'


#Show the menu
menu()
option = int(input("Enter yor option: \n"))


while option != 6: 
    if option == 1:                 
        
        print("Admin Panel")

        adminMenu()
        aoption = int(input("Enter yor option: \n"))
        
        while aoption !=6:
            
            if aoption == 1:
                print("\n*** Upload files ***\n")
                files = []
                for file in os.listdir(os.getcwd()+"\\uploads"):
                    if file.endswith(".txt"):
                        files.append(file)
                print("You have: " + str(len(files)) + " upload files \n")
                print(files)


            elif aoption == 2:

                #Updated files
                print("\n*** Updated files ***")
                #Return the no. files updated
                nfiles = countfiles("uploads\\updates")
                print("\nYou have: " + str(nfiles) + " updated files\n")
                #Show the files
                getFileNames(os.getcwd()+"\\uploads\\updates")

            
            elif aoption == 3:

                #Deleted files
                print("\n*** Deleted files ***")
                #Return no. files updated
                nfiles = countfiles("uploads\\bin")
                print("\nYou have: " + str(nfiles) + " deleted files\n")
                #Show the files
                getFileNames(os.getcwd()+"\\uploads\\bin")
                

            elif aoption == 4:

                #Pdf converter
                print("\n***Pdf converter ***")
                path = input("Enter the path of the file as: uploads\\raul.txt \n")
                filename = input("Enter the pdf name: \n")
                pdfConvert(os.getcwd() + "\\" + path, filename)
            
            elif aoption == 5:
                print("\n*** Docx converter ***")
                path = input("Enter the path of the file as: uploads\\raul.txt \n")
                filename = input("Enter the docx name: \n")
                docxConvert(os.getcwd() + "\\" + path, filename)
            
            elif aoption == 6:
                print("\n*** DB ***")
                

            else: 
                print ("Invalid option: ")  

            adminMenu()
            aoption = int(input("Enter yor option: \n"))
        
        
    elif option == 2:

        #Upload new register 
        print("\n ***Upload new file*** \n")
        #Input the new filename 
        newfile = input('Enter the new filename: \n')
        newfile = newfile + '.txt'
        #Mix format with the new filename
        combinar_archivos (persona, oficio, newfile)
        #Move file to uploads
        changePath(newfile, "uploads")

    elif option == 3:

        print("\n ***Update file*** \n")
        #Show all file into uploads
        getFileNames("uploads\\")
        
        updfile = input("*** Wich file would you like to update? *** \n")

        #Show the information of the file 
     
        exist = showFile(updfile)

        if exist == "true":
            argfile = input("***What would you like to change?*** \n")
            #Update the file
            searchWord("uploads\\" + updfile, argfile)
            #Move to updates 
            #print(updfile + os.getcwd() + "\\uploads")
            changePath( updfile , "updates", os.getcwd() + "\\uploads")

        else:

            break


        #print(argfile + "has been updated into" + updfile)
        #changePath(updfile, "updates")


    elif option == 4:
        print("\n ***Delete a file*** \n")

        #Show files to delete
        getFileNames("uploads\\")
        delfile= input("Which file do you want to delete? \n")
        changePath(delfile, "bin", os.getcwd() + "\\uploads")

    elif option == 5:

        dbMenu()
        dboption = int(input("Enter your option: \n"))

        while dboption != 6:

            if dboption == 1:
                #Upload new register in database
                print("upload")
                
                #New id
                id = newId()

                #TODO: CUSTOM PROPERTIES UNCOMMENT THIS

                #Add the params for the format
                instituto = input("Enter your School: \n")
                nombre = input("Enter the student name: \n")
                registro = input("Enter the student register: \n")
                carrera = input("Enter the student career: \n")
                duracion = input("Enter the duration career: \n")
                actual = input("Enter the actual duration: \n")
                fecha = input("Enter the date: \n")
                responsable = input("Enter the current supervisor \n")
                cargo = input("Enter the supervisor position: \n")
                correo = input("Enter the supervisor email \n")	
                telefono = input("Enter the school number: \n") 
                domicilio = input("Enter the school address: \n")
                colonia = input("Enter the school colony: \n")
                cp = input("Enter the school cp: \n")

                #Add register with the new id
                addRegister(id, instituto, nombre, registro, carrera, duracion, actual, fecha, responsable, cargo, correo, telefono, domicilio, colonia, cp)


                #TODO: COMMENT THIS FOR CUSTOM UPLOAD
                #addRegister(id, "UVM", "RUBI ESPINAL FLORES", "14301085", "INGENIERIA FORECENCE", "9", "5", "20 Octubre 2022", "ING. AHTZIRY", "DIRECTORA", "aht@hotmail.com", "3320912074", "Prolo. Revolcion", "Nextipac", "45220")
            
            elif dboption == 2:

                print("*** update ***")

                #WICH REGISTER WOULD YOU LIKE TO UPDATE
                showFile("DB.txt")
                
                upreg = input("Which file would you like to update? \n")
                upreg = str(upreg) + ","

                #Search ID and if it exist it will be updated and added to updates.txt
                searchId(upreg, "update")


            elif dboption == 3:

                print("delete")
            
                #WICH REGISTER WOULD YOU LIKE TO DELETE
                showFile("DB.txt")

                delreg = input("Which file would you like to delete? \n")
                delreg = str(delreg) + ","
                
                #Search ID and if it exist it will be deleted and added to deletes.txt
                searchId(delreg, "delete")

            elif dboption == 4:

                print("*** show updated and deleted files *** \n")
                
                print("Updates files: \n")
                showFile("updates.txt")

                print("Deletes files: \n")
                showFile("deletes.txt")

            elif dboption == 5:

                print("*** Generate certificates *** \n")

                showFile("DB.txt")
                
                certificates = input("Which registers would you like to generate: \n")



                #generateCertificates("3,")

                print(certificates)
                
                
                

            else:
                print("Invalid option \n")
            
            dbMenu()
            dboption = int(input("Enter your option: \n"))



    else:
        print("Invalid option \n")

    menu()
    option = int(input("Enter your option: \n"))


print("Come soon!")