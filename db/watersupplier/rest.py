from wq.db import rest
from .models import Watersupplier


rest.router.register_model(
    Watersupplier,
    fields="__all__",
    cache="all",
    locate=True,
    map=[{
        'mode': 'list',
        'autoZoom' : False,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Furnizorilor de apă</span><img style="height: 20px;" src="images/watersupplier.png">',
            'url': 'watersuppliers.geojson',
            'popup': 'watersupplier',
            'icon' : 'watersupplier',
        }],
    }, {
        'mode': 'detail',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Furnizorilor de apă</span><img style="height: 20px;" src="images/watersupplier.png">',
            'url': 'watersuppliers/{{id}}.geojson',
            'popup': 'watersupplier',
            'flatten': True,
            'icon' : 'watersupplier',
        }],
    }, {
        'mode': 'edit',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Furnizorilor de apă</span><img style="height: 20px;" src="images/watersupplier.png">',
            'url': 'watersuppliers/{{id}}/edit.geojson',
            'popup': 'watersupplier',
            'geometryField': 'geometry',
            'flatten': True,
            'icon' : 'watersupplier',
        }],
    }],
)
