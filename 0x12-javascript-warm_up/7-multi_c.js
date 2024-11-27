#!/usr/bin/node
const myArray = process.argv.slice(2);
if (myArray.length === 0 || isNaN(Number(myArray[0]))) {
  console.log('Missing number of occurences');
} else {
  const x = Number(myArray[0]);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
