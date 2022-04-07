#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);
request(myArgs[0], function (error, response, body) {
  if (error !== null) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    console.log('code:', response && response.statusCode); // Print the response status code if a response was received
    // console.log('body:', body); // Print the HTML for the Google homepage.
  }
});
