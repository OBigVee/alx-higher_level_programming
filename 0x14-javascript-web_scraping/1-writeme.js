#!/usr/bin/node

/**
 * script writes a string to a file
 *
 */

const fs = require('fs');

if (process.argv.length !== 4) {
  process.exit();
}
const [path, data] = process.argv.slice(2);

fs.writeFile(path, data, (err) => {
  if (err) {
    console.log(err);
  }
});
