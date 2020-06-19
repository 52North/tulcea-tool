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
        'name': '<span style="padding-right: 5px;">Sale points</span><img style="height: 20px;" src="images/salepoint.png">',
        'type': 'geojson',
        'url': 'salepoints.geojson',
        'popup': 'salepoint',
        'icon': 'salepoint',
    },
    {
        'name': '<span style="padding-right: 5px;">Storage points</span><img style="height: 20px;" src="images/storagepoint.png">',
        'type': 'geojson',
        'url': 'storagepoints.geojson',
        'popup': 'storagepoint',
        'icon' : 'storagepoint',
    },
    {
        'name': '<span style="padding-right: 5px;">Producers</span><img style="height: 20px;" src="images/producer.png">',
        'type': 'geojson',
        'url': 'producers.geojson',
        'popup': 'producer',
        'icon' : 'producer',
    },
    {
        'name': '<span style="padding-right: 5px;">Water suppliers</span><img style="height: 20px;" src="images/watersupplier.png">',
        'type': 'geojson',
        'url': 'watersuppliers.geojson',
        'popup': 'watersupplier',
        'icon' : 'watersupplier',
    }]
}]
