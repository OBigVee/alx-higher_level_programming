#!/usr/bin/node

const args = require("process").argv;
const vals = parseInt(args[2]);
if (!isNaN(vals)) {
    console.log('My number: ' + vals);
} else {
    console.log('Not a number');
}