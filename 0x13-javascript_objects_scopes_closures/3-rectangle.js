#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (this.valid(w) && this.valid(h)) {
      this.width = w;
      this.height = h;
    }
  }

  valid (wh) {
    return Number.isInteger(wh) && wh > 0;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
