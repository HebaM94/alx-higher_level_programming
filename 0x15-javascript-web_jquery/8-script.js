$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    data.results.forEach(function(movie) {
    $("ul#list_movies").append($('<li></li>').text(movie.title));
    });
});
