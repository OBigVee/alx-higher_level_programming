#!/usr/bin/node

const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    let char = 'X';

    if (c) {
      char = c;
    }
    for (let i = 1; i <= this.size; i++) { console.log(char.repeat(this.size)); }
  }
};
