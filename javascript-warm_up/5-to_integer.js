#!/opt/homebrew/bin/node
const process = require('process');

if (parseInt(process.argv[2])) {
  console.log('My number: ' + Math.floor(process.argv[2]));
} else {
  console.log('Not a number');
}
