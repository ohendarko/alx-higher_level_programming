#!/usr/bin/node

const args = process.argv.slice(2);
const rep = parseInt(args[0]);
let i, j;

if (isNaN(rep)) {
  console.log('Missing size');
} else {
  for (i = 0; i < rep; i++) {
    let row = '';
    for (j = 0; j < rep; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
