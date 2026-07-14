class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        track = {}
        for i in range(len(s)):
            track[s[i]] = track[s[i]] + 1 if s[i] in track else 1
            track[t[i]] = track[t[i]] - 1 if t[i] in track else -1
        for x in track.values():
            if x != 0:
                return False
        return True
        
        