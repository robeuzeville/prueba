import os
from zipfile import ZipFile
import pandas as pd

def detectaZip(zipParentName, ruta):
    global listaRutas
    myzip = ZipFile(zipParentName, 'r')
    ruta = ruta + '/' + zipParentName
    for name in myzip.namelist():
        rutaArchivo = ruta + '/' + name
        listaRutas.append(rutaArchivo)

        if name.endswith('.zip'):
            detectaZip(name, ruta)
    
    myzip.close()

ruta = "C:/Users/AL256AN/OneDrive - EY/Documents/Documentos APIs"
rutaTXT = "C:/Users/AL256AN/OneDrive - EY/Documents/Documentos APIs"
listaRutas = list()
os.chdir(ruta)

zipParentName = 'Geolocalización.zip'

detectaZip(zipParentName, ruta)

data = pd.DataFrame(listaRutas)
data.head()
data.to_csv('Lista_rutas.csv', sep=";", index=False, header=None)
