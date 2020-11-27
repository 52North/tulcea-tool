from wq.db import rest
from .models import Storagepoint


rest.router.register_model(
    Storagepoint,
    fields="__all__",
    cache="all",
    locate=True,
    map=[{
        'mode': 'list',
        'autoZoom' : False,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Puncte de depozitare</span><img style="height: 20px;" src="images/storagepoint.png">',
            'url': 'storagepoints.geojson',
            'popup': 'storagepoint',
            'icon' : 'storagepoint',
        }],
    }, {
        'mode': 'detail',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Puncte de depozitare</span><img style="height: 20px;" src="images/storagepoint.png">',
            'url': 'storagepoints/{{id}}.geojson',
            'popup': 'storagepoint',
            'flatten': True,
            'icon' : 'storagepoint',
        }],
    }, {
        'mode': 'edit',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Puncte de depozitare</span><img style="height: 20px;" src="images/storagepoint.png">',
            'url': 'storagepoints/{{id}}/edit.geojson',
            'popup': 'storagepoint',
            'geometryField': 'geometry',
            'flatten': True,
            'icon' : 'storagepoint',
        }],
    }],
)
