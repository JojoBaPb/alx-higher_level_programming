#!/usr/bin/node
let myObject = {
  type: 'object',
  val: 12
};
console.log(myObject);

myObject.incr = function () {
  this.val++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
