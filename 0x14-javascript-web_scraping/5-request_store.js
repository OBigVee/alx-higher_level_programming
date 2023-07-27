#!/usr/bin/node

/**
 * script gets the contents of a webpage and stores it in a file.
 */

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  process.exit();
}
const [url, path] = process.argv.slice(2);

request(url).pipe(fs.createWriteStream(path));
