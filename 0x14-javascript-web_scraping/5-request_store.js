#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const writeFile = require('fs').writeFile;
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) throw error;
  if (response) {
    writeFile(filePath, body, 'utf8', (error) => {
      if (error) throw error;
    });
  }
});
