import os
from zipfile import ZipFile
import pandas as pd

def detectaZip(zipParentName, ruta):
    global listaRutas
    # Error en linea: zipParentName es listado como ruta
    # Ejemplo: 'roberto_raso_mx_ey_com/Documents/Desktop/Compañías/RR/CNOOC/2021/Carpeta Jessie/Cálculo LC 2020 presentado 2021/Archivos para proveedores.zip'
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

ruta = "A:/Mina/20220829-kmc-001/OD/RRaso/VB read files/20210827_To_20220401/SharePoint - Copy"
listaRutas = list()
os.chdir(ruta)

zipParentName = 'Roberto C Raso Salinas-2.zip'

detectaZip(zipParentName, ruta)

data = pd.DataFrame(listaRutas)
data.head()
data.to_csv('Lista_rutas.csv', sep=";", index=False, header=None)
