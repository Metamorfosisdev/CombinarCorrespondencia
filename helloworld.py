#from fileinput import close
from turtle import update
from dircount import countfiles
from change_path import changePath
from print_files import printFiles
from show_menu import menu
from get_filenames import getFileNames

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





#Print files

#printFiles(3)

#Count deleted

#print( "Deleted: " + str(countfiles("bin")))

#Count uploads

#print( "Uploads: "+ str(countfiles("uploads")))



#Define txt files for the format 
persona = 'persona.txt'
oficio = 'oficio.txt'


#Show the menu
menu()
option = int(input("Enter yor option: "))


while option != 5: 
    if option == 1:

        print("Admin Panel \n")

    elif option == 2:

        #Upload new register 
        print("***Upload new file*** \n")
        #Input the new filename 
        newfile = input('Enter the new filename: \n')
        newfile = newfile + '.txt'
        #Mix format with the new filename
        combinar_archivos (persona, oficio, newfile)
        #Move file to uploads
        changePath(newfile, "uploads")

    elif option == 3:

        print("***Update file*** \n")
        getFileNames("uploads\\")
        
        updfile = input("*** Wich file would you like to update? *** \n")
        argfile = input("***What would you like to change?")

        #print(argfile + "has been updated into" + updfile)
        #changePath(updfile, "updates")


    elif option == 4:
        print("Deleted files \n")
    else:
        print("Invalid option \n")

    menu()
    option = int(input("Enter yor option: \n"))


print("Come soon!")