def balancedSum(nums):
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return -1
    dpFromLeft = [0] * len(nums)
    dpFromRight = [0] * len(nums)
    dpFromLeft[0] = nums[0]
    dpFromRight[len(nums) - 1] = nums[len(nums) - 1]
    for i in range(1, len(nums)):
        dpFromLeft[i] = nums[i] + dpFromLeft[i - 1]
        dpFromRight[len(nums) - 1 - i] = nums[len(nums) - 1 - i] + dpFromRight[len(nums) - 1 - i]
    for i in range(1, len(nums) - 1):
        if dpFromLeft[i - 1] == dpFromRight[i + 1]:
            return i
    return -1

def main():
    testA = [1,2,3,4,6]
    testB = [1,2,3,3]
    print(balancedSum(testA))
    print(balancedSum(testB))

main()
