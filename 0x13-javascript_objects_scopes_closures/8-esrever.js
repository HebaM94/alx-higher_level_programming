#!/usr/bin/node
exports.esrever = function (list) {
  let idx = list.length - 1;
  for (let i = 0; (idx - i) > 0; i++) {
    const temp = list[idx];
    list[idx] = list[i];
    list[i] = temp;
    idx--;
  }
  return list;
};
