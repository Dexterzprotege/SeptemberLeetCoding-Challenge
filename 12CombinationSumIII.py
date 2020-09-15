'''Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
Note:
The solution set must not contain duplicate combinations.
 
Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]

Example 3:
Input: k = 4, n = 1
Output: []

Example 4:
Input: k = 3, n = 2
Output: []

Example 5:
Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
 
Constraints:
2 <= k <= 9
1 <= n <= 60'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.combination(k, n, 1, [], res)
        return res
        
    def combination(self, k, n, curr, arr, res):
        if len(arr) == k:
            if sum(arr) == n:
                res.append(list(arr))
            return
        if len(arr)>k or curr>9:
            return
        for i in range(curr, 10):
            arr.append(i)
            self.combination(k, n, i+1, arr, res)
            arr.pop()
