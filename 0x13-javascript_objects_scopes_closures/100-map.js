#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const newArray = list.map((value, index) => value * index);
console.log(newArray);
