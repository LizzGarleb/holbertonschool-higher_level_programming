#!/usr/bin/node
const arg = process.argv;

if (arg[2] === undefined || arg.length === 3) {
  console.log(0);
} else {
  let max = Number.MIN_SAFE_INTEGER;
  let secondMax = Number.MIN_SAFE_INTEGER;
  let i = 2;
  while (i < arg.length) {
    const num = parseInt(arg[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num !== max) {
      secondMax = num;
    }
    i++;
  }
  console.log(secondMax);
}
