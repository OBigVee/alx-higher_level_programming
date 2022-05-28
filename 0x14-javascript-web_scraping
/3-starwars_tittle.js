#!/usr/bin/node
/**
 * Script prints the tittle of a Star Wars movie where the episode
 * number matches a given integer:
 *  The first argument is the movie ID
 *  must use the star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
 * You must use the module request
 * ------request Module (how to use it)-----------
 * https://github.com/request/request#:~:text=const%20request%20%3D%20require,homepage.%0A%7D)%3B
 *
 */

const request = require('request');

if (process.argv.length > 2){
    const id = process.argv[2];
    request(`https://swapi-api.hbtn.io/api/films/${id}/` ,function (error, response, body){
        if(error){
            console.log(error);
        }else{
            console.log(JSON.parse(body).title);
        }

    })
}