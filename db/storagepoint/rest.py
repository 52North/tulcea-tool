from wq.db import rest
from .models import Storagepoint


rest.router.register_model(
    Storagepoint,
    fields="__all__",
    map=[{
        'mode': 'list',
        'autoLayers': True,
        'layers': [],
    }, {
        'mode': 'detail',
        'autoLayers': True,
        'layers': [],
    }, {
        'mode': 'edit',
        'layers': [{
            'type': 'geojson',
            'name': 'geometry',
            'url': 'storagepoints/{{id}}/edit.geojson',
            'draw': {
                'circle': False,
                'marker': {},
                'polyline': False,
                'polygon': False,
                'rectangle': False,
            },
            'geometryField': 'geometry',
            'flatten': True,
        }],
    }],
)
