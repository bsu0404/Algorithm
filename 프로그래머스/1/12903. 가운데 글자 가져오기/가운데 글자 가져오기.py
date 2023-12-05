def solution(s):
    length=len(s);
    ans=s[length//2]
    if length%2!=0:
        return ans
    else:
        ans=s[length//2-1]+ans
        return ans