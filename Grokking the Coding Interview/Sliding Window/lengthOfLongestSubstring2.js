const length_of_longest_substring = function(arr, k) {
  let longest = 0;
  let start = 0;
  let chain = 0;

  for (let end = 0; end < arr.length; end++) {
    if (arr[end] === 1) {
      chain += 1
    }
    if (end - start + 1 - chain > k) {
      if (arr[start] === 1) {
        chain -= 1
      }
      start += 1
    }
    longest = Math.max(longest, end - start + 1)
  }

  return longest;
};

console.log(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2));
console.log(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3));
