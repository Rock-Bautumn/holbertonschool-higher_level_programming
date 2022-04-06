#!/usr/bin/node
const middleSquare = require('./5-square');

module.exports = class Square extends middleSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let thischar = 'X';
    if (c) {
      thischar = c;
    }
    let i = 0;
    while (i < this.width) {
      console.log(thischar.repeat(this.width));
      i++;
    }
  }
};
