#!/usr/bin/node
// a script that prints all characters of a Star Wars movie but ordered

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

function getCharacter (characters, index) {
  request.get(characters[index], (error, response, body) => {
    if (error) console.error(error);
    if (response && response.statusCode === 200) {
        console.log(JSON.parse(body).name);
        if (index < characters.length - 1) {
          getCharacter(characters, ++index);
        }
    }
  });
}
  
request.get(url + movieId, (error, response, body) => {
  if (error) console.error(error);
  if (response && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    getCharacter(characters, 0);
  }
});
