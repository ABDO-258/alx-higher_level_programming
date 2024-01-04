#!/usr/bin/node
const request = require('request');

// Check the arguments are 3
if (process.argv.length !== 3) {
  console.error('Usage: node 2-statuscode.js <URL>');
  process.exit(1);
}

// Get the url from command-line arguments
const url = process.argv[2];

// make a request to url
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
