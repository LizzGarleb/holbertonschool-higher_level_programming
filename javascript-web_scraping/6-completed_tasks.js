#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) throw err;
  else {
    const tasks = JSON.parse(body);
    const allTasks = {};
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed === true) {
        if (allTasks[tasks[i].userId] === undefined) {
          allTasks[tasks[i].userId] = 1;
        } else {
          allTasks[tasks[i].userId]++;
        }
      }
    }
    console.log(allTasks);
  }
});
