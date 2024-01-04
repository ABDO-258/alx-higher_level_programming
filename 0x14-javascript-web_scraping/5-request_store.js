#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Check the arguments are 3
if (process.argv.length !== 4) {
  console.error('Usage: node 5-request_store.js <URL> <file path>');
  process.exit(1);
}

// Get the url from command-line arguments
const WebUrl = process.argv[2];
// Get the file path from command-line arguments
const filePath = process.argv[3];
// make a request to url
request.get(WebUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // write the content to the file in utf-8
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
