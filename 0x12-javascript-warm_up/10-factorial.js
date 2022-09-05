#!/usr/bin/node
function factorial (number) {
  if (number === 1 || isNaN(number)) { return 1; } else { return number * factorial(number - 1); }
}
const num = parseInt(process.argv[2]);
console.log(factorial(num));
