#!/usr/bin/node
// a script that prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

request.get(url + movieId, (error, response, body) => {
    if (error) console.error(error);
    if (response && response.statusCode === 200) {
      const characters = JSON.parse(body).characters;
      characters.forEach((character) => {
        request.get(character, (error, response, body) => {
          if (error) console.error(error);
          if (response && response.statusCode === 200) {
            console.log(JSON.parse(body).name);
          }
        });
      });
    }
});
