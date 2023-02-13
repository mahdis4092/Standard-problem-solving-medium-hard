'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
#my solution
nums = [2,11,15,7]
target = 9
A=[]
for j in range(len(nums)):
    for k in range(j+1,len(nums)):
        if nums[j]+nums[k]==target:
            A.append(j)
            A.append(k)
            k+=1
    j+=1
print(A)
        
#Leetcode submit
class Solution:
    def twoSum(self, nums: List[int], target: int):
         A=[]
         for j in range(len(nums)):
             for k in range(j+1,len(nums)):
                 if nums[j]+nums[k]==target:
                     A.append(j)
                     A.append(k)
                     k+=1
             j+=1
         return A       


