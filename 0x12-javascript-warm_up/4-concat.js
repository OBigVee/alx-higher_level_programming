#!/usr/bin/node
/**
 * script prints two arguments passed to it
 */

const value = require('process');
const args = value.argv;

console.log(`${args[2]} is ${args[3]}`);
