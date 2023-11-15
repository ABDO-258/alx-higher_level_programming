#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      const rep2 = 'C';
      for (let i = 0; i < this.height; i++) {
        console.log(rep2.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
