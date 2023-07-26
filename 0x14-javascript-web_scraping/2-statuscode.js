#!/usr/bin/node

/**
 * script
 */

const request = require('request');

if (process.argv.length !== 3) {
    process.exit();
}
const url = process.argv[2];
request(url, function(error, res, body) {
    if (error) {
        console.log(error);
    }
    console.log(`code: ${res.statusCode}`);
});