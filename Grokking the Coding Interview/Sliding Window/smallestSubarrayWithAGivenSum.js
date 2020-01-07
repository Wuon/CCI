const smallest_subarray_with_given_sum = function(s, arr) {
  let start = 0,
    end = 0,
    sum = 0.0,
    smallest = Infinity;
  while (end <= arr.length) {
    if (sum >= s) {
      smallest = Math.min(smallest, end - start)
    }
    if (sum < s) {
      sum += arr[end]
      end += 1
    } else {
      sum -= arr[start]
      start += 1
    }
  }
  return smallest === Infinity ? -1 : smallest;
};

console.log(`Smallest subarray length: ${smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])}`);
console.log(`Smallest subarray length: ${smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])}`);
console.log(`Smallest subarray length: ${smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])}`);
