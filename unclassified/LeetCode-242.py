class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        source = [0] * 26 # 0:48 a:97
        target = [0] * 26
        for ch in s:
            source[ord(ch)-ord('a')] += 1
        for ch in t:
            target[ord(ch)-ord('a')] += 1
        return source == target
    

s = 'abc'
source = [0] * 26
# for ch in s:
#         source[ch-49] += 1
print(ord('a')-ord('a'))

