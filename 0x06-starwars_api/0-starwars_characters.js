#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Makes API request to get film info
request(filmURL + filmNum, async function (err, res, body) {
  if (err) return console.error(err);

  // Parse response body to get list of character URLs
  const charURLList = JSON.parse(body).characters;

  // Iterate through character URLs and fetch info
  // Make request to each character URL
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // Parse character info and print character name
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
