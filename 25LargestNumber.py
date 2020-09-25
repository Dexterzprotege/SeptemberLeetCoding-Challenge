'''Given a list of non negative integers, arrange them such that they form the largest number.
Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.'''

class Comparator(int):
    def __lt__(x, y):
        return str(x)+str(y) > str(y)+str(x)
        
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def solution1(nums):
            n = len(str(max(nums))) + 1
            t = []
            for i in nums:
                temp = str(i)*n
                t.append((temp[:n], i))
            t.sort(reverse=True)
            ans = ""
            for i in t:
                ans+=str(i[1])
            if int(ans)==0:
                return "0"
            return ans
        def solution2(nums):
            nums = sorted(nums, key=Comparator)
            if nums[0]==0:
                return "0"
            return ''.join(str(x) for x in nums)
        return solution2(nums)
            
