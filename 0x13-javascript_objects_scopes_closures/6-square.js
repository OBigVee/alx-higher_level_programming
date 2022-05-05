#!/usr/bin/node

const square = require("./5-square");
module.exports = class Square extends square {

    constructor(size) {
        super(size, size);
    }
    charPrint(c) {
        this.print(c);
    }

}