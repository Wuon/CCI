const length_of_longest_substring = function(str, k) {
  let start = 0;
  let longest = 0;
  let chain = 0;
  const freq = {};
  for (let end = 0; end < str.length; end++) {
    if (!(str[end] in freq)) {
      freq[str[end]] = 0;
    }
    freq[str[end]] += 1;
    chain = Math.max(chain, freq[str[end]]);
    if ((end - start + 1 - chain) > k) {
      freq[str[start]] -= 1;
      start += 1;
    }
    longest = Math.max(end - start + 1, longest);
  }
  return longest;
};

console.log(length_of_longest_substring('aabccbb', 2));
console.log(length_of_longest_substring('abbcb', 1));
console.log(length_of_longest_substring('abccde', 1));
