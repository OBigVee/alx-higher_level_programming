#!/usr/bin/node
/**
 * function prints the number of arguments already printed and the
 * new argument value
 * @type {number}
 */
let count = 0
exports.logMe = function (item) {
  console.log(`${count}: ${item}`)
  count += 1
}
