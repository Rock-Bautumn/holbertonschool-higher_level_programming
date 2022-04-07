#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const myArgs = process.argv.slice(2);
const reqRoute = myArgs[0];
const fileTarget = myArgs[1];
// console.log(reqRoute);
request(reqRoute, function (error, response, body) {
  if (error !== null) {
    console.error('error:', error); // Print the error if one occurred
  }
  else {
    // console.log('code:', response && response.statusCode); // Print the response status code if a response was received
    // console.log('body:', body); // Print the HTML for the Google homepage.
    // console.log(typeof body);
    // const resJSON = JSON.parse(body);
    fs.writeFile(fileTarget, body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
