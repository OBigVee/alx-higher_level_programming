#!/usr/bin/node

const vals = parseInt(process.argv.slice(2));

if (vals) {
  console.log(`My number: ${vals}`);
} else {
  console.log('Not a number');
}
