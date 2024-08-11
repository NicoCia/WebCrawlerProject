# WebCrawlerProject

## Introducción

API en Python que cuenta con un método POST que recibé una URL de una Web App o Website 
```JSON
{
  "url": "string"
}
```

y responde con las "features" principales de la misma. 

```JSON
{
  "webmap": [
    { "name": "Home", "url": "url_recibida" },
    { "name": "Feature 1", "url": "url_recibida/feature-1" },
    { "name": "Feature 2", "url": "url_recibida/feature-2" },
    { "name": "Feature 3", "url": "url_recibida/feature-3" }
  ]
}
```

En caso de que la url ingresada no sea valida o el la request generada a dicha url no tenga respuesta,
el usuario recibira la correspondiente respuesta de error:

```JSON
{
  "error": "The provided url is not a valid url"
}
```

ó

```JSON
{
  "error": "Unable to connect to the requested url"
}
```

## Como ejecutar el proyecto

La presente herramienta se puede correr facilmente haciendo uso de la cli de fastapi.
Esto levantara la api generada en la dirección "http://127.0.0.1:8000".

```shell
  fastapi dev ./src/api/router.py
```

Una vez levantado el sistema se puede probar su funcionamiento desde la ruta http://127.0.0.1:8000/docs
o realizando request con herramientas como curl o postman.

## Links / Referencias
- [1] [FastAPI](https://fastapi.tiangolo.com/)
- [2] [Scrapy](https://scrapy.org/)
- [3] [Hos to extract data from an HTML in Python](https://www.zenrows.com/blog/web-crawler-python#extract-data-into-csv)
- [4] [Katana - a cli web crawler](https://blog.projectdiscovery.io/introducing-katana-the-best-cli-web-crawler/)
- [5] [GitHub repository](https://github.com/NicoCia/WebCrawlerProject)
