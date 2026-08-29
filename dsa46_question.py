class Solution:
    def selectionSort(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
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
obj.selectionSort(a)
               
