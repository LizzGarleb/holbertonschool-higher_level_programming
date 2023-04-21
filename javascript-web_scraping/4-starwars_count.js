#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) throw err;
  else {
    const response = JSON.parse(body);
    const films = response.results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
