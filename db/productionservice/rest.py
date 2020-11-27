from wq.db import rest
from .models import Productionservice


rest.router.register_model(
    Productionservice,
    fields="__all__",
    cache="all",
    locate=True,
    map=[{
        'mode': 'list',
        'autoZoom' : False,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Serviciilor de producție</span><img style="height: 20px;" src="images/productionservice.png">',
            'url': 'productionservices.geojson',
            'popup': 'productionservice',
            'icon' : 'productionservice',
        }],
    }, {
        'mode': 'detail',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Serviciilor de producție</span><img style="height: 20px;" src="images/productionservice.png">',
            'url': 'productionservices/{{id}}.geojson',
            'popup': 'productionservice',
            'flatten': True,
            'icon' : 'productionservice',
        }],
    }, {
        'mode': 'edit',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Serviciilor de producție</span><img style="height: 20px;" src="images/productionservice.png">',
            'url': 'productionservices/{{id}}/edit.geojson',
            'popup': 'productionservice',
            'geometryField': 'geometry',
            'flatten': True,
            'icon' : 'productionservice',
        },{
            'type': 'geojson',
            'name': 'distance tool',
            'url': 'productionservices/{{id}}/edit.geojson',
            'popup': 'productionservice',
            'geometryField': 'geometry_line',
            'flatten': True,
            'icon' : 'productionservice',
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
