#!/usr/bin/node
const myIndex = parseInt(process.argv[2]);
const myVar = 'X';
let index;
if (!isNaN(myIndex) && Number.isInteger(myIndex)) {
  for (index = 0; index < myIndex; index++) {
    console.log(myVar.repeat(myIndex));
  }
} else {
  console.log('Missing size');
}
