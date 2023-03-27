#!/usr/bin/node

const process = require('process');
const argv = process.argv;

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
  return;
}

let x = 2;
let z = 0;
const y = [];
//Storing args in array 'y'
while (argv[x]) {
  y[z] = Number(argv[x]);
  x++;
  z++;
}
//console.log(y);

let i;
const len = y.length;
//console.log('Length of arr is:', len);
let h;
let j;
//console.log(len);
//Searching for the highest of all arguments
for (i = 0; i < len; i++) {
  h = y[i];
  for (j = 0; j < len; j++) {
    if (Number(y[j]) > h) {
      h = Number(y[j]);
    }
  }
}

//Serching 2nd before highest of all arguments
let n;
let s;
for (n = 0; n < len; n++) {
  if (Number(y[n]) != h) {
    s = y[n];
  }
  let m;
  for (m = 0; m < len; m++) {
    if ((Number(y[m]) > s) & (Number(y[m]) != h)) {
      s = Number(y[m]);
    }
  }
}
//console.log(h);
console.log(s);
  
