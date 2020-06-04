define(["data/config", "data/templates", "data/version", "module"],
function(config, templates, version, module) {

var overrides = module.config();

config.router = {
    'base_url': '/tulcea-tool'
};

config.template = {
    'templates': templates,
    'defaults': {
        'version': version
    }
};

config.store = {
    'service': config.router.base_url,
    'defaults': {'format': 'json'}
};

config.map = {
    'bounds': [[45.15, 28.75], [45.20, 28.81]],
    'basemaps': [{
        'name': 'OpenStreetMap Carto',
        'type': 'tile',
        'url': '//a.tile.openstreetmap.org/{z}/{x}/{y}.png',
        'layer': 'terrain',
        'attribution': '© <a href="https://www.openstreetmap.org">OpenStreetMap</a> contributors (<a href="https://www.openstreetmap.org/copyright">ODbL</a>) | <a href="https://icons8.com">icons8</a>'
    },
    {
        'name': 'OpenTopoMap',
        'type': 'tile',
        'url': '//a.tile.opentopomap.org/{z}/{x}/{y}.png',
        'layer': 'terrain',
        'attribution': 'Map data: © <a href="https://www.openstreetmap.org">OpenStreetMap</a> contributors (<a href="https://www.openstreetmap.org/copyright">ODbL</a>), SRTM | Map design: © <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>) | <a href="https://icons8.com">icons8</a>'
    }]
};

config.outbox = {};

config.transitions = {
    'default': "slide",
    'save': "flip"
};

for (var key in overrides) {
    config[key] = overrides[key];
}

return config;

});
