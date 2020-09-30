define(['wq/app', 'wq/map', 'wq/patterns', 'wq/photos', './hide', './welcome', './i18n', 'wq/locate', './config', 'leaflet.draw', 'leaflet.markercluster'],
function(app, map, patterns, photos, hide, welcome, i18n, locate, config) {

app.use(hide);
app.use(welcome);
app.use(i18n);
app.use(photos);
app.use(map);
app.use(patterns);
app.use(locate);

//  Add new map icon
map.createIcon("producer", {'iconUrl': config.router.base_url.concat("/images/producer.png"), 'iconSize': [30, 30]});
map.createIcon("salepoint", {'iconUrl': config.router.base_url.concat("/images/salepoint.png"), 'iconSize': [30, 30]});
map.createIcon("storagepoint", {'iconUrl': config.router.base_url.concat("/images/storagepoint.png"), 'iconSize': [30, 30]});
map.createIcon("watersupplier", {'iconUrl': config.router.base_url.concat("/images/watersupplier.png"), 'iconSize': [20, 30]});
map.createIcon("energysource", {'iconUrl': config.router.base_url.concat("/images/energysource.png"), 'iconSize': [20, 30]});
map.createIcon("productionservice", {'iconUrl': config.router.base_url.concat("/images/productionservice.png"), 'iconSize': [30, 30]});

config.presync = presync;
config.postsync = postsync;
var ready = app.init(config).then(function() {
    app.jqmInit();
    app.prefetchAll();
});

// Sync UI
function presync() {
    $('button.sync').html("Syncing...");
    $('li a.ui-icon-minus, li a.ui-icon-alert')
       .removeClass('ui-icon-minus')
       .removeClass('ui-icon-alert')
       .addClass('ui-icon-refresh');
}

function postsync(items) {
    $('button.sync').html("Sync Now");
    app.syncRefresh(items);
}

return ready;

});
