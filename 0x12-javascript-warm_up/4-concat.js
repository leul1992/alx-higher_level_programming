#!/usr/bin/node
const v = 'undefined';
if (!process.argv[2]) {
  console.log(v + ' is ' + v);
} else if (!process.argv[3]) {
  console.log(process.argv[2] + ' is ' + v);
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
