#!/usr/bin/node
/**
 * script prints the first argument passed to it
 */
const value = require('process');
const args = value.argv;

if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
