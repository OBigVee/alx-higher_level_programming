#!/usr/bin/node

/**
 * Script prints the title of a Star Wars movie where the 
 * episode number matches a given integer
 */

const request = require('request');

if (process.argv.length < 2) {
    process.exit();
}
id = process.argv[2];
url = `https://swapi-api.alx-tools.com/api/films/:${id}/`;
request(url, function(err, r, body) {
    if (err) {
        console.log(err);
    } else {
        console.log(JSON.parse(body).title);
    }
})