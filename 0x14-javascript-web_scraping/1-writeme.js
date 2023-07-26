#!/usr/bin/node

/**
 * script writes a string to a file
 *
 */

const fs = require('fs');
const { encode } = require('punycode');

if (process.argv < 3) {
    process.exit();
}
file = process.argv[2];
data = process.argv[3];

fs.writeFile(file, data, (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log(fs.readFileSync(file, 'utf-8'))
    }
})