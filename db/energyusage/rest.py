from wq.db import rest
from .models import Energyusage


rest.router.register_model(
    Energyusage,
    fields="__all__",
    locate=True,
    map=[{
        'mode': 'list',
        'autoZoom' : False,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Surse regenerabile de energie</span><img style="height: 20px;" src="images/energysource.png">',
            'url': 'energyusages.geojson',
            'popup': 'energyusage',
            'icon' : 'energysource',
        }],
    }, {
        'mode': 'detail',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Surse regenerabile de energie</span><img style="height: 20px;" src="images/energysource.png">',
            'url': 'energyusages/{{id}}.geojson',
            'popup': 'energyusage',
            'flatten': True,
            'icon' : 'energysource',
        }],
    }, {
        'mode': 'edit',
        'autoZoom' : True,
        'layers': [{
            'type': 'geojson',
            'name': '<span style="padding-right: 5px;">Surse regenerabile de energie</span><img style="height: 20px;" src="images/energysource.png">',
            'url': 'energyusages/{{id}}/edit.geojson',
            'popup': 'energyusage',
            'geometryField': 'geometry',
            'flatten': True,
            'icon' : 'energysource',
        }],
    }],
)
