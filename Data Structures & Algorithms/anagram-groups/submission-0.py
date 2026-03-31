class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 #Creting a list of 26 zeroes, representing a to z

            for i in s:
                count[ord(i) - ord('a')] += 1   # This subtraction will give is the location each alphabet present in the word s, thus correct position will get 1, rest 0
                                                # ord gives the ASCII values of the alphabets [82-80 = 2], count[2] +=1, will get 1 in postion 2 

            result[tuple(count)].append(s)  # We are setting key:value pairs. Count:s

        return list(result.values())  #Can directly call values from the hashamp and as list 
