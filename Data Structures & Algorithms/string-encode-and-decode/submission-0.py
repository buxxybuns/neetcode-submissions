class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for s in strs:
            length=len(s)
            encoded+=str(length) + "#" +s
        return encoded    
    def decode(self, s: str) -> List[str]:
        final=[]
        i=0
        while i <len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            i=j+1
            word=s[i:i+length]  
            final.append(word)
            i+=length

        return final

