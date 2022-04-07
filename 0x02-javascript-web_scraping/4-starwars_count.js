#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);
const reqRoute = myArgs[0];

// const target = reqRoute.replace('films/', '') + 'people/18/';
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
    // console.log('results:', results)
    let x = 0;
    let matches = 0;
    while (x < results.length) {
      // console.log(results[x]['characters']);
      const thesechars = results[x].characters;
      // console.log(thesechars)
      // console.log("includes? ", results[x].characters.includes('/18/'));
      // console.log("includes? ", thesechars.includes('/18/'));
      // const result = results[x].characters.filter(word => word.endsWith('/18/') === true);
      for (const character in thesechars) {
        if (thesechars[character].includes('/18/')) { matches++; }
      }
      x++;
    }
    console.log(matches);
  }
});
