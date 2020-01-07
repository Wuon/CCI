const longest_substring_with_k_distinct = function(str, k) {
  const s = new Set();
  let start = 0;
  let longest = -1;
  for (let i = 0; i < str.length; i++) {
    s.add(str[i]);
    if (s.size === k) {
      longest = Math.max(longest, i - start + 1);
    }
    while (s.size > k) {
      s.delete(str[start])
      start += 1
    }
  }
  return longest;
};

console.log(`Length of the longest substring: ${longest_substring_with_k_distinct('araaci', 2)}`);
console.log(`Length of the longest substring: ${longest_substring_with_k_distinct('araaci', 1)}`);
console.log(`Length of the longest substring: ${longest_substring_with_k_distinct('cbbebi', 3)}`);
