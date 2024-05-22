#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) console.error(error);
  if (response && response.statusCode === 200) {
    const toDos = JSON.parse(body);
    const completedTasks = {};

    for (const toDo of toDos) {
      if (toDo.completed === true) {
        if (!completedTasks[toDo.userId]) {
          completedTasks[toDo.userId] = 1;
        } else {
          completedTasks[toDo.userId]++;
        }
      }
    }
    console.log(completedTasks);
  }
});
