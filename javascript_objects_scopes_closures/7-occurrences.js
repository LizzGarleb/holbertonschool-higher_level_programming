#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (const elem of list) {
    if (searchElement === elem) {
      occur += 1;
    }
  }
  return occur;
};
