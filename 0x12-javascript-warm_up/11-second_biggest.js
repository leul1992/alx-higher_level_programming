#!/usr/bin/node
let num = process.argv;
num = num.map(val => parseInt(val));
num.sort((a, b) => a - b);
console.log(num[num.length - 2] || 0);
