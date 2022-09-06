#!/usr/bin/node
exports.esrever = function (list) {
  let last = list.length - 1;
  let first = 0;
  while (last > first) {
    const temp = list[last];
    list[last] = list[first];
    list[first] = temp;
    first++;
    last--;
  }
  return list;
};
