import zipfile
import io
import sys
import os
import pandas as pd

def enlistaRutas(zipFile, parent=[]):
    result = []
    try:
        myzip = zipfile.ZipFile(zipFile, 'r')
        for name in myzip.namelist():
            path = parent + [name]
            if name.lower().endswith(".zip"):
                result += enlistaRutas(io.BytesIO(myzip.open(name).read()), path)
            else:
                result.append("/".join(path))

    except Exception as ex:
        return result

    return result

ruta = 'C:/Users/AL256AN/OneDrive - EY/Documents/Pruebas Python'
os.chdir(ruta)

listaRutas = list()
dirs = os.listdir()
for file in dirs:
    if file.endswith('.zip'):
        listaRutas += enlistaRutas(open(file, "rb"), [ruta + '/' + file])

# print("\n".join(listaRutas))
data = pd.DataFrame(listaRutas)
CSV_name = 'Lista_rutas.csv'
data.to_csv(CSV_name, sep=";", index=False, header=None)

# listaRutas = enlistaRutas(open("Prueba01.zip", "rb"), ["Prueba01.zip"])
# print(listaRutas)
# print("\n".join(enlistaRutas(open("Prueba01.zip", "rb"), ["Prueba01.zip"])))
