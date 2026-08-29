class solution:
    def reverse(self,arr):
        p1=0
        p2=len(arr)-1
        while p1<p2:
            arr[p1],arr[p2]=arr[p2],arr[p1]
            p1+=1
            p2-=1
        return arr
obj=solution()
n=int(input())
arr=[]
for i in range(n):
    val=int(input("enter the value:"))
    arr.append(val)
print(obj.reverse(arr))
