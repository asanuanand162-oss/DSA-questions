class Solution:
    def insertionSort(self, nums):
        n=len(nums)
        for i in range(1,n):
            key=nums[i]
            j=i-1
            while key<nums[j]and j>=0:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        print("sorted elsements:",nums)
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
obj.insertionSort(a)
