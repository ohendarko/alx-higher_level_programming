function loadDoc() {
  $('#character').load('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (response, status, xhr) {
      var data = JSON.parse(response)
      $('#character').text(data.name);
    });
}
loadDoc();