const find_permutation = function(str, pattern) {
  const freq = {};
  let matched = 0;
  let start = 0;

  for (let i = 0; i < pattern.length; i++) {
    if (!(pattern[i] in freq)) {
      freq[pattern[i]] = 0;
    }
    freq[pattern[i]] += 1;
  }

  for (let end = 0; end < str.length; end++) {
    if (str[end] in freq) {
      freq[str[end]] -= 1;
      if (freq[str[end]] === 0) {
        matched += 1;
      }
    }

    if (Object.keys(freq).length === matched) {
      return true;
    }

    if (end >= pattern.length - 1) {
      if (str[start] in freq) {
        if (freq[str[start]] === 0) {
          matched -= 1;
        }
        freq[str[start]] += 1;
      }
      start += 1;
    }
  }
  return false;
};

console.log(`Permutation exist: ${find_permutation('oidbcaf', 'abc')}`);
console.log(`Permutation exist: ${find_permutation('odicf', 'dc')}`);
console.log(`Permutation exist: ${find_permutation('bcdxabcdy', 'bcdyabcdx')}`);
console.log(`Permutation exist: ${find_permutation('aaacb', 'abc')}`);
