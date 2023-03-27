#!/usr/bin/node

const process = require('process');
const argv = process.argv;

const x = Number(argv[2]);
if (Number.isFinite(x) !== false) {
  let y = 0;
  while (y < x) {
    console.log('C is fun');
    y++;
  }
} else {
  console.log('Missing number of occurences');
}
