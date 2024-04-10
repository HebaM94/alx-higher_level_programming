#!/usr/bin/node
const dict = require('./101-data').dict;

const sortedDict = {};

for (const key in dict) {
  const occurrences = dict[key];
  if (sortedDict[occurrences]) {
    sortedDict[occurrences].push(key);
  } else {
    sortedDict[occurrences] = [key];
  }
}

console.log(sortedDict);
