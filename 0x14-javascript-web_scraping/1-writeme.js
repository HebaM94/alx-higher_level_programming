#!/usr/bin/node
// a script that writes a string to a file.

const writeFile = require('fs').writeFile;
const filepath = process.argv[2];
const string = process.argv[3];

writeFile(filepath, string, 'utf8', (error) => {
    if (error) throw error;
  });
