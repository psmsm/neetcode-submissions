from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)

        for k in c1:
            if c1[k] != c2[k]:
                return False

        for k in c2:
            if c1[k] != c2[k]:
                return False

        return True