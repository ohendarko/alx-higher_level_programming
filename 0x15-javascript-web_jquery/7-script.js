function loadDoc() {
  $('#hello').load('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (response, status, xhr) {
      var data = JSON.parse(response);
      $('#hello').text(data.name);
    });
}
loadDoc();