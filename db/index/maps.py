from django.conf import settings

basemaps = [
    {
        'name': "Stamen Terrain",
        'type': 'tile',
        'url': '//stamen-tiles-{s}.a.ssl.fastly.net/{layer}/{z}/{x}/{y}.jpg',
        'layer': 'terrain',
        'attribution': 'Map tiles by Stamen Design ...'
    }
];

index_map = [{
    'autoZoom' : False,
    'layers': [{
        'name': '<span style="padding-right: 5px;">Puncte de vânzare</span><img style="height: 20px;" src="images/salepoint.png">',
        'type': 'geojson',
        'url': 'salepoints.geojson',
        'popup': 'salepoint',
        'icon': 'salepoint',
    },
    {
        'name': '<span style="padding-right: 5px;">Puncte de depozitare</span><img style="height: 20px;" src="images/storagepoint.png">',
        'type': 'geojson',
        'url': 'storagepoints.geojson',
        'popup': 'storagepoint',
        'icon' : 'storagepoint',
    },
    {
        'name': '<span style="padding-right: 5px;">Producătorilor</span><img style="height: 20px;" src="images/producer.png">',
        'type': 'geojson',
        'url': 'producers.geojson',
        'popup': 'producer',
        'icon' : 'producer',
    },
    {
        'name': '<span style="padding-right: 5px;">Furnizorilor de apă</span><img style="height: 20px;" src="images/watersupplier.png">',
        'type': 'geojson',
        'url': 'watersuppliers.geojson',
        'popup': 'watersupplier',
        'icon' : 'watersupplier',
    },
    {
        'name': '<span style="padding-right: 5px;">Surse regenerabile de energie</span><img style="height: 20px;" src="images/energysource.png">',
        'type': 'geojson',
        'url': 'energyusages.geojson',
        'popup': 'energyusage',
        'icon' : 'energysource',
    },
    {
        'name': '<span style="padding-right: 5px;">Serviciilor de producție</span><img style="height: 20px;" src="images/productionservice.png">',
        'type': 'geojson',
        'url': 'productionservices.geojson',
        'popup': 'productionservice',
        'icon' : 'productionservice',
    }]
}]
