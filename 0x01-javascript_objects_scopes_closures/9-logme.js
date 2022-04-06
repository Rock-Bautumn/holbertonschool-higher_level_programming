#!/usr/bin/node
let loggedQty = 0;
exports.logMe = function (item) {
  console.log(`${loggedQty}: ${item}`);
  loggedQty++;
};
