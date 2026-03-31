class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for cha in word:
                count[ord(cha) - ord('a')] +=1 
                
            freq_map[tuple(count)].append(word)

        return list(freq_map.values())