#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  // method
  //charPrint (c) {
    //for (let i = 0; i < this.size; i++) {
      //if (!c) {
        //console.log('X');
      //} else {
        //console.log('c');
      //}
    //}
  //}
  charPrint (c) {
    if (!c) {
      for (let i =0; i < this.size; i++) {
         console.log('X');
      }
    } else {
       this.print(c);
    }
  }
};
