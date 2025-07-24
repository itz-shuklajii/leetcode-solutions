// Problem: https://leetcode.com/problems/climbing-stairs/
// Difficulty: Easy
// Language: Python
// Solution by: Shivam Shukla


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        way1=1
        way2=2
        for i in range(3,n+1):
            current = way1 + way2
            way1=way2
            way2=current
        return current    

        
