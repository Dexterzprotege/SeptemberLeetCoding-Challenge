'''Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # def backtrack(s, d):
        #     size = len(s)
        #     if size == 0:
        #         return True
        #     for i in range(1, size+1):
        #         if s[:i] in d and backtrack(s[i:size], d):
        #             return True
        #     return False
        # return backtrack(s, wordDict)
        size = len(s)
        dp = [False]* (size+1)
        dp[0] = True
        for i in range(1, size+1):
            for j in range(0, i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
        
