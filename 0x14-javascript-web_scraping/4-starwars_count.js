#!/usr/bin/node
// script that prints the number of movies where
// the character “Wedge Antilles” is present

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) throw error;
  if (response && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
  
    for (const episode of films) {
      let check = episode.characters.some((characterId) => {
        return characterId.slice(-3, -1) === '18';
      });
    if (check) count++;
    }
    console.log(count);
    }
});
