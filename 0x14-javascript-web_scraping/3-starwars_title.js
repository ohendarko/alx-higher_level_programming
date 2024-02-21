#!/usr/bin/node
const movieId = process.argv[2];
const request = require('request');
const api = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(api, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const resp = JSON.parse(body);
  console.log(resp.title);
});
