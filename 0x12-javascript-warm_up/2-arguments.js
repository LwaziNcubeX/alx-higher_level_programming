#!/usr/bin/node

const argsLen = process.argv.length;

console.log(argsLen === 2 ? 'Argument found' : argsLen > 2 ? 'Arguments found' : 'No argument');
