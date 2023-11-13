#!/usr/bin/node
const myIndex = parseInt(process.argv[2]);
const myVar = 'C is fun';
let index;
if (!isNaN(myIndex) && Number.isInteger(myIndex)) {
  for (index = 0; index < myIndex; index++) {
    console.log(myVar);
  }
} else {
  console.log('Missing number of occurrences');
}
