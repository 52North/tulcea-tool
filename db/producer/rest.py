from wq.db import rest
from .models import Producer


rest.router.register_model(
    Producer,
    fields="__all__",
    locate=True,
    map=[{
        'mode': 'list',
        'autoZoom' : False,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Producers</span><img style="height: 20px;" src="images/producer.png">',
            'url': 'producers.geojson',
            'popup': 'producer',
            'icon' : 'producer',
        }],
    }, {
        'mode': 'detail',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Producer</span><img style="height: 20px;" src="images/producer.png">',
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
            'name': '<span style="padding-right: 5px;">Producer</span><img style="height: 20px;" src="images/producer.png">',
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
            'name': '<span style="padding-right: 5px;">Sale points</span><img style="height: 20px;" src="images/salepoint.png">',
            'type': 'geojson',
            'url': 'salepoints.geojson',
            'popup': 'salepoint',
            'icon': 'salepoint',
        },{
            'name': '<span style="padding-right: 5px;">Storage points</span><img style="height: 20px;" src="images/storagepoint.png">',
            'type': 'geojson',
            'url': 'storagepoints.geojson',
            'popup': 'storagepoint',
            'icon' : 'storagepoint',
        }],
    }],
)
