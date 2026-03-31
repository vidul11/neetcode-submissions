class Solution:

    def encode(self, strs: List[str]) -> str:
        latent = ''

        for s in strs:   #running through the list[str]
            latent += str(len(s)) + "#" + s   #creating our encoding format for ease while decoding

        return latent 


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0    #pointer

        while i < len(s):   
            j = i  #another pointer
            while s[j] != '#':   #iterating till j reaches the postion of our seaparator #
                j += 1
            length = int(s[i:j])  # In the above encode code our latent format had the length of each string, as i is at 0 positiona and j is at # position, by slicing s[i:j] => 4/2 whatever is the length
                                  # As everything is in str format even the number we changed it to int
            output.append(s[j + 1 : j + length + 1 ])  # main step of obtaining the respective string between (j+1 => #) and (j+length+1 => +1 postion after the end of string)

            i = j + length + 1  # to keep i iterating/moving next we add move it to the beginning of the next word using this

        return output  