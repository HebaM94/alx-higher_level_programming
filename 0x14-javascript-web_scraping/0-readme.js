#!/usr/bin/node
//a script that reads and prints the content of a file.

const readFile = require('fs').readFile;
const filename = process.argv.slice(2)[0];

if (filename) {
  readFile(filename, 'utf8', (error, data) => {
    if (error) throw error;
    console.log(data);
  });
}
