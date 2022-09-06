#!/usr/bin/node
let list = require('./100-data').list;
console.log(list);
list = list.map((li, index, list) => li * index);
console.log(list);
