import pandas
import os
import json
from decimal import Decimal

listaProductosId = ['7798062547788', '7500435012409', '7790895000997']
sucursales = []

#for element in listaProductosId:
    #print(element)

listaProdsEnSuc = []

path = 'productos'

#filtrar sucursales cerca

def getProds(listaProductosId):
    if os.path.exists(path):

        for sucursal in os.listdir(path):

            if sucursal.endswith('.json'):

                with open(path+'/'+sucursal, 'r') as listado:
                    listadoJson = json.load(listado)
                    listaTemp=[]
                    for element in listadoJson:
                        #print(listadoJson[element]['id'])
                        if listadoJson[element]['id'] in listaProductosId:
                            listaTemp.append(
                                [
                                    os.path.splitext(sucursal)[0],
                                    listadoJson[element]['nombre'],
                                    listadoJson[element]['marca'],
                                    listadoJson[element]['precio']
                                ]
                            )
                    if len(listaTemp) == 3:
                        listaProdsEnSuc.append(os.path.splitext(sucursal)[0])

    #print(listaProdsEnSuc)
    return listaProdsEnSuc


def getMejorPrecio(sucursales, listaProductosId):
    dictPrecios = {}

    for sucursal in sucursales:
        dictPrecios[sucursal] = [0]
        listaSucursal = []

        with open(path + '/' + sucursal + '.json', 'r') as listado:
            listadoJson = json.load(listado)

            for element in listadoJson:
                # print(listadoJson[element]['id'])

                if listadoJson[element]['id'] in listaProductosId:
                    dictPrecios[sucursal][0] = round(dictPrecios[sucursal][0] + float(listadoJson[element]['precio']), 2)
                    dictPrecios[sucursal].append([listadoJson[element]['id'], listadoJson[element]['precio']])
    return dictPrecios


sucursales = getProds(listaProductosId)
print(getMejorPrecio(sucursales, listaProductosId))