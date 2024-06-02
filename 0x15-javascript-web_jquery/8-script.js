$.ajax({
    method: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: (data) => {
        $.each(data.results, (index, movie) => {
        $('ul#list_movies').append($('<li></li>').text(movie.title));
        });
    }
});
