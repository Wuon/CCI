const fruits_into_baskets = function(fruits) {
  const freq = {};
  let start = 0;
  let maxLength = -1;
  for (let end = 0; end < fruits.length; end++) {
    if (fruits[end] in freq) {
      freq[fruits[end]] += 1
    } else {
      freq[fruits[end]] = 1
    }
    while (Object.keys(freq).length > 2) {
      freq[fruits[start]] -= 1
      if (freq[fruits[start]] === 0) {
        delete freq[fruits[start]]
      }
      start += 1
    }
    maxLength = Math.max(maxLength, end - start + 1)
  }
  return maxLength;
};

console.log(`Maximum number of fruits: ${fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])}`);
console.log(`Maximum number of fruits: ${fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])}`);
