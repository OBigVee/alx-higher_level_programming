#!/usr/bin/node
/**
 * Script that computes the number of tasks completed by user id::
 *  -> The first argument is the API URL:  https://jsonplaceholder.typicode.com/todos
 *  -> Only print users with completed task
 *  -> you must use the module request
 */

const request = require('request')
if (process.argv.length > 2) {
  const url = process.argv[2]
  const obj = {}
  request(url, function (err, resp, body) {
    switch (body) {
      case err:
        console.log(err)
        break
      case body:
        JSON.parse(body).forEach(person => {
          if (person.completed) {
            if (!obj[person.userId]) {
              obj[person.userId] = 0
            }
            obj[person.userId]++
          }
        })
        console.log(obj)
        break
    }
  })
}
