#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (this.valid(w) && this.valid(h)) {
      this.width = w;
      this.height = h;
    }
  }

  valid(wh) {
    return Number.isInteger(wh) && wh > 0;
  }
}

module.exports = Rectangle;
