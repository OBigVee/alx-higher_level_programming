#!/usr/bin/node

const args = require('process').argv;
let bigVal = 0;
let valList = args.slice(2);
if (valList.length > 1) {
    valList.sort();
    bigVal = valList[valList.length - 2];
}
console.log(bigVal);