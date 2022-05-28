#!/usr/bin/node
/**
 * Script writes a string to a file:
 * The first arg is the file path
 * The second arg is the string to write
 * The content of the file must be written in utf-8
 * if an error occurred during while writing, print the error object
 *
 */
const fs = require('fs')

if (process.argv.length > 3) {
  const path = process.argv[2]
  const data = process.argv[3]
  fs.writeFile(path, data, 'utf-8', (err) => {
    if (err) {
      throw err
    }
  })
}
