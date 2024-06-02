
function fetchTranslation() {
    var language = $('input#language_code').val();
        var url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + language;
        $.get(url, function(data) {
            $("div#hello").text(data.hello);
        }).fail(function() {
             $("div#hello").text('Error: Unable to fetch translation');
        });
}

$(document).ready(function() {
    $('input#btn_translate').on('click',fetchTranslation);
    $('input#language_code').keypress(function(event){
        if (event.keyCode === 13) {
            fetchTranslation();
        }
    });
});
