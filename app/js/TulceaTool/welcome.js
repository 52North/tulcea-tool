define(['wq/store'], function (ds) { 'use strict';

var welcome = {
    name: 'welcome'
};

var $;

welcome.init = function (config) {
    $ = config && config.jQuery || window.jQuery;
    ds.set('pageloadcount', 0);
};

welcome.run = function ($page, routeInfo) {

  /* Show welcome dialog if it is the first page load */
  $page.ready( function() {

    if (window.location.pathname == "/login" ) {
      ds.set('pageloadcount', 0);
    }
    else if (window.location.pathname == "/" ) {
      ds.get('pageloadcount').then(function(pageloadcount) {
        if(pageloadcount == null) {
          $('div[id="welcome"]').addClass("active");
        }
        ds.set('pageloadcount', pageloadcount + 1);
      });
    }

  });

  /* Show welcome dialog */
  $page.on('click', '.welcome-open', function(evt) {
    $('div[id="welcome"]').addClass("active");
  })

  /* Hide welcome dialog */
  $page.on('click', '.welcome-close', function(evt) {
    $('div[id="welcome"]').removeClass("active");
  })


};

return welcome;

});
