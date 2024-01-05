#!/usr/bin/node
const request = require('request');

// Check the arguments are 3
if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <API-URL>');
  process.exit(1);
}

// Get the url from command-line arguments
const urlApi = process.argv[2];

// make a request to url
request.get(urlApi, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const Datas = JSON.parse(body);
    const completedTasksByUser = {};
    Datas.forEach((Data) => {
      if (Data.completed) {
        if (completedTasksByUser[Data.userId] === undefined) {
          completedTasksByUser[Data.userId] = 1;
        } else {
          completedTasksByUser[Data.userId]++;
        }
      }
    });
  }
});
