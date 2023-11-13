#!/usr/bin/node

const process = require('node:process');

const arg = process.argv[2];

if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (arg > process.argv[1]) {
  console.log('Arguments found');
}
