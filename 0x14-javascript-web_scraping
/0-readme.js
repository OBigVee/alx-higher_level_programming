#!/usr/bin/node
/**
 * Scripts reads and prints the content of a file.
 * The first argument is the file path
 * the content of the file must be read in utf-8
 * if an error occurred during the reading, print the error object
 */

const fs = require("fs")

if(process.argv.length > 2){
    fs.readFile(process.argv[2], (err,data) => {
        if(err){
            console.log(err);
        }else{
            console.log(data.toString("utf-8"));
        }
    });
}