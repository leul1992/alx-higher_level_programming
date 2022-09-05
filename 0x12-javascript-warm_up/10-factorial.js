#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (num && num >= 1) {
  let number = 1;
  for (let i = 2; i <= num; i++) {
    number *= i;
  }
  console.log(number);
} else {
  console.log(1);
}
