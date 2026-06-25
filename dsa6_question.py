class Solution:
    def reverse(self, arr: list) -> None:
        arr.reverse()
        print(arr)
obj=Solution()
lst=[]
n=int(input("enter the number of elements: "))
for i in range(n):
    val=int(input("enter the value: "))
    lst.append(val)
obj.reverse(lst)
    
    
