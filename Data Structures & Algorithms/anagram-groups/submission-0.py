class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map={}
        
        for s in strs:
            count=[0]*26
            for char in s:
                count[ord(char)-ord('a')]+=1
            key=tuple(count)
            if key not in char_map:
                char_map[key]=[]
            char_map[key].append(s)
        return list(char_map.values())






        
        