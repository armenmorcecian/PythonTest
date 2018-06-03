import json
import requests
import os
import logging
import psycopg2 as pg




def getSucursalesFaltantes():

    offset = 0
    tipodato = 'sucursales'
    elementPos = 0
    tipodatoList = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    if not os.path.exists(tipodato):
        os.makedirs(tipodato)

    if os.path.exists(tipodato+'/'+tipodato+'.json'):
        os.remove(tipodato+'/'+tipodato+'.json')

    urlCant = 'https://d3e6htiiul5ek9.cloudfront.net/prod/sucursales?limit=30&offset=' + str(offset)
    rTot = requests.get(urlCant, headers=headers).json()


    if isinstance(rTot['total'], int):

        totalElementos = rTot['total']

        while offset <= totalElementos:
            url = 'https://d3e6htiiul5ek9.cloudfront.net/prod/sucursales?limit=30&offset=' + str(offset)
            r2 = requests.get(url, headers=headers).json()
            filename = tipodato+'/'+tipodato+'.json'

            for element in r2['sucursales']:
                tipodatoList[elementPos] = element
                elementPos = elementPos + 1

            offset = offset + 29

        with open(filename, 'w') as outfile:
            json.dump(tipodatoList, outfile)


#getSucursalesFaltantes()

#load into postgre

def cargarEnDB(path):
    # !/usr/bin/env python

    logger = logging.getLogger()

    PG_CONN_STRING = "host='localhost' dbname='postgres' user='postgres'"

    data_dir = path
    dbconn = pg.connect(PG_CONN_STRING)

    logger.info("Loading data from '{}'".format(data_dir))

    cursor = dbconn.cursor()

    counter = 0
    empty_files = []

    #pi = ProgressInfo(os.path.expanduser(data_dir))

    with open(path, 'r') as fileSucursales:
        jsonSucs = json.load(fileSucursales)

        for elemSuc in jsonSucs:
            try:
            #pi.update(counter)
                cursor.execute("INSERT INTO public.sucursales("
                               "bandera_id, "
                               "lat, "
                               "lng, "
                               "sucursal_nombre, "
                               "id, "
                               "sucursal_tipo, "
                               "provincia, "
                               "direccion, "
                               "bandera_descripcion, "
                               "localidad, "
                               "comercio_razon_social, "
                               "comercio_id, "
                               "sucursal_id)"
                               "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               (
                                   jsonSucs[elemSuc]['banderaId'],
                                   jsonSucs[elemSuc]['lat'],
                                   jsonSucs[elemSuc]['lng'],
                                   jsonSucs[elemSuc]['sucursalNombre'],
                                   jsonSucs[elemSuc]['id'],
                                   jsonSucs[elemSuc]['sucursalTipo'],
                                   jsonSucs[elemSuc]['provincia'],
                                   jsonSucs[elemSuc]['direccion'],
                                   jsonSucs[elemSuc]['banderaDescripcion'],
                                   jsonSucs[elemSuc]['localidad'],
                                   jsonSucs[elemSuc]['comercioRazonSocial'],
                                   jsonSucs[elemSuc]['comercioId'],
                                   jsonSucs[elemSuc]['sucursalId']
                               )
                               )
            except:
                print('duplicate row con id:'+jsonSucs[elemSuc]['id'])
            else:
                counter += 1
                print(counter)
                dbconn.commit()

    logger.info("Loaded {} files".format(counter))
    logger.info("Found {} empty files".format(len(empty_files)))
    if empty_files:
        logger.info("Empty files:")
        for f in empty_files:
            logger.info(" >>> {}".format(f))

    cursor.close()
    dbconn.close()


#with open(filename, "rb") as json_data:
#    my_data = json.load(json_data)

def mostrarSucursales(path):

    with open(path, 'r') as fileSucursales:
        jsonSucs = json.load(fileSucursales)

        for elemSuc in jsonSucs:
            print(jsonSucs[elemSuc]['banderaId'])
            print(jsonSucs[elemSuc]['lat'])
            print(jsonSucs[elemSuc]['lng'])
            print(jsonSucs[elemSuc]['sucursalNombre'])
            print(jsonSucs[elemSuc]['id'])
            print(jsonSucs[elemSuc]['sucursalTipo'])
            print(jsonSucs[elemSuc]['provincia'])
            print(jsonSucs[elemSuc]['direccion'])
            print(jsonSucs[elemSuc]['banderaDescripcion'])
            print(jsonSucs[elemSuc]['localidad'])
            print(jsonSucs[elemSuc]['comercioRazonSocial'])
            print(jsonSucs[elemSuc]['comercioId'])
            print(jsonSucs[elemSuc]['sucursalId'])

path='sucursales/sucursales.json'
#mostrarSucursales(path)
cargarEnDB(path)
