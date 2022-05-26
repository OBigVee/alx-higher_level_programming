#!/usr/bin/node
/**
 * script that imports a dictionary of occurrences by user id and computes a dictionary
 * of user ids by occurrence.
 * -----------
 *  import dict from the file 101-data.js
 *  In the new dictionary:
 *
 *     A key is a number of occurrences
 *     A value is the list of user ids
 *
 * Print the new dictionary at the end
 */
const dict = require('./101-data').dict
const sortDict = {}
Object.getOwnPropertyNames(dict).forEach(key => {
  // if a key doesn't have a value
  if (sortDict[dict[key]] === undefined) {
    // create and empty list
    sortDict[dict[key]] = [key]
  }
  sortDict[dict[key]].push(key)
})

console.log(sortDict)
