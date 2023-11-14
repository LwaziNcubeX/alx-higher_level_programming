#!/usr/bin/node
let x = 0;
const arg = process.argv[2];

if (!parseInt(arg)) {
  console.log('Missing number of occurrences');
}

while (x < process.argv[2]) {
  console.log('C is fun');
  x++;
}
