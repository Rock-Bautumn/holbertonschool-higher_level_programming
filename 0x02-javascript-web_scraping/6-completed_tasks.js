#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);
const reqRoute = myArgs[0];
// console.log(reqRoute);
const newDict = {};
request(reqRoute, function (error, response, body) {
  if (error !== null) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    // console.log('code:', response && response.statusCode); // Print the response status code if a response was received
    // console.log('body:', body); // Print the HTML for the Google homepage.
    // console.log(typeof body);
    const resJSON = JSON.parse(body);
    resJSON.forEach(task => {
      // console.log(task.title)
      if (newDict[task.userId] === undefined) {
        newDict[task.userId] = {};
      }
      if (newDict[task.userId].completed_tasks === undefined) {
        newDict[task.userId].completed_tasks = 0;
      }
      if (task.completed === true) {
        newDict[task.userId].completed_tasks += 1;
      }
      // newDict[task.userId] = {};
    });
    // newDict['4'].completed_tasks = 0;
    const outputObj = {};
    for (const [key, value] of Object.entries(newDict)) {
      if (value.completed_tasks > 0) {
        outputObj[key] = value.completed_tasks;
        // console.log(`${key}: ${value.completed_tasks}`)
      }
      // console.log(`${key}: ${value}`);
    }
    console.log(outputObj);
  }
});
