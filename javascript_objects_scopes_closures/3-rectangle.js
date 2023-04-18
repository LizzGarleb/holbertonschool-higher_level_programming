#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
            // empty object
        } else {
            this.width = w;
            this.height = h;
        }
    }
    print () {
        let rect_print = ''
        for (let i = 0; i < this.width; i++) {
            rect_print += 'X';
        }
        for (let i = 0; i < this.height; i++) {
            console.log(rect_print);
        }
    }
}

module.exports = Rectangle;
