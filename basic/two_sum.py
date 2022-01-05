# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
from typing import List

# Brute force
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i]+nums[j]
            if sum==target:
                return [i, j]

    return []

def twoSum2(nums: List[int], target: int) -> List[int]:
    # Brute force
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i]+nums[j]
            if sum==target:
                return [i, j]

    return []

print(twoSum([2,8, 7,11,15], 9))