#!/usr/bin/node

/**
 * script  prints the number of movies where the character
 *  “Wedge Antilles” is present.
 */

const request = require('request');

if (process.argv.length !== 3) {
  process.exit();
}
const id = 18;
const url = process.argv[2];
request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
    process.exit();
  } else if (resp.statusCode !== 200) {
    process.exit();
  }

  let track = 0;
  const res = JSON.parse(body);
  const results = res.results;
  for (const obj of results) {
    for (const char of obj.characters) {
      if (char.indexOf(id) !== -1) {
        track++;
      }
    }
  }
  console.log(track);
});
