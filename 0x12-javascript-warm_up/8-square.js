#!/usr/bin/node
const arg = process.argv[2];
let i = 0;

if (!parseInt(arg)) {
  console.log('Missing size');
}

while (i < arg) {
  let j = 0;
  let row = '';

  while (j < arg) {
    row += 'X';
    j++;
  }

  console.log(row);
  i++;
}
