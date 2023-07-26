#!/usr/bin/node

/**
 * script reads and prints the content of a file.
 * the 1st argument is the file ath
 * the content of the file must be read in utf-8
 * if an error occurred during the reading, print the error object
 */
const fs = require('fs');

if (process.argv.length > 2) {
  fs.readFile(process.argv[2]),
  (error, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data.toString('utf-8'));
    }
  };
}
