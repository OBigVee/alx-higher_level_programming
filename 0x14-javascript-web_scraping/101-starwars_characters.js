#!/usr/bin/node
/**
 * Script prints all chracters of a Start Wars movie:
 * -> The first arg is the movie ID -example: 3 = "Return of the Jedi"
 * -> Display one character name by line in the same order of the list "characters" in the /films/ response
 * -> you must use the Star Wars API
 * -> You must use the module request
 */
const request = require('request')

const url = 'https://swapi-api.hbtn.io/api/films/'

if (process.argv.length > 2) {
    const episodeID = process.argv[2]
    request(`${url}${episodeID}`, function (error, response, body) {
        if (error) throw error
        const charactersURL = JSON.parse(body).characters;
        const charactersName = charactersURL.map(
            url => new Promise((resolve, reject) => {
                request(url, (err, res, body) => {
                    if (err) {
                        reject(err);
                    }
                    resolve(JSON.parse(body).name);
                });
            }));

        Promise.all(charactersName)
            .then(names => console.log(names.join('\n')))
            .catch(err => console.log(err));
    });
    //     else if (body) {
    //         const charURL = JSON.parse(body).characters;
    //         //console.log(charURL);
    //         const charName = charURL.map(
    //             eachUrl => new Promise((resolve, reject)=>{
    //                 request(eachUrl,function (err, response, body){
    //                     if(err) throw reject(err);
    //                     resolve(JSON.parse(body).name);
    //                     //console.log(resolve(JSON.parse(body).name));
    //                 });
    //             }));
    //         console.log(charName);
    //         Promise.all(charName)
    //             .then(names => console.log(names.join("\n")))
    //             .then(error => console.log(error))
    //     }
    // })
}
