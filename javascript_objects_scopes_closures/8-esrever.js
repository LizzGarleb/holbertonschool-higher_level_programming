#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  const leng = list.length;
  for (let i = leng - 1; i >= 0; i--) {
    reverse.push(list[i]);
  }
  return reverse;
};
