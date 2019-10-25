def getSetGo(nums, target, size):
    if target == 0:
        return True
    if target != 0 and size == 0:
        return False
    if nums[size - 1] > target:
        return getSetGo(nums, target, size - 1)
    return getSetGo(nums, target, size - 1) or getSetGo(nums, target - nums[size - 1], size - 1)

def main():
    testA = [2,9,5,1,6]
    testB = [2,3,15,1,16]
    print(getSetGo(testA, 12, len(testA)))
    print(getSetGo(testB, 8, len(testB)))

main()
