#!/usr/bin/node
const num1 = process.argv[2];
const num2 = process.argv[3];

if (num1 === 'undefined' || num2 === 'undefined') {
  console.log(NaN);
} else {
  console.log(parseInt(num1) + parseInt(num2));
}
