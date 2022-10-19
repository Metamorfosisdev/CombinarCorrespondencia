#String 
data = 'RAUL, CETI, 3320912074'

#Separar un string y colocar las palabras en un arreglo
array = data.split(', ')

format = "hola NOMBRE mi institucion es INSTITUTO y mi numero de telefono TELEFONO".replace(
    "NOMBRE", array[0] ).replace(
        "INSTITUTO", array[1]).replace("TELEFONO", array[2])


#Hacer el primer elemento un arreglo

with open("DB.txt", "r", encoding= "utf-8") as f:
    for l1 in f:
        if(l1.startswith("2")):
            array = l1.split(', ')

#print(array)

fin = open("constancia.txt", "rt", encoding= "utf-8")

fout = open("out.txt", "wt", encoding= "utf-8")

for line in fin:
    fout.write(line.replace("INSTITUTO", array[1]).replace(
        "NOMBRE", array[2]).replace("REGISTRO", array[3]).replace(
            "CARRERA", array[4]).replace("DURACION", array[5]).replace(
                "ACTUAL", array[6]).replace("FECHA", array[7]).replace(
                    "RESPONSABLE", array[8]).replace("CARGO", array[9]).replace(
                        "CORREO", array[10]).replace("TELEFONO", array[11]).replace(
                            "DOMICILIO", array[12]).replace("COLONIA",array[13]).replace(
                                "CP", array[14]))

fin.close()
fout.close()

print(array[1])

#with open("constancia.txt", "r", encoding="utf-8") as f2:
#    for line in f2:
#        l2.replace("INSTITUTO", array[0])
 
#print(f2)