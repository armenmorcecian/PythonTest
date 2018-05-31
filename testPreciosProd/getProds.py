import json
import requests
import os
from decimal import Decimal


tipodato = 'productos'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
sucursales = []

#limites sucursales capital
#-34.599722, -58.381944
#-34.691235, -58.354478


# creo la carpeta
if not os.path.exists(tipodato):
    os.makedirs(tipodato)

#traigo sucursales
with open('sucursales/sucursales.json', 'r') as fileSucursales:
    jsonSucursales = json.load(fileSucursales)

    for elemSucursal in jsonSucursales:
        if (Decimal(jsonSucursales[elemSucursal]['lat']) >= -34.691235) \
                and (Decimal(jsonSucursales[elemSucursal]['lat']) <= -34.599722) \
                and (Decimal(jsonSucursales[elemSucursal]['lng']) >= -58.381944) \
                and (Decimal(jsonSucursales[elemSucursal]['lng']) <= -58.354478):
            sucursales.append(jsonSucursales[elemSucursal]['id'])

for sucursal in sucursales:

    filename = tipodato + '/' + sucursal + '.json'
    offset = 0
    elementPos = 0
    tipodatoList = {}

    #creo el archivo
    if not os.path.exists(filename):
        #os.remove(filename)
        urlCant = 'https://d3e6htiiul5ek9.cloudfront.net/prod/productos?id_sucursal=' + sucursal + '&limit=100&offset=' + str(
                    offset)
        rTot = requests.get(urlCant, headers=headers).json()

        if isinstance(rTot['total'], int):

            totalElementos = rTot['total']

            while offset <= totalElementos:
                url = 'https://d3e6htiiul5ek9.cloudfront.net/prod/productos?id_sucursal=' + sucursal + '&limit=100&offset=' + str(
                    offset)
                r2 = requests.get(url, headers=headers).json()

                for element in r2['productos']:
                    tipodatoList[elementPos] = element
                    elementPos = elementPos + 1

                offset = offset + 99

        with open(filename, 'w') as outfile:
            json.dump(tipodatoList, outfile)

