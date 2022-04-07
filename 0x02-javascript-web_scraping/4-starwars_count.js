#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);
let reqRoute = myArgs[0];
if (!reqRoute.endsWith('/')) {
  reqRoute = reqRoute + '/';
}
const target = reqRoute.replace('films/', '') + 'people/18/';
// console.log(reqRoute);
// console.log(target);
request(reqRoute, function (error, response, body) {
  if (error !== null) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    // console.log('code:', response && response.statusCode); // Print the response status code if a response was received
    // console.log('body:', body); // Print the HTML for the Google homepage.
    // console.log(typeof body);
    const resJSON = JSON.parse(body);
    const results = resJSON.results;
    let x = 0;
    let matches = 0;
    while (x < results.length) {
      // console.log(results[x]['characters']);
      // console.log(results[x]['characters'].includes(target));
      result = results[x].characters.filter(word => word.endsWith('/18/') == true)
      if (result.length == 1) {
        matches++;
      }
      x++;
    }
    console.log(matches);
  }
});
