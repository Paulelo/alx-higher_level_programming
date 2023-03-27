#!/usr/bin/node
const process = require('process');
const argv = process.argv;

let x = 0;
while (argv[x]) {
  x++;
}
if (x === 2) {
  console.log('No argument');
} else {
  let y = 2;
  while (argv[y]) {
    console.log(argv[y]);
    y++;
  }
}
