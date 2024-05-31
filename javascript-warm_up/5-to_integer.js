#!/usr/bin/node
const cmarg = process.argv.slice(2);
console.log(parseInt(cmarg[0]) ? `My number: ${parseInt(cmarg[0])}` : 'Not a number');
