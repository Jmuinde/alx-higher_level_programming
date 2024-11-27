#!/usr/bin/node
const myArgs = process.argv.slice(2);
function add(a, b) {
  if (myArgs.length === 0 || myArgs.length === 1) {
  console.log('NaN');
} else {
    a = Number(myArgs[0]);
    b = Number(myArgs[1]);
    result = a + b;
    console.log(result);
}
}
add();
