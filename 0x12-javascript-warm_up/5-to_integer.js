#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length === 0) {
  console.log('Not a number');
} else if (isNaN(Number(myArgs[0]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.floor(Number(myArgs[0])));
}
