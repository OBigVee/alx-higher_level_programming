#!/usr/bin/node
/**
 * nbOccurence returns the number of occurrences in a list
 * @param list
 * @param searchElement
 * @returns {number}
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1
    }
  }
  return count
}
