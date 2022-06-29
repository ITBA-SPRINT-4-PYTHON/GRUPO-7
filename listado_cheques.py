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

nroCheque=''
msjError=''

lineas = csv.reader(file)

for cheque in lineas:
    if cheque[8] ==  dni:
        if nroCheque=='':
            nroCheque=cheque[0]
        else:
            if cheque[0]==nroCheque:
                msjError= 'El DNI:', dni, 'tiene dos cheques iguales con nro: ', nroCheque
                break
    else:
        print("No se encontro ningun cheque")

file.close()




