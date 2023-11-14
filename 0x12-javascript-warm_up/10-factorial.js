#!/usr/bin/node
function Factorial (n) {
  if (n === 0) {
    return (1);
  } else {
    return (n * Factorial(n - 1));
  }
}

if (process.argv[2]) {
  const myArg1 = parseInt(process.argv[2]);
  const result = Factorial(myArg1);
  console.log(result);
} else {
  console.log(Factorial(0));
}
