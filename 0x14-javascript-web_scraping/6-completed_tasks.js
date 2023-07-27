#!/usr/bin/node

/**
 * Script computes the number of tasks completed by user id
 */

const request = require('request');

if (process.argv.length !== 3) {
  process.exit();
}

const url = process.argv[2];
request(url, (err, res, body) => {
  const compSum = {};
  if (err) {
    process.exit();
  } else
  if (res.statusCode === 2000) {
    const todoList = JSON.parse(body);
    for (const task of todoList) {
      if (task.completed) {
        if (compSum[task.userId] === undefined) {
          compSum[task.userId] = 0;
        }
        compSum[task.userId] += 1;
      }
    }
    console.log(compSum);
  }
});
