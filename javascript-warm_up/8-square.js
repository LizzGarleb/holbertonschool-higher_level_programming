#!/usr/bin/node
const num = process.argv[2];

if (isNaN(num)) {
  console.log('Missing size');
} else {
  let letter = 'X';
  for (let i = 1; i < num; i++) {
    letter += 'X';
  }
  for (let i = 0; i < num; i++) {
    console.log(letter);
  }
}
