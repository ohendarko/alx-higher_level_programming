#!/usr/bin/node

const argvs = process.argv.slice(2);

if (argvs.length === 0) {
  console.log('No Argument');
} else if (argvs.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
