class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case: check if lenghts are same, if not they cant be anagrams
        if len(s) != len(t):
            return False

        # Using dict as frequency maps to get freqs of each value in each string
        freqS, freqT = {}, {}

        for i in range (len(s)):
            freqS[s[i]] = 1 + freqS.get(s[i], 0)
            freqT[t[i]] = 1 + freqT.get(t[i], 0)

        # Comparing these freq maps directly gives us if they are anagram or not
        return freqS == freqT