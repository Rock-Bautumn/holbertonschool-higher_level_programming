#!/usr/bin/node
exports.esrever = function (list) {
  let length = list.length;
  const newList = [];
  while (length) {
    length--;
    newList.push(list[length]);
  }
  return newList;
};
