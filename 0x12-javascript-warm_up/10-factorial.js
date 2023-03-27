#!/usr/bin/node

const process = require('process');
const argv = process.argv;

function factorial (num) {
  const x = Number(num);
  if (x === 0) {
    return 1;
  } else if (Number.isFinite(x) === false) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const x = factorial(Number(argv[2]));
console.log(x);
