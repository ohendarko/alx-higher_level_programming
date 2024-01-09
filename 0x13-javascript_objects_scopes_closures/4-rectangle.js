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

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
