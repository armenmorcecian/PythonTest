import urllib3
import json
import requests
import certifi
import os
from csv import DictWriter

offset = 0
tipodato = 'sucursales'
elementPos = 0
tipodatoList = {}

#con urllib3
#http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
#r = http.request('GET', url)
#obj = json.load(r.data)

#con requests
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







#with open(filename, "rb") as json_data:
#    my_data = json.load(json_data)

