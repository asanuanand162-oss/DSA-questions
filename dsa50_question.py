class Solution:
    def bubbleSort(self, nums):
        if len(nums)<=1:
            return nums
        did_swap=False
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                did_swap=True
        if not did_swap:
                return nums
        nums[:-1]=self.bubbleSort(nums[:-1])
        return nums
obj=Solution()
nums=[]
n=int(input("enter the number of element:"))
for i in range(n):
    val=int(input("enter the value:"))
    nums.append(val)
ans=obj.bubbleSort(nums)
print("sorted elements:",ans)

                  
