#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (isNaN(parseInt(myArgs[0]))) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  const int = parseInt(myArgs[0]);
  while (i < int) {
    console.log('C is fun');
    i++;
  }
}
