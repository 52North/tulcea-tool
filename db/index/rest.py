from wq.db import rest
from .maps import basemaps, index_map
from django.conf import settings


rest.router.add_page('index', {
    'url': '',
    'map': index_map,
})

rest.router.add_page('about', {
    'url': 'about',
})

rest.router.add_page('food-guide', {
    'url': 'food-guide',
})

rest.router.add_page('water-guide', {
    'url': 'water-guide',
})

rest.router.add_page('consumer-guide', {
    'url': 'consumer-guide',
})

rest.router.add_page('legal-notice', {
    'url': 'legal-notice',
})

rest.router.add_page('privacy-statement', {
    'url': 'privacy-statement',
})

rest.router.add_page('terms-of-use', {
    'url': 'terms-of-use',
})

rest.router.set_extra_config(
    debug=settings.DEBUG,
    map={
        'bounds': [[-70, -180], [70, 180]],
        'basemaps': basemaps
    },
)
