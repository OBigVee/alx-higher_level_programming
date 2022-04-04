#!/usr/bin/node

const value = require('process');
const args = value.argv;

if (args[2] === undefined) {
    console.log('No argument'); // no args
} else {
    console.log(args[2]);
}