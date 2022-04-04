#!/usr/bin/node
 // script prints square
const args = require('process').argv;
const strVal = "X";
const size = parseInt(args[2]);
if (isNaN(size)) {
    console.log('Missing size');
} else {
    for (let i = 0; i < size; i++) {
        console.log(strVal.repeat(size));
    }
}