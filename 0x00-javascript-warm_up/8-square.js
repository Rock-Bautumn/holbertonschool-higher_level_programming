#!/usr/bin/node
const char = 'X';
const myArgs = process.argv.slice(2);
if (isNaN(parseInt(myArgs[0]))) {
  console.log('Missing size');
} else {
  let i = 0;
  const int = parseInt(myArgs[0]);
  while (i < int) {
    console.log(char.repeat(int));
    i++;
  }
}
