class solution:
    def palindrome(self,i,s):
        if i>=len(s)//2:
            return True
        if s[i]!=s[len(s)-i-1]:
            return False
        return self.palindrome(i+1,s)  
obj=solution()
s=input()
print(obj.palindrome(0,s))
