#!/usr/bin/node
const fs = require('fs');

const a = fs.readFileSync(process.argv[2]).toString();
const b = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], (a + b));
