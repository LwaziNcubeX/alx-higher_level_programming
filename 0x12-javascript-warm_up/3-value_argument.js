#!/usr/bin/node
const process = require('node:process');

if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (process.argv[2] > process.argv[1]) {
  console.log(process.argv[2]);
}
