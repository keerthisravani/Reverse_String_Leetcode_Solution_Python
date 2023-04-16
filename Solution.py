def reverseString(self, s: List[str]) -> None:
    n=len(s)
    start=0
    end=n-1
    while start<end:
        s[start],s[end]=s[end],s[start]
        start+=1
        end-=1
    return s
s=['h','e','e','l','l','o']
print(reverseString(s))
