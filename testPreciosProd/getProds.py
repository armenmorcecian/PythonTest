import json
import requests
import os
from decimal import Decimal

#limites sucursales capital
#-34.68000, -58.56000
#-34.50000, -58.31000

def importarProductos():

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    tipodato = 'productos'
    sucursales = []

    # creo la carpeta
    if not os.path.exists(tipodato):
        os.makedirs(tipodato)

    #traigo sucursales
    with open('sucursales/sucursales.json', 'r') as fileSucursales:
        jsonSucursales = json.load(fileSucursales)

        for elemSucursal in jsonSucursales:
            if (float(jsonSucursales[elemSucursal]['lat']) >= -34.69000) \
                    and (float(jsonSucursales[elemSucursal]['lat']) <= -34.50000) \
                    and (float(jsonSucursales[elemSucursal]['lng']) >= -58.56000) \
                    and (float(jsonSucursales[elemSucursal]['lng']) <= -58.31000):
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
            print(filename)


importarProductos()
