import csv
import sys
import datetime


def imprimir():
    for x in devolucion:
        print(x)
        
def returnCsv():
    tiempo = datetime.timestamp(datetime.now())
    fileName = dni + tiempo + '.csv'
    with open(fileName, 'a') as f:
        write = csv.writer(f)
        write.writerows(devolucion)
    
    f.close()


argumentos = sys.argv

todoBien = True
nroCheque = ''
msjError = ''

devolucion = []

if len(argumentos) == 5:
    nombreArchivo = argumentos[1]
    dni = argumentos[2]
    salida = argumentos[3]
    tipoCheque = argumentos[4]
else:
    todoBien = False
    msjError = 'ERROR EN CANTIDAD DE ARGUMENTOS'

file = open(nombreArchivo, 'r')

lineas = csv.reader(file)

if todoBien:
    for cheque in lineas:
        if cheque[8] == dni:
            if nroCheque == '':
                nroCheque = cheque[0]
            else:
                if cheque[0] == nroCheque:
                    msjError = 'El DNI:', dni, 'tiene dos cheques iguales con nro: ', nroCheque
                    break
            if cheque[9] == tipoCheque.upper():
                devolucion.append(cheque)
        else:
            print("No se encontro ningun cheque con dni: ", dni)


if msjError == '':
    if salida.lower() == 'pantalla':
        imprimir()
    elif salida.lower() == 'csv':
        returnCsv()
else:
    print(msjError)


file.close()
