#!/usr/bin/node
const api = process.argv[2];
const request = require('request');

request.get(api, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const resp = JSON.parse(body);

  const compTask = {};

  resp.forEach(resp => {
    if (resp.completed) {
      compTask[resp.userId] = (compTask[resp.userId] || 0) + 1;
    }
  });
  for (const userId in compTask) {
    if (userId === '1') {
      console.log(`{ '${userId}': ${compTask[userId]},`);
    } else if (userId === '10') {
      console.log(`'${userId}': ${compTask[userId]} }`);
    } else {
      console.log(`'${userId}': ${compTask[userId]},`);
    }
  }
});
