#!/usr/bin/node
const fs = require('fs');

// Check the arguments are 3
if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file-path> "string to write"');
  process.exit(1);
}

// Get the file path from command-line arguments
const filePath = process.argv[2];

// Get the string to write
const StrWrite = process.argv[3];

// write the content to the file in utf-8
fs.writeFile(filePath, StrWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
