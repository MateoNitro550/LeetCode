from typing import List


class Solution:
    def two_sum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def two_sum_hashmap(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            else:
                hashmap[num] = i
        return []


if __name__ == '__main__':
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    print(solution.two_sum_hashmap(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(solution.two_sum_hashmap(nums, target))

    nums = [3, 3]
    target = 6
    print(solution.two_sum_hashmap(nums, target))
