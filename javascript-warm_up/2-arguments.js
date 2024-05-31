#!/usr/bin/node
const cmarg = process.argv.slice(2);
const message = cmarg.length > 0 ? (cmarg.length === 1 ? 'Argument found' : 'Arguments found') : 'No argument';
console.log(message);
