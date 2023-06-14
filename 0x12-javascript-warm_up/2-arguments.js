#!/usr/bin/node
/**
 * Script prints a message depending
 * of the number of arguments passed
 */

const argv = process.argv.slice(2);

if (argv[1] === null) {
  console.log('No argument');
} else if (argv.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
