#!/usr/bin/node
 //script prints the addition of  2 ints

function add(a, b) {
    const args = require('process').argv;
    a = parseInt(args[2]);
    b = parseInt(args[3]);
    console.log(a + b);
}
add();