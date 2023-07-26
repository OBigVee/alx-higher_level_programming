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

request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
    process.exit();
  }
  const data = JSON.parse.body();
  fs.writeFileSync(path, data, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
