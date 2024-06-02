$.ajax({
    method: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: (data) => $('div#hello').text(data.hello)
});
