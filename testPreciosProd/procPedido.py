import os
import json
from math import sin, cos, sqrt, atan2, radians


def getSucursalesCerca(custlat, custlon, custdist):

    # approximate radius of earth in km
    R = 6373.0
    sucsresult = []
    custlat = radians(float(custlat))
    custlon = radians(float(custlon))

    with open('sucursales/sucursales.json', 'r') as fileSucursales:
        jsonsucursales = json.load(fileSucursales)

        for elemsucursal in jsonsucursales:
            suclat = radians(float(jsonsucursales[elemsucursal]['lat']))
            suclon = radians(float(jsonsucursales[elemsucursal]['lng']))
            dlon = suclon - custlon
            dlat = suclat - custlat
            #print(dlat, '-', dlon)
            a = sin(dlat / 2)**2 + cos(custlat) * cos(suclat) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = R * c


            if distance <= custdist:
                #print("Result:", jsonsucursales[elemsucursal]['id'], '-', distance)
                sucsresult.append([jsonsucursales[elemsucursal]['id'], distance])

    return sucsresult

def getSucsConProds(listaProductosId, sucscandidatas):

    path = 'productos'

    if os.path.exists(path):
        listaSucsConProd = []

        for sucursal in sucscandidatas:
            print(path+'/'+sucursal[0]+'.json')

            try:
                with open(path+'/'+sucursal[0]+'.json', 'r') as listado:
                    listadoJson = json.load(listado)
                    listaTemp=[]
                    for element in listadoJson:
                        #print(listadoJson[element]['id'])
                        if listadoJson[element]['id'] in listaProductosId:
                            listaTemp.append(
                                [
                                    sucursal[0],
                                    listadoJson[element]['nombre'],
                                    listadoJson[element]['marca'],
                                    listadoJson[element]['precio']
                                ]
                            )
                    if len(listaTemp) >= len(listaProductosId):
                        listaSucsConProd.append(sucursal)
            except:
                print('No existe el archivo')

    #print(listaSucsConProd)
    return listaSucsConProd


def getPrecios(sucursales, listaProductosId):
    dictPrecios = {}
    path = 'productos'

    for sucursal in sucursales:
        idSucursal = sucursal[0]
        dictPrecios[idSucursal] = {}
        dictPrecios[idSucursal]['suma'] = 0
        dictPrecios[idSucursal]['distancia'] = sucursal[1]
        dictPrecios[idSucursal]['productos'] = {}

        listaSucursal = []

        with open(path + '/' + idSucursal + '.json', 'r') as listado:
            listadoJson = json.load(listado)

            for element in listadoJson:
                # print(listadoJson[element]['id'])
                if listadoJson[element]['id'] in listaProductosId:
                    dictPrecios[idSucursal]['suma'] = round(dictPrecios[idSucursal]['suma'] + float(listadoJson[element]['precio']), 2)
                    dictPrecios[idSucursal]['productos'][listadoJson[element]['id']] = listadoJson[element]['precio']
    return dictPrecios


def devolverResultado(lat, lon, listaProductosId):

    sucscandidatas = getSucursalesCerca(lat, lon, 1)
    #print(sucscandidatas)
    listaSucsConProd = getSucsConProds(listaProductosId, sucscandidatas)
    print(getPrecios(listaSucsConProd, listaProductosId))


#devolverResultado('-34.568485', '-58.435059', ['7798062547788', '7500435012409', '7790895000997'])
devolverResultado('-34.5633', '-58.5585', ['7798062547788', '7500435012409', '7790895000997'])