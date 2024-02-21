#!/usr/bin/node
const url = process.argv[2];
const storagePath = process.argv[3];
const request = require('request');
const path = require('path');
const fs = require('fs');
const directory = path.dirname(storagePath);

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }

  fs.mkdir(directory, { recursive: true }, (err) => {
    if (err) {
      console.error(err);
    }
    fs.writeFile(storagePath, body, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
