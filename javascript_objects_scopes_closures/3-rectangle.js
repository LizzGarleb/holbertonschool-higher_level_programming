#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      // empty object
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';
    for (let i = 0; i < this.width; i++) {
      rect += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(rect);
    }
  }
}

module.exports = Rectangle;
