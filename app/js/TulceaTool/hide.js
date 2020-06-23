define({
  "run": function($page, routeInfo) {

    $page.ready( function() {
      $('.wq-yes-hide').hide();
      $('.wq-no-hide').hide();
    })

    $page.on('change', 'input[class="wq-hide"]', function(evt) {
      var $button = $(evt.target);

      if ($button.val() == "yes") {
        $('.wq-no-hide').show();
        $('.wq-yes-hide').hide();
        // $('.wq-no-hide').attr('required', '');
        // $('.wq-no-hide').attr('data-error', 'This field is required.');
      } else {
        $('.wq-no-hide').hide();
        $('.wq-yes-hide').show();
        // $('.wq-no-hide').removeAttr('required');
        // $('.wq-no-hide').removeAttr('data-error');
      }

      if ($button.val() == "renewable" || $button.val() == "both") {
        $('.wq-renewable-hide').show();
      } else {
        $('.wq-renewable-hide').hide();
      }

    })

  }
});
