'''Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.
Follow up: Could you do this in O(n) runtime?
Example 1:
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:
Input: nums = [0]
Output: 0

Example 3:
Input: nums = [2,4]
Output: 6

Example 4:
Input: nums = [8,10,2]
Output: 10

Example 5:
Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 
Constraints:
1 <= nums.length <= 2 * 104
0 <= nums[i] <= 231 - 1'''

class Trie:
    def __init__(self):
        self.children = {}
        
class Solution:
    # Insert into Trie bit by bit
    def insertBits(self, num):
        bits = bin(num)[2:].zfill(32)
        node = self.root
        for bit in bits:
            if bit not in node.children:
                node.children[bit] = Trie()
            node = node.children[bit]
    
    #Find the max of a number in the trie 
    def findmax(self, num):
        bits = bin(num)[2:].zfill(32)
        node = self.root
        ans = ''
        for bit in bits:
            if bit == '0':
                opp_bit = '1'
            elif bit == '1':
                opp_bit = '0'
            if opp_bit in node.children:
                ans += opp_bit
                node = node.children[opp_bit]
            else:
                ans += bit
                node = node.children[bit]
        return int(ans, 2) ^ num
        
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Create a Trie Root node 
        self.root = Trie()
        # Insert all numbers in array into trie in form of bits
        for num in nums:
            self.insertBits(num)
        ans = 0
        # for each number in array, find the corresponding max number of it from trie by complementing each bit
        for num in nums:
            ans = max(ans, self.findmax(num))
        return ans
            
