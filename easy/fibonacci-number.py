// Problem: https://leetcode.com/problems/fibonacci-number/
// Difficulty: Easy
// Language: Python3
// Solution by: Shivam Shukla

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n==1 or n ==2:
            return 1
        return self.fib(n-1)+self.fib(n-2)        
        
