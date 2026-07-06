class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS={}        
        for char in s:
            countS[char]=1+countS.get(char,0)
        for char in t:
            if char not in countS:
                return False
            countS[char]-=1
            if countS[char]<0:
                return False 
        return True         