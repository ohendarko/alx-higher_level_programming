#!/usr/bin/node
const args = process.argv;
const reqURL = args[2];
const request = require('request');
request(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
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
