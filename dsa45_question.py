class Solution:
    def countFrequencies(self, nums):
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        ans=[]
        for key in freq:
            ans.append([key,freq[key]])
        print(ans)

obj=Solution()
num=[]
n=int(input("enter a number:"))
for i in range(n):
    val=int(input("enter value:"))
    num.append(val)
obj.countFrequencies(num)
    
