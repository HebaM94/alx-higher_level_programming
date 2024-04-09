#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(process.argv[2]);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
