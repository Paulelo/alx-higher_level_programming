#!/usr/bin/node
const process = require('process');
const argv = process.argv;

const x = argv.length;
if (x === 2) {
  console.log('No argument');
} else if (x === 3) {
  console.log('Argument found');
} else if (x > 3) {
  console.log('Arguments found');
}
