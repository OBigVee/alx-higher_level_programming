#!/usr/bin/node
/**
 * script prints
 * My number :<first argument converted in integer>
 * if the first argument can be converted to an integer
 */
const args = require('process').argv;
const values = parseInt(args[2]);

if (!isNaN(values)) {
  console.log(`My number: ${Number(values)}`);
} else {
  console.log('Not a member');
}
