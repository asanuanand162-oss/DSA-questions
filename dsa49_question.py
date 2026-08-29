class Solution:
    def mergeSort(self, nums):
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=self.mergeSort(nums[:mid])
        right=self.mergeSort(nums[mid:])
        result=[]
        i=0
        j=0
        while i<len(left)and j<len(right):
                    if left[i]<right[j]:
                         result.append(left[i])
                         i+=1
                    else:
                         result.append(right[j])
                         j+=1
        while i<len(left):
            result.append(left[i])
            i+=1
        while j<len(right):
            result.append(right[j])
            j+=1
        return result
obj=Solution()
nums=[]
n=int(input("enter the number of element:"))
for i in range(n):
    val=int(input("enter the value:"))
    nums.append(val)
ans=obj.mergeSort(nums)
print("sorted elements:",ans)

                  
