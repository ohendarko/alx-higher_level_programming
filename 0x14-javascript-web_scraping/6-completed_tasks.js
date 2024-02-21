#!/usr/bin/node
const args = process.argv;
const reqURL = args[2];
const request = require('request');
request(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const resp = JSON.parse(body);
    const dash = {};
    for (let i = 0; i < resp.length; i++) {
      const comp_task = (resp[i].completed);
      const key = resp[i].userId.toString();
      if (comp_task) {
        if (dash[key]) {
          dash[key]++;
        } else {
          dash[key] = 1;
        }
      }
    }
    console.log(dash);
  }
});
