import urllib3
import certifi
import json


http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
r = http.request('GET', 'https://d3e6htiiul5ek9.cloudfront.net/prod/productos?id_sucursal=10-3-251&limit=100&offset=99')
obj = json.load(r.data)




