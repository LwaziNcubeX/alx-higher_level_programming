#!/usr/bin/node
// A script that display the status code of a GET request.
const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
