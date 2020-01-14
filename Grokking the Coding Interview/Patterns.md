# Patterns

Table of contents

[Sliding Window](##sliding-window)

[Topological Sort](##topological-sort)

## Sliding Window

Typically, this pattern can be identified when an index can move forwards or backwards
during iteration. This is useful because the size of the window can be fixed, grow or
shrink depending on the conditional logic.

A brute force approach on this type of problem would be to compute every possibility.

``` javascript
function max_sub_array_of_size_k(k, arr) {
  let maxSum = 0,
    windowSum = 0;

  for (i = 0; i < arr.length - k + 1; i++) {
    windowSum = 0;
    for (j = i; j < i + k; j++) {
      windowSum += arr[j];
    }
    maxSum = Math.max(maxSum, windowSum);
  }
  return maxSum;
}


console.log(`Maximum sum of a subarray of size K: ${max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])}`);
console.log(`Maximum sum of a subarray of size K: ${max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])}`);
```

This poses a problem however, since the runtime is O(n * k). It is still possible to improve the
sliding window technique, by retaining previous information.

``` javascript
function max_sub_array_of_size_k(k, arr) {
  let maxSum = 0,
    windowSum = 0,
    windowStart = 0;

  for (window_end = 0; window_end < arr.length; window_end++) {
    windowSum += arr[window_end]; // add the next element
    // slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if (window_end >= k - 1) {
      maxSum = Math.max(maxSum, windowSum);
      windowSum -= arr[windowStart]; // subtract the element going out
      windowStart += 1; // slide the window ahead
    }
  }
  return maxSum;
}


console.log(`Maximum sum of a subarray of size K: ${max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])}`);
console.log(`Maximum sum of a subarray of size KL ${max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])}`);
```

The new solution runs in O(n), by keeping all of the data inside of the window in memory, it is possible to
remove the last data point and insert the new data point for linear time.

For certain problems, it is possible to use a hashmap to store the frequency of the data. This is especially important
when the problem specifies a certain uniqueness or limit. For example, when a limit is imposed on

``` javascript

function length_of_longest_substring(str, k) {
  let windowStart = 0,
    maxLength = 0,
    maxRepeatLetterCount = 0,
    frequencyMap = {};

  // Try to extend the range [windowStart, windowEnd]
  for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
    const rightChar = str[windowEnd];
    if (!(rightChar in frequencyMap)) {
      frequencyMap[rightChar] = 0;
    }
    frequencyMap[rightChar] += 1;
    maxRepeatLetterCount = Math.max(maxRepeatLetterCount, frequencyMap[rightChar]);

    // Current window size is from windowStart to windowEnd, overall we have a letter which is
    // repeating 'maxRepeatLetterCount' times, this means we can have a window which has one letter
    // repeating 'maxRepeatLetterCount' times and the remaining letters we should replace.
    // if the remaining letters are more than 'k', it is the time to shrink the window as we
    // are not allowed to replace more than 'k' letters
    if ((windowEnd - windowStart + 1 - maxRepeatLetterCount) > k) {
      leftChar = str[windowStart];
      frequencyMap[leftChar] -= 1;
      windowStart += 1;
    }

    maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
  }
  return maxLength;
}


console.log(length_of_longest_substring('aabccbb', 2));
console.log(length_of_longest_substring('abbcb', 1));
console.log(length_of_longest_substring('abccde', 1));
```

## Topological Sort

The basic idea behind the topological sort is to provide a partial ordering among the vertices of the graph such that if there is an edge from U to V then U≤V i.e., U comes before V in the ordering. Here are a few fundamental concepts related to topological sort:

- Source: Any node that has no incoming edge and has only outgoing edges is called a source.

- Sink: Any node that has only incoming edges and no outgoing edge is called a sink.

- So, we can say that a topological ordering starts with one of the sources and ends at one of the sinks.

- A topological ordering is possible only when the graph has no directed cycles, i.e. if the graph is a Directed Acyclic Graph (DAG). If the graph has a cycle, some vertices will have cyclic dependencies which makes it impossible to find a linear ordering among vertices.

To find the topological sort of a graph we can traverse the graph in a Breadth First Search (BFS) way. We will start with all the sources, and in a stepwise fashion, save all sources to a sorted list. We will then remove all sources and their edges from the graph. After the removal of the edges, we will have new sources, so we will repeat the above process until all vertices are visited.

This is how we can implement this algorithm:

a. Initialization

We will store the graph in Adjacency Lists, which means each parent vertex will have a list containing all of its children. We will do this using a HashMap where the ‘key’ will be the parent vertex number and the value will be a List containing children vertices.
To find the sources, we will keep a HashMap to count the in-degrees i.e., count of incoming edges of each vertex. Any vertex with ‘0’ in-degree will be a source.

b. Build the graph and find in-degrees of all vertices

We will build the graph from the input and populate the in-degrees HashMap.

c. Find all sources

All vertices with ‘0’ in-degrees will be our sources and we will store them in a Queue.

d. Sort

For each source, do the following things:

- Add it to the sorted list.
- Get all of its children from the graph.
- Decrement the in-degree of each child by 1.
- If a child’s in-degree becomes ‘0’, add it to the sources Queue.
- Repeat step 1, until the source Queue is empty.

``` javascript
const Deque = require('./collections/deque'); //http://www.collectionsjs.com


function topological_sort(vertices, edges) {
  const sortedOrder = [];
  if (vertices <= 0) {
    return sortedOrder;
  }

  // a. Initialize the graph
  const inDegree = Array(vertices).fill(0); // count of incoming edges
  const graph = Array(vertices).fill(0).map(() => Array()); // adjacency list graph

  // b. Build the graph
  edges.forEach((edge) => {
    let parent = edge[0],
      child = edge[1];
    graph[parent].push(child); // put the child into it's parent's list
    inDegree[child]++; // increment child's inDegree
  });

  // c. Find all sources i.e., all vertices with 0 in-degrees
  const sources = new Deque();
  for (i = 0; i < inDegree.length; i++) {
    if (inDegree[i] === 0) {
      sources.push(i);
    }
  }

  // d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  // if a child's in-degree becomes zero, add it to the sources queue
  while (sources.length > 0) {
    const vertex = sources.shift();
    sortedOrder.push(vertex);
    graph[vertex].forEach((child) => { // get the node's children to decrement their in-degrees
      inDegree[child] -= 1;
      if (inDegree[child] === 0) {
        sources.push(child);
      }
    });
  }

  // topological sort is not possible as the graph has a cycle
  if (sortedOrder.length !== vertices) {
    return [];
  }

  return sortedOrder;
}


console.log(`Topological sort: ${
  topological_sort(4, [
    [3, 2],
    [3, 0],
    [2, 0],
    [2, 1],
  ])}`);

console.log(`Topological sort: ${
  topological_sort(5, [
    [4, 2],
    [4, 3],
    [2, 0],
    [2, 1],
    [3, 1],
  ])}`);
console.log(`Topological sort: ${
  topological_sort(7, [
    [6, 4],
    [6, 2],
    [5, 3],
    [5, 4],
    [3, 0],
    [3, 1],
    [3, 2],
    [4, 1],
  ])}`);
```
