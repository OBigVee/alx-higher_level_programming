#!/usr/bin/node

/**
 * Script prints all characters of a star Wars Movie:
 * -> The first arg is the Movie ID - example 3 = "Return of the jedi"
 * -> display on character name by line
 * you mut use the star wars api
 * you must use the module request
 */
const request = require('request')

const url = 'https://swapi-api.hbtn.io/api/films/'

if (process.argv.length > 2) {
  const episodeID = process.argv[2]
  request(`${url}${episodeID}`, function (error, response, body) {
    if (error) throw error
    else if (body) {
      JSON.parse(body).characters.forEach(eachCharacter => {
        request(eachCharacter, function (err, resp, body) {
          if (err) throw err
          console.log(JSON.parse(body).name)
        })
      })
    }
  })
}
