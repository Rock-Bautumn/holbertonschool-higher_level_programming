#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length === 0) {
  console.log('0');
} else if (myArgs.length === 1) {
  console.log('0');
} else {
  const sortedArgs = myArgs.sort(function (a, b) { return b - a; });
  console.log(sortedArgs[1]);
}
