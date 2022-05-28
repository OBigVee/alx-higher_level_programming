#!/usr/bin/node
/**
 * Script prints the number of movies where the character "Wedge Antilles" is present
 * -> The first arg is the API URL of the Star Wars API: https://swapi-api.hbtn.io/api/films/
 * -> Wedge Antilles is character ID 18  - your script must use this ID for filtering
 * the result of the API.
 * -> you must use the module request
 */

const request = require("request");
if(process.argv.length > 2){
    const ID = 18;
    const url = process.argv[2]
    request(url,function (error, response, body){
        switch (body) {
            case body:
                const getCharacter = JSON.parse(body).results.filter(
                    i => i.characters.find(j => j.match(/\/people\/18\/?$/))
                );
                console.log(getCharacter.length);
                break;
            case error:
                console.log(error);
                break;
        }
    });
}