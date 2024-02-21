#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;
request(url, (err, response, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (err, response, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
