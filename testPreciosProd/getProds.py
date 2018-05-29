import urllib3
import json
import requests
import certifi
import os

sucn3=0
sucursal = '10-3-'+str(sucn3)
offset = 0


#con urllib3
#http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
#r = http.request('GET', url)
#obj = json.load(r.data)

#con requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

while sucn3 <= 99:

    if not os.path.exists(sucursal):
        os.makedirs(sucursal)

    while offset <= 1000:
        url = 'https://d3e6htiiul5ek9.cloudfront.net/prod/productos?id_sucursal=' + sucursal + '&limit=100&offset=' + str(
            offset)
        r2 = requests.get(url, headers=headers).json()
        filename = sucursal+'/'+sucursal+'_'+str(offset)+'.json'

        with open(filename, 'w') as outfile:
            json.dump(r2, outfile)

        offset = offset+99

    sucn3 = sucn3+1
