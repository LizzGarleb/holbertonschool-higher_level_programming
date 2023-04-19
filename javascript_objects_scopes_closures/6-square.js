#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let rect = '';
    for (let i = 0; i < this.width; i++) {
      rect += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(rect);
    }
  }
}

module.exports = Square;
