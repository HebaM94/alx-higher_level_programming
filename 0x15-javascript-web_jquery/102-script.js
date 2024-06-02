$(document).ready(function() {
    $('input#btn_translate').on('click', function() {
        var language = $('input#language_code').val();
        var url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + language;
        $.get(url, function(data) {
            $("div#hello").text(data.hello);
        });
    });
});
