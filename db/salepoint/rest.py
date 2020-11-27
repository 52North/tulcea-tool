from wq.db import rest
from .models import Salepoint


rest.router.register_model(
    Salepoint,
    fields="__all__",
    cache="all",
    locate=True,
    map=[{
        'mode': 'list',
        'autoZoom' : False,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Puncte de vânzare</span><img style="height: 20px;" src="images/salepoint.png">',
            'url': 'salepoints.geojson',
            'popup': 'salepoint',
            'icon' : 'salepoint',
        }],
    }, {
        'mode': 'detail',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Puncte de vânzare</span><img style="height: 20px;" src="images/salepoint.png">',
            'url': 'salepoints/{{id}}.geojson',
            'popup': 'salepoint',
            'flatten': True,
            'icon' : 'salepoint',
        }],
    }, {
        'mode': 'edit',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Puncte de vânzare</span><img style="height: 20px;" src="images/salepoint.png">',
            'url': 'salepoints/{{id}}/edit.geojson',
            'popup': 'salepoint',
            'geometryField': 'geometry',
            'flatten': True,
            'icon' : 'salepoint',
        }],
    }],
)
