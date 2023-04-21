#!/usr/bin/node
const request = require('request');
const id = process.argv[1];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(url, (err, body) => {
  if (err) throw err;
  else {
    const response = JSON.parse(body);
    const films = response.results;
    let count = 0;
    for (let i = 0; i < films.lenght; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
