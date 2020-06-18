from wq.db import rest
from .models import Watersupplier


rest.router.register_model(
    Watersupplier,
    fields="__all__",
    locate=True,
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
            'url': 'watersuppliers/{{id}}/edit.geojson',
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
