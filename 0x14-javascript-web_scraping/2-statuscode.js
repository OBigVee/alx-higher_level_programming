#!/usr/bin/node

/**
 * script displays the status code of a GET request
 */

const request = require('request');

if (process.argv.length < 3) {
    process.exit();
}

url = process.argv[2];
request.get(url).on('response', r => {
    console.log(`code:${r.statusCode}`)
})