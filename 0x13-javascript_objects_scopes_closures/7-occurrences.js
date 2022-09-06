#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const li of list) {
    if (li === searchElement) {
      i++;
    }
  }
  return i;
};
