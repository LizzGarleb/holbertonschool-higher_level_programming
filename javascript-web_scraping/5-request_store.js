#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, (err, response, body) => {
  if (err) throw err;
  else {
    const content = body;
    fs.writeFile(filePath, content, 'utf-8', (err) => {
      if (err) throw err;
    });
  }
});
