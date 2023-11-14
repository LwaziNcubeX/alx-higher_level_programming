#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
const sortedArgs = args.sort((a, b) => b - a);
const secondLargest = sortedArgs[1] || 0;
console.log(secondLargest);
