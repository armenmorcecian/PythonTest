# -*- coding: utf-8 -*-
import scrapy
import dmoz.items

class QuotesSpider(scrapy.Spider):
    name = "zonaprop"

    def start_requests(self):
        urls = [
            "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez.html",
            "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-2.html"
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-3.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-4.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-5.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-6.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-7.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-8.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-9.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-10.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-11.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-12.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-13.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-14.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-15.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-16.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-17.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-18.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-19.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-20.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-21.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-22.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-23.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-24.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-25.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-26.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-27.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-28.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-29.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-30.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-31.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-32.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-33.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-34.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-35.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-36.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-37.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-38.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-39.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-40.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-41.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-42.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-43.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-44.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-45.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-46.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-47.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-48.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-49.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-50.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-51.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-52.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-53.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-54.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-55.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-56.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-57.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-58.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-59.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-60.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-61.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-62.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-63.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-64.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-65.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-66.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-67.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-68.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-69.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-70.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-71.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-72.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-73.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-74.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-75.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-76.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-77.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-78.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-79.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-80.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-81.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-82.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-83.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-84.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-85.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-86.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-87.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-88.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-89.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-90.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-91.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-92.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-93.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-94.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-95.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-96.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-97.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-98.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-99.html",
            # "http://www.zonaprop.com.ar/departamento-venta-vicente-lopez-vicente-lopez-la-lucila-vicente-lopez-pagina-100.html"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
        sites = response.xpath("/html"
                               "/body[@id='listado']"
                               "/div[@id='vista-listado']"
                               "/div[@class='container container-listado-patrocinado']"
                               "/section[@id='listadoSection']"
                               "/ul[@id='avisos-content']"
                               "/li")

        for site in sites:

            id2=site.xpath("./@data-aviso").extract()

            titulo2 = site.xpath("./div[@class='aviso-data aviso-data--right']"
                                 "/div"
                                 "/div[@class='aviso-data-head']"
                                 "/div[@class='aviso-data-text']"
                                 "/h4"
                                 "/a"
                                 "/@title").extract()
            direccion2 = site.xpath("normalize-space(./div[@class='aviso-data aviso-data--right']"
                                    "/div"
                                    "/div[@class='aviso-data-head']"
                                    "/div[@class='aviso-data-text']"
                                    "/span"
                                    "/text())").extract()

            localidad2 = site.xpath("./div[@class='aviso-data aviso-data--right']"
                                    "/div"
                                    "/div[@class='aviso-data-head']"
                                    "/div[@class='aviso-data-text']"
                                    "/span"
                                    "/span"
                                    "/text()").extract()

            metros2 = site.xpath("normalize-space(./div[@class='aviso-data aviso-data--right']"
                                 "/div"
                                 "/ul"
                                 "/li"
                                 "/text())").extract()

            precio2 = site.xpath("./div[@class='aviso-data']"
                                 "/div[@class='aviso-data-price']"
                                 "/div"
                                 "/span[@class='aviso-data-price-value']"
                                 "/text()").extract()

            print(id2, titulo2, direccion2, localidad2, metros2, precio2)

            item = dmoz.items.PropItem()
            item['id'] = id2
            item['titulo'] = titulo2
            item['direccion'] = direccion2
            item['localidad'] = localidad2
            item['metros'] = metros2
            item['precio'] = precio2

            yield item

