#!/usr/bin/node

const args = process.argv.slice(2);
const rep = parseInt(args[0]);
let i;

if (isNaN(rep)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < rep; i++) {
    console.log('C is fun');
  }
}
