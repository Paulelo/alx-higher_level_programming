#!/usr/bin/node

const process = require('process');
const argv = process.argv;

const x = Number(argv[2]);
if (Number.isFinite(x) !== false) {
  console.log('My number:', (Number(argv[2])));
} else {
  console.log('Not a number');
}
