#!/usr/bin/node
function add (a, b) {
  const sum = a + b;
  return sum;
}
const myArgs = process.argv.slice(2);
const a = parseInt(myArgs[0]);
const b = parseInt(myArgs[1]);
console.log(add(a, b));
