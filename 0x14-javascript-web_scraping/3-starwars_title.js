#!/usr/bin/node
// a script that prints the title of a Star Wars movie
// where the episode number matches a given integer

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

request.get(url + movieId, (error, response, body) => {
  if (error) throw error;
  console.log(response && JSON.parse(body).title);
});
