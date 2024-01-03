#!/usr/bin/node
// A script that writes a string to a file.
const fs = require('fs');

const filePath = process.argv[2];
const string = process.argv[3];

if (!filePath || !string) {
  console.error('Usage: ./1-writeme.js <file-path> <string>');
  process.exit(1);
}

fs.writeFile(filePath, string, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
