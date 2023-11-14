#!/usr/bin/node
function add (a, b) {
  const result = a + b;
  console.log(result);
}

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

if (Number.isNaN(a) || Number.isNaN(b)) {
  console.log('NaN');
} else {
  add(a, b);
}
