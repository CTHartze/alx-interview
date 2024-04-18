#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/';

// Makes an API request to get film info
request(`${url}films/${process.argv[2]}`, async (error, response, body) => {
  error && console.log(error);

  // Parse response body to get the list of character URLs
  const chars = (JSON.parse(response.body).characters);
    for (const char of chars) {
      await new Promise((resolve, reject) => {
        request(char, (error, response, body) => {
          error && console.log(error);

          const name = JSON.parse(response.body).name;
          console.log(name);
          resolve();
        });
      });
    }
});
