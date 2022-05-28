#!/usr/bin/node
/**
 * Script that display the status code of a GET request
 * The first arg is the url to the request (GET)
 * the status code must be printed like this : code: <status code>
 *     must use the module request
 */

const request = require('request')
if (process.argv.length > 2) {
  request.get(process.argv[2]).on('response', r => {
    console.log(`code: ${r.statusCode}`)
  })
}
