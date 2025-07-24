// Problem: https://leetcode.com/problems/majority-element/
// Difficulty: Easy
// Language: Python
// Solution by: Shivam Shukla

**Boyer–Moore Voting Algorithm Logic**

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major=nums[0]
        count=1
        for i in range(1,len(nums)):
            if nums[i]==major:
                count+=1
            else:
                count-=1
                if count==0:
                    major = nums[i]
                    count=1
        return major            
