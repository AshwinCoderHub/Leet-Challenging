
def two_sum(nums, target):
    n = len(nums)


    for i in range(n - 1):
        for j in range(i + 1, n):
            # Check if the pair sums up to the target
            if nums[i] + nums[j] == target:
                return [i, j]

    # no solution is found
    return None


nums1 = [2, 7, 11, 15]
target1 = 9
result1 = two_sum(nums1, target1)
print(result1)

nums2 = [3, 2, 4]
target2 = 6
result2 = two_sum(nums2, target2)
print(result2)

nums3 = [3, 3]
target3 = 6
result3 = two_sum(nums3, target3)
print(result3)