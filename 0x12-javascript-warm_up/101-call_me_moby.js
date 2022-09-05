#!/usr/bin/node
exports.callMeMoby = function (x, threetimes) {
  for (let i = 0; i < x; i++) {
    threetimes();
  }
};
