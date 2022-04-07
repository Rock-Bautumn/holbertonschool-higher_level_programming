#!/usr/bin/node
const fs = require('fs');
const myArgs = process.argv.slice(2);
const filename = myArgs[0];
const content = myArgs.slice(1).join(' ');

fs.writeFile(filename, content, err => {
  if (err) {
    console.error(err);
  }
});
