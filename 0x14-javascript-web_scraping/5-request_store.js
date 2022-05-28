#!/usr/bin/node
/**
 * Script gets the contents of a webpage and stores it in a file
 * -> The first argument is the URL to request
 * -> The second arg is the file path to store the body response
 * -> the file must be UTF-8 encoded
 * -> You must use the module request
 */

const request = require('request')
const fs = require('fs')

const encode = 'utf-8'

if (process.argv.length > 3) {
  const url = process.argv[2]
  const pathToStoreTo = process.argv[3]
  request(url, function (error, response, body) {
    if (error) throw error
    else if (body) {
      fs.writeFile(pathToStoreTo, body, encode, err => {
        if (err) throw err
      })
    }
  })
}
