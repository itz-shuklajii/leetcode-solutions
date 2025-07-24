// Problem: https://leetcode.com/problems/longest-common-prefix
// Difficulty: Easy
// Language: Python3
// Solution by: Shivam Shukla

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None:
            return ""
        let=strs[0]
        for each in strs[1:]:
            while not each.startswith(let):
                let=let[:-1]
        return let            
