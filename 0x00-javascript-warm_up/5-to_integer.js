#!/usr/bin/node
const myArgs = process.argv.slice(2);
const myVar = parseInt(myArgs[0]);
if (isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myVar}`);
}
