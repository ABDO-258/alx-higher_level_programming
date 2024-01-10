$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    const listMovies = $('#list_movies');

    $.each(movies, function (index, movie) {
      const listItem = $('<li></li>').text(movie.title);
      listMovies.append(listItem);
    });
});