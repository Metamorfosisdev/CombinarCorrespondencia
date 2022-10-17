import os


from docx_convert import docxConvert
from dircount import countfiles
from change_path import changePath
from show_menu import menu
from get_filenames import getFileNames
from show_file import showFile
from search_word import searchWord
from admin_menu import adminMenu
from pdf_convert import pdfConvert

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


while option != 5: 
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
                print("\n***Docx converter ***")
                path = input("Enter the path of the file as: uploads\\raul.txt \n")
                filename = input("Enter the docx name: \n")
                docxConvert(os.getcwd() + "\\" + path, filename)

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

    else:
        print("Invalid option \n")

    menu()
    option = int(input("Enter your option: \n"))


print("Come soon!")