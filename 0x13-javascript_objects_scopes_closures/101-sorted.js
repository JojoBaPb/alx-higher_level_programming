#!/usr/bin/node
const dict = require('./101-data').dict;
const NewDiction = {};

Object.keys(dict).map(function (key, index) {
  if (NewDiction[dict[key]] === undefined) {
    NewDiction[dict[key]] = [];
  }
  NewDiction[dict[key]].push(key);
});

console.log(NewDiction);
