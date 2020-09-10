'''Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
 
Constraints:
0 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or not nums or k <= 0:
            return False
        buckets = {}
        width = t + 1

        for n, i in enumerate(nums):
            buck = i // width
            if buck in buckets:
                return True
            else:
                buckets[buck] = i
                if buck - 1 in buckets and i - buckets[buck-1] <= t:
                    return True
                if buck + 1 in buckets and buckets[buck+1] - i <= t:
                    return True
                if n >= k:
                    del buckets[nums[n-k] // width]
        return False
