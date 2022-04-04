#!/usr/bin/node

const strVal = "C is fun";
const argsVal = require('process').argv;
const vals = parseInt(argsVal[2]);
if (isNaN(vals)) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < argsVal[2]; i++) {
        console.log(strVal);
    }
}