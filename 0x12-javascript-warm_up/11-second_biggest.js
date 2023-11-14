#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let index;
  const myArr = [];
  for (index = 2; index < process.argv.length; index++) {
    myArr.push(parseInt(process.argv[index]));
  }
  myArr.sort(function (a, b) {
    return b - a;
  });
  console.log(myArr[1]);
}
