#!/usr/bin/node

/**
 * Script prints the title of a Star Wars movie where the 
 * episode number matches a given integer
 */

const request = require('request');
if (process.argv < 2) {
    process.exit();
}
id = process.argv[2];
url = `https://swapi-api.alx-tools.com/api/films/:${id}`;
request.get(url).on('response ', r => {
    console.log(r.title);
})