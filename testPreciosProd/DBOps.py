
import psycopg2 as pg


def crearTabla(nombre, schema):

    PG_CONN_STRING = "host='localhost' dbname='postgres' user='postgres'"
    dbconn = pg.connect(PG_CONN_STRING)
    cursor = dbconn.cursor()
    nombreNorm = nombre.replace("-", "_")
    try:
        cursor.execute("CREATE TABLE " + schema + '.' + nombreNorm + "("
                                "precio double precision, "
                                 "marca character(200) COLLATE pg_catalog.""default"", "
                                 "producto_id character(200) COLLATE pg_catalog.""default"" NOT NULL, "
                                 "nombre character(200) COLLATE pg_catalog.""default"", "
                                 "presentacion character(200) COLLATE pg_catalog.""default"", "
                                 "sucursal_id character(200) COLLATE pg_catalog.""default"","
                                 "CONSTRAINT " + nombreNorm + "_pkey PRIMARY KEY (producto_id))"
                                 "WITH (   OIDS = FALSE ) TABLESPACE pg_default;"
                       )
    except:
        print('error al crear tabla')
    else:
        dbconn.commit()

    cursor.close()
    dbconn.close()


#crearTabla('P_1-1-1', 'productos')