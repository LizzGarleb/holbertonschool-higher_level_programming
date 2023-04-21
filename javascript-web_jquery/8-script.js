$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: (data) => {
    data.results.forEach((movie) => {
      $('<li>').text(movie.title).appendTo($('UL#list_movies'));
    });
  }
});
