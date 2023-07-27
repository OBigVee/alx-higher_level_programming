#!/usr/bin/node

/**
 * Script prints all character of a Star wars movie
 */

const request = require('request');

if (process.argv.length !== 3) {
    process.exit()
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const arr = [];
request(url, function(err, res, body) {
    if (err) {
        console.log(err);
    }
    if (res.statusCode === 200) {
        const data = JSON.parse(body);
        for (const char of data.characters) {
            request(char, function(err, res, body) {
                if (err) {
                    console.log(err);
                } else if (res.statusCode === 200) {
                    const name = JSON.parse(body);
                    console.log(name.name);
                    arr.push(name.name);
                }
            });
        }
    }
    console.log(arr);
});