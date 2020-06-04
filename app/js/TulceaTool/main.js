define(['wq/app', 'wq/map', 'wq/patterns', 'wq/photos',
        './config',
        'leaflet.draw', 'leaflet.markercluster'],
function(app, map, patterns, photos, config) {

app.use(map);
app.use(patterns);
app.use(photos);

//  Add new map icon
map.createIcon("producer", {'iconUrl': config.router.base_url.concat("/images/producer.png"), 'iconSize': [30, 30]});
map.createIcon("salepoint", {'iconUrl': config.router.base_url.concat("/images/salepoint.png"), 'iconSize': [30, 30]});
map.createIcon("storagepoint", {'iconUrl': config.router.base_url.concat("/images/storagepoint.png"), 'iconSize': [30, 30]});

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
