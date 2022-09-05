#!/usr/bin/node
const rep = parseInt(process.argv[2]);
if (rep) {
  for (let i = 0; i < rep; i++) {
    let str = '';
    for (let j = 0; j < rep; j++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
