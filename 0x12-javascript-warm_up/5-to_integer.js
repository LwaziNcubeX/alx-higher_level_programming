#!/usr/bin/node

if (typeof process.argv[2] === 'undefined' || isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ', process.argv[2]);
}
