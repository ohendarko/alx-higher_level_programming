#!/usr/bin/node
const api = process.argv[2];
const request = require('request');

request.get(api, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const resp = JSON.parse(body);
  let films = 0;

  // Iterate through each result in the results array
  resp.results.forEach(result => {
    // Iterate through each character URL in the characters array
    result.characters.forEach(character => {
      // Check if the character URL matches the specified URL
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        // Increment the films counter if the character appears in a film
        films++;
      }
    });
  });
  console.log(films);
});
