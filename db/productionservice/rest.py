from wq.db import rest
from .models import Productionservice


rest.router.register_model(
    Productionservice,
    fields="__all__",
    locate=True,
    map=[{
        'mode': 'list',
        'autoZoom' : False,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Production services</span><img style="height: 20px;" src="images/productionservice.png">',
            'url': 'productionservices.geojson',
            'popup': 'productionservice',
            'icon' : 'productionservice',
        }],
    }, {
        'mode': 'detail',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Production services</span><img style="height: 20px;" src="images/productionservice.png">',
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
            'name': '<span style="padding-right: 5px;">Production services</span><img style="height: 20px;" src="images/productionservice.png">',
            'url': 'productionservices/{{id}}/edit.geojson',
            'popup': 'productionservice',
            'geometryField': 'geometry',
            'flatten': True,
            'icon' : 'productionservice',
        }],
    }],
)
