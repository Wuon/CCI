import sys

def solution(N, K):
  # Set max position to 0. In an array size of 1, this will set max to the first.
  maxPosition = 0

  # I am modifying to create a new copy of N which is the same but with length - K + 1. I am using something
  # similar to the sliding window technique, but in this case I just want to compare to very first value.
  # Therefore all possibilities exist where for length K exists in the range of in N len(N) - K + 1
  modifiedInput = N[:len(N) - K + 1]

  # Now we just check to see if there is a greater value and store the POSITION. This is because we need to
  # return the position + K.
  for i in range(len(modifiedInput)):
    if modifiedInput[i] > modifiedInput[maxPosition]:
      maxPosition = i
  return N[maxPosition: maxPosition + K]

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  N = [int(x) for x in input[0].split(",")]
  K = int(input[1])
  sys.stdout.write(",".join([str(i) for i in solution(N, K)]))


if __name__ == "__main__":
  main()
