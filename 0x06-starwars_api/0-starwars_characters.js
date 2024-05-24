#!/usr/bin/node

const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (error, _, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const charactersName = JSON.parse(body).characters.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));
    Promise.all(charactersName)
      .then(charactersNames => console.log(charactersNames.join('\n')))
      .catch(errors => console.log(errors));
  }
});
