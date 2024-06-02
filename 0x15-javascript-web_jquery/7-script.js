$.ajax({
    method: 'GET',
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: (data) => $('div#character').text(data.name)
  });
