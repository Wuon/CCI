const max_sub_array_of_size_k = function(k, arr) {
  let start = 0;
  let end = 0;
  let sum = 0.0;
  let largest = Number.MIN_VALUE;
  while (end < arr.length) {
    if (end >= k) {
      largest = Math.max(largest, sum);
      sum -= arr[start];
      start += 1;
    }
    sum += arr[end];
    end += 1;
  }
  return largest;
};

console.log(`Maximum sum of a subarray of size K: ${max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])}`);
console.log(`Maximum sum of a subarray of size K: ${max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])}`);
