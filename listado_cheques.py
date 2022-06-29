import csv
import sys

argumentos = sys.argv

if len(argumentos) > 1:
    nombreArchivo = argumentos[1]
    dni=argumentos[2]
    salida=argumentos[3]
    tipoCheque=argumentos[4]
else:
    dni=''

file=open(nombreArchivo,'r')

lineas = csv.reader(file)

for cheque in lineas:
    if cheque[8] ==  dni:
        print("se encontro el cheque: ", cheque)
    else:
        print("no se encontro ningun cheque")

file.close()




