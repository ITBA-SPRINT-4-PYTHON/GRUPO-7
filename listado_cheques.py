import csv
import sys
import time
from datetime import *

def recorridoLista():
    aDevolver = ''
    for x in devolucion:
        aDevolver = aDevolver + ','.join(x) + '\n'
    return aDevolver

def imprimir():
    for x in devolucion:
        print(x)
        
def returnCsv():
    tiempo = int(datetime.now().timestamp())
    fileName = dni + str(tiempo) + '.csv'
    archivoCSV = open(fileName, 'a')
    archivoCSV.write(recorridoLista())  
    archivoCSV.close()

def checkEstado(estado):
    return estado == 'PENDIENTE' or estado == 'APROBADO' or estado == 'RECHAZADO'

def conversionFecha(fecha):
    rangoDiv = fecha.split(':')
    rangoDiv[0] = int(time.mktime(datetime.datetime.strptime(rangoDiv[0], "%d-%m-%Y").timetuple()))
    rangoDiv[1] = int(time.mktime(datetime.datetime.strptime(rangoDiv[1], "%d-%m-%Y").timetuple()))
    return rangoDiv


argumentos = sys.argv

todoBien = True
nroCheque = ''
msjError = ''
#---------------
estadoCheque = ''
rango = ''

devolucion = []

# if len(argumentos) == 5:
#     nombreArchivo = argumentos[1]
#     dni = argumentos[2]
#     salida = argumentos[3]
#     tipoCheque = argumentos[4]

# está mal pero no tan mal
if len(argumentos) > 4:
    nombreArchivo = argumentos[1]
    dni = argumentos[2]
    salida = argumentos[3]
    tipoCheque = argumentos[4]
    if len(argumentos) > 6 and checkEstado(argumentos[5]):
        estadoCheque = argumentos[5]
        if len(argumentos) > 7:
            rango = argumentos[6]
    elif len(argumentos) > 6:
        rango = argumentos[5]
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
                if estadoCheque != '':
                    if estadoCheque == cheque[10]:
                        if rango != '':
                            miRango = conversionFecha(rango)
                            if cheque[7] > miRango[0] and cheque[7] < miRango[1]:
                                devolucion.append(cheque)
                        else:
                            devolucion.append(cheque)
                else:
                    devolucion.append(cheque)


if msjError == '':
    if salida.lower() == 'pantalla':
        imprimir()
    elif salida.lower() == 'csv':
        returnCsv()
else:
    print(msjError)


file.close()
