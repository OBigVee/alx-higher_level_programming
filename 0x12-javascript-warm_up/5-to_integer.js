#!/usr/bin/node
/**
 * script prints
 * My number :<first argument converted in integer>
 * if the first argument can be converted to an integer
 */
const values = parseInt(process.argv.slice(2));

if (!isNaN(values)) {
  console.log(`My number: ${values}`);
} else {
  console.log('Not a member');
}
