import sys

def solution(A, B):
  # Create two new copies of A and B that are split by ",". This
  # makes it easier to manipulate. Also retains the original data.
  aConverted = A.split(",")
  bConverted = B.split(",")

  # Store results in array
  results = []

  # Store least occurences of A inside array
  aOccur = []

  # Memoize results by pre computing results for least occurence.
  # This will allow for faster access and comparison.
  for aWord in aConverted:
    aOccur.append(aWord.count(min(aWord)))

  # Iterate through all samples in B. Then Iterate through all samples in A.
  # Find lowest character using min function in B. Since we have computed
  # results of A, we can then just cycle through, tallying win while we
  # loop through aOccur. Add win to result then reset win counter
  for bWord in bConverted:
    bOccur = bWord.count(min(bWord))
    win = 0
    for occur in aOccur:
      if occur < bOccur:
        win += 1
    results.append(win)
  return results


def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = input[0]
  B = input[1]
  sys.stdout.write(",".join([str(i) for i in solution(A, B)]))


if __name__ == "__main__":
  main()
