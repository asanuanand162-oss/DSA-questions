class Solution:
    def bubbleSort(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        print("sorted elements:",nums)
obj=Solution()
a=[]
n=int(input("enter thr number:"))
for i in range(n):
               val=int(input("enter the value:"))
               a.append(val)
print("original value:",end=" ")
for i in range(n):
               print(a[i],end=" ")
print()
obj.bubbleSort(a)
