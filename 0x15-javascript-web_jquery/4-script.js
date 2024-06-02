$('div#toggle_header').on('click', function() {
    $(this).toggleClass(function() {
        if ($('header').hasClass('red')) {
            $('header').removeClass('red').addClass('green');
        } else {
            $('header').removeClass('green').addClass('red');
        }
    });
});
