#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getActors (characters, index) {
  request(characters[index], (err, response, body) => {
    if (err) {
      console.error(err);
    } else {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        getActors(characters, index + 1);
      }
    }
  });
}

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    getActors(characters, 0);
  }
});
