#!/usr/bin/node

const process = require('process');
const argv = process.argv;

const x = Number(argv[2]);
if (Number.isFinite(x) !== false) {
  let i = 0;
  const myArr = [];
  while (i < x) {
    myArr[i] = 'X';
    i++;
  }
  for (i = 0; i < x; i++) {
    console.log(myArr.join(''));
  }
} else {
  console.log('Missing size');
}
