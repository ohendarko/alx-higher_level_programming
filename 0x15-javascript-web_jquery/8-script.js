$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (response) {
      var titles = [];
      response.results.forEach(function (movie) {
        titles.push('<li>' + movie.title + '</li>');
      });
      $('#list_movies').html('<ul>' + titles.join('') + '</ul>');
    },
  });
});