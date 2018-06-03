import json
import requests
import os
import logging
import psycopg2 as pg
import DBOps

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
                    try:
                        r2 = requests.get(url, headers=headers).json()

                        for element in r2['productos']:
                            tipodatoList[elementPos] = element
                            elementPos = elementPos + 1
                    except:
                        print('error con sucursal:'+sucursal+' offset:'+str(offset))

                    offset = offset + 99

            with open(filename, 'w') as outfile:
                json.dump(tipodatoList, outfile)
            print(filename)


def cargarProdsDB(path):

    PG_CONN_STRING = "host='localhost' dbname='postgres' user='postgres'"
    data_dir = path

    if os.path.exists(path):

        for file in os.listdir(path):
            dbconn1 = pg.connect(PG_CONN_STRING)
            cursor1 = dbconn1.cursor()
            #print(path+'/'+file)
            #print(os.path.splitext(file)[0])
            cursor1.execute("DROP SCHEMA productos CASCADE;")
            cursor1.execute("CREATE SCHEMA productos;")
            dbconn1.commit()
            cursor1.close()
            dbconn1.close()


            if os.path.splitext(file)[1] == '.json':

                with open(path + '/' + file, 'r') as fileProds:
                    jsonProds = json.load(fileProds)
                    sucursalNorm = os.path.splitext(file)[0].replace("-", "_")
                    dbconn = pg.connect(PG_CONN_STRING)
                    cursor = dbconn.cursor()
                    DBOps.crearTabla('PRODS_' + sucursalNorm, 'productos')

                    for producto in jsonProds:
                        #print(jsonProds[producto]['precio'])
                        #print(jsonProds[producto]['marca'])
                        #print(jsonProds[producto]['id'])
                        #print(jsonProds[producto]['nombre'])
                        #print(jsonProds[producto]['presentacion'])
                        try:
                            cursor.execute("INSERT INTO productos.PRODS_" + sucursalNorm + "("
                                           "precio, "
                                           "marca, "
                                           "producto_id, "
                                           "nombre, "
                                           "presentacion, "
                                           "sucursal_id)"
                                           "VALUES(%s, %s, %s, %s, %s, %s)",
                                           (
                                               jsonProds[producto]['precio'],
                                               jsonProds[producto]['marca'],
                                               jsonProds[producto]['id'],
                                               jsonProds[producto]['nombre'],
                                               jsonProds[producto]['presentacion'],
                                               os.path.splitext(file)[0]
                                           )
                                           )
                            dbconn.commit()
                        except:
                           print('duplicate row sucursal:' + os.path.splitext(file)[0] + ' id:' + jsonProds[producto]['id'])

                    cursor.close()
                    dbconn.close()
            else:
                print('no se puede cargar'+file)



#importarProductos()
cargarProdsDB('productos')
