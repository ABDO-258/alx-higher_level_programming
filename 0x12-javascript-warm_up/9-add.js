#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const myArg1 = parseInt(process.argv[2]);
const myArg2 = parseInt(process.argv[3]);
add(myArg1, myArg2);
