const find_string_anagrams = function(str, pattern) {
  const result_indexes = [];
  const freq = {};
  let start = 0;
  let matched = 0;

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
      for (let i = start; i < end + 1; i++) {
        result_indexes.push(i);
      }
      return result_indexes;
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
  return result_indexes;
};

console.log(find_string_anagrams('ppqp', 'pq'));
console.log(find_string_anagrams('abbcabc', 'abc'));
