#!/usr/bin/node

const args = process.argv.slice(2);
const concat = [];
let i;
for (i = 0; i < 2; i++) {
  if (args[i] === undefined) {
    concat[i] = 'undefined';
  } else {
    concat[i] = args[i];
  }
}
console.log(concat[0] + ' is ' + concat[1]);
