import os
from zipfile import ZipFile
import pandas as pd

def detectaZip(zipParentName, ruta):
    global listaRutas
    # Error en linea: zipParentName es listado como ruta
    # Intentar llamar ruta completa / intentar separar string en lista y tomar último elemento
    # Separar 
    myzip = ZipFile(zipParentName, 'r')
    ruta = ruta + '/' + zipParentName
    print('parent:', zipParentName)
    # print('ruta:', ruta)
    for name in myzip.namelist():
        print(name)
        nameAsList = name.split('/')
        print(nameAsList[:-1])
        # rutaArchivo = ruta + '/' + name
        # listaRutas.append(rutaArchivo)

        # if name.endswith('.zip'):
        #     print(name, ruta)
        #     detectaZip(name, ruta)
    
    myzip.close()

ruta = "Ruta con /"
listaRutas = list()
os.chdir(ruta)

# Cambiar para que busque los archivos desde os
zipParentName = 'Nombre base'

detectaZip(zipParentName, ruta)

data = pd.DataFrame(listaRutas)
data.head()
data.to_csv('Lista_rutas.csv', sep=";", index=False, header=None)
