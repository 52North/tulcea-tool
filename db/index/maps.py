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

def choose_icon(feature_properties):
    return 'producer'

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
        'name': '<span style="padding-right: 5px;">Producătorilor</span><img style="height: 20px; padding-right: 5px" src="images/producer.png"><img style="height: 20px; padding-right: 5px" src="images/milk-bottle2.png"><img style="height: 20px; padding-right: 5px" src="images/group-of-fruits.png"><img style="height: 20px; padding-right: 5px" src="images/group-of-vegetables.png"><img style="height: 20px; padding-right: 5px" src="images/steak-rare.png"><img style="height: 20px; padding-right: 5px" src="images/fish.png"><img style="height: 20px; padding-right: 5px" src="images/bakery.png"><img style="height: 20px;" src="images/honey.png">',
        'type': 'geojson',
        'url': 'producers.geojson',
        'popup': 'producer',
        'icon' : '{{#category_dairy_products}}milk-bottle2{{/category_dairy_products}}{{#category_fruits}}group-of-fruits{{/category_fruits}}{{#category_vegetables}}group-of-vegetables{{/category_vegetables}}{{#category_meat}}steak-rare{{/category_meat}}{{#category_fish}}fish{{/category_fish}}{{#category_bakery_products}}bakery{{/category_bakery_products}}{{#category_honey}}honey{{/category_honey}}{{#category_none}}producer{{/category_none}}',
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
