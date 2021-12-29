#!/usr/bin/node
const arguments = process.argv.length -2 ;
if(arguments === 0){
	console.log("No arguments");
}
else if(arguments === 1){
	console.log("Argument found");
}
else if(arguments > 1){
	console.log("Arguments found");
}
