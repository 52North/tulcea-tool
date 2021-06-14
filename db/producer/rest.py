from wq.db import rest
from .models import Producer
from .serializers import ProducerSerializer
from .views import ProducerViewSet


rest.router.register_model(
    Producer,
    viewset=ProducerViewSet,
    serializer=ProducerSerializer,
    fields="__all__",
    cache="all",
    locate=True,
    map=[{
        'mode': 'list',
        'autoZoom' : False,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Producătorilor</span><img style="height: 20px; padding-right: 5px" src="images/producer.png"><img style="height: 20px; padding-right: 5px" src="images/milk-bottle2.png"><img style="height: 20px; padding-right: 5px" src="images/group-of-fruits.png"><img style="height: 20px; padding-right: 5px" src="images/group-of-vegetables.png"><img style="height: 20px; padding-right: 5px" src="images/steak-rare.png"><img style="height: 20px; padding-right: 5px" src="images/fish.png"><img style="height: 20px; padding-right: 5px" src="images/bakery.png"><img style="height: 20px;" src="images/honey.png">',
            'url': 'producers.geojson',
            'popup': 'producer',
            'icon' : '{{#category_dairy_products}}milk-bottle2{{/category_dairy_products}}{{#category_fruits}}group-of-fruits{{/category_fruits}}{{#category_vegetables}}group-of-vegetables{{/category_vegetables}}{{#category_meat}}steak-rare{{/category_meat}}{{#category_fish}}fish{{/category_fish}}{{#category_bakery_products}}bakery{{/category_bakery_products}}{{#category_honey}}honey{{/category_honey}}{{#category_none}}producer{{/category_none}}',
        }],
    }, {
        'mode': 'detail',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Producătorilor</span><img style="height: 20px;" src="images/producer.png">',
            'url': 'producers/{{id}}.geojson',
            'popup': 'producer',
            'flatten': True,
            'icon' : 'producer',
        }],
    }, {
        'mode': 'edit',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Producătorilor</span><img style="height: 20px;" src="images/producer.png">',
            'url': 'producers/{{id}}/edit.geojson',
            'popup': 'producer',
            'geometryField': 'geometry',
            'flatten': True,
            'icon' : 'producer',
        },{
            'type': 'geojson',
            'name': 'distance tool',
            'url': 'producers/{{id}}/edit.geojson',
            'popup': 'producer',
            'geometryField': 'geometry_line',
            'flatten': True,
            'icon' : 'producer',
            'draw': {
                'circle': False,
                'circlemarker': False,
                'marker': False,
                'polyline': {},
                'polygon': False,
                'rectangle': False,
            },
        },{
            'name': '<span style="padding-right: 5px;">Puncte de vânzare</span><img style="height: 20px;" src="images/salepoint.png">',
            'type': 'geojson',
            'url': 'salepoints.geojson',
            'popup': 'salepoint',
            'icon': 'salepoint',
        },{
            'name': '<span style="padding-right: 5px;">Puncte de depozitare</span><img style="height: 20px;" src="images/storagepoint.png">',
            'type': 'geojson',
            'url': 'storagepoints.geojson',
            'popup': 'storagepoint',
            'icon' : 'storagepoint',
        }],
    }],
)
