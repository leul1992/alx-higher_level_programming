#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (num && num >= 1) {
  let number = 1;
  for (let i = 1; i <= num; i++) {
    number *= i;
  }
  console.log(number);
} else {
  console.log(1);
}
