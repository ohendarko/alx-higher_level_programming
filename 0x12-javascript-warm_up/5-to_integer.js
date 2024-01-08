#!/usr/bin/node

const args = process.argv.slice(2);
const farg = parseInt(args[0]);

if (!isNaN(farg)) {
  console.log('My number:', farg);
} else {
  console.log('Not a number');
}
