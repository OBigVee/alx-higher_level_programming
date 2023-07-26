#!/usr/bin/node

/**
 * script
 */

const request = require('request');

if (process.argv.length !== 3) {
    process.exit();
}

request(process.argv[2], function(error, response, body) {
    if (error) {
        console.log(error);
    }
    console.log(`code: ${response.statusCode}`);
});