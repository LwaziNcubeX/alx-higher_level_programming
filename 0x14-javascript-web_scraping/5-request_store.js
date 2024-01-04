#!/usr/bin/node
// A script that writes a string to a file.
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeErr) => {
      if (writeErr) {
        console.error('Error writing to file:', writeErr);
      }
    });
  }
});
