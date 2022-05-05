#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w
      this.height = h
    }
  }

  print () {
    /**
         * prints the rectangle using the character X
         */
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width))
    }
  }

  rotate () {
    /**
         * exchange width and height of the rectangle
         */
    // console.log(`before rotation:: this.height = ${this.height} and this.width = ${this.width}`);
    // [this.height, this.width] = [this.width, this.height]
    const placeHolder = this.width
    this.width = this.height
    this.height = placeHolder
    // console.log(`After rotation:: this.height = ${this.height} and this.width = ${this.width}`);
  }

  double () {
    /**
         * multiplies width and height of rectangle by 2
         */
    this.height = this.height * 2
    this.width = this.width * 2
  }
}
