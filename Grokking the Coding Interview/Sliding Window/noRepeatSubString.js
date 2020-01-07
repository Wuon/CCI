const non_repeat_substring = function (str) {
  largest = 0;
  start = 0;
  const s = new Set();
  for (let end = 0; end < str.length; end++) {
    while (s.has(str[end])) {
      s.delete(str[start]);
      start += 1;
    }
    s.add(str[end]);
    largest = Math.max(largest, s.size);
  }
  return largest;
};

console.log(`Length of the longest substring: ${non_repeat_substring('aabccbb')}`);
console.log(`Length of the longest substring: ${non_repeat_substring('abbbb')}`);
console.log(`Length of the longest substring: ${non_repeat_substring('abccde')}`);
