// Problem: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
// Difficulty: Easy
// Language: Python
// Solution by: Shivam Shukla

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count =0
        for num in grid:
            for each in num:
                if (each<0):
                    count+=1
        return count            
