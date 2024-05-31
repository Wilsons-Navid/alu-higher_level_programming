#!/usr/bin/node
const cmarg = process.argv.slice(2);
const message = cmarg[0] ? cmarg[0] : 'No argument';
console.log(message);
