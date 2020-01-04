function find_averages_of_subarrays(k, arr){
  const result = [];
  let sum = 0.0;
  let start = 0;
  for (i = 0; i < arr.length; i++) {
    sum += arr[i];
    if ( i >= k - 1) {
      result.push(sum / k);
      sum -= arr[start];
      start += 1;
    }
  }
  return result;
}

const result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]);
console.log(`Averages of subarrays of size K: ${result}`);
