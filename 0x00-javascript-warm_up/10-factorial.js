#!/usr/bin/node
function factorial (num) {
  if ((num === 0) || (isNaN(num))) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const myArgs = process.argv.slice(2);
const myNum = parseInt(myArgs[0]);
console.log(factorial(myNum));
