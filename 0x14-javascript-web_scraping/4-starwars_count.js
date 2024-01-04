#!/usr/bin/node
const request = require('request');

// Check the arguments are 3
if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <API-URL>');
  process.exit(1);
}

// Get the url from command-line arguments
const urlApi = process.argv[2];

// make a request to url
request.get(urlApi, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const Data = JSON.parse(body);
    const filmsWithWedge = Data.results.filter((film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );

    // Print the number of movies with Wedge Antilles
    console.log(filmsWithWedge.length);
  }
});
