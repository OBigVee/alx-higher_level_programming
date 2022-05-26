#!/usr/bin/node
/**
 * scripts import list from 100-data.js
 * creates a new list with each value equal to the value of the
 * initial list, multiplied by the indexed in the list
 * print both the initial and new list.
 */
const list = require('./100-data').list
const newList = list.map(function (val, idx) { return val * idx })
console.log(list)
console.log(newList)
