#!/usr/bin/node
const request = require('request');

// Check the arguments are 3
if (process.argv.length !== 3) {
  console.error('Usage: node 3-starwars_title.js <id>');
  process.exit(1);
}

// Get the url from command-line arguments
const id = process.argv[2];
const urlMovie = `https://swapi-api.alx-tools.com/api/films/${id}`;

// make a request to url
request.get(urlMovie, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const Data = JSON.parse(body);
    console.log(Data.title);
  }
});
