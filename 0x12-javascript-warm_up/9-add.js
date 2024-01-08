#!/usr/bin/node

const args = process.argv.slice(2);

function add (a, b) {
  a = parseInt(args[0]);
  b = parseInt(args[1]);
  return a + b;
}
const res = add();
console.log(res);
