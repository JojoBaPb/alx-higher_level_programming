#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map(function (nm, index) {
  return nm * index;
});

console.log(list);
console.log(newList);
