#!/usr/bin/node

const { dict } = require('./101-data');

const userOccurrences = Object.keys(dict).reduce((newDict, userId) => {
  const occurrences = dict[userId];

  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(userId);

  return newDict;
}, {});

console.log(userOccurrences);
