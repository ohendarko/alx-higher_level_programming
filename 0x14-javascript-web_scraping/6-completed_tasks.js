#!/usr/bin/node
const api = process.argv[2];
const request = require('request');
request(api, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const resp = JSON.parse(body);
    const done = {};
    for (let i = 0; i < resp.length; i++) {
      const compTask = (resp[i].completed);
      const comp = resp[i].userId.toString();
      if (compTask) {
        if (done[comp]) {
          done[comp]++;
        } else {
          done[comp] = 1;
        }
      }
    }
    console.log(done);
  }
});
