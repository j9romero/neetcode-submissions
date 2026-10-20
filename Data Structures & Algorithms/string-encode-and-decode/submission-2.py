class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result 

        # example: 5#hello5#world
    def decode(self, s: str) -> List[str]:
        result = []
        j = 0
        i = 0

        while j < len(s):
            while s[j] != "#":
                j +=1
        
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            result.append(word)
            i = j+ 1 + length
            j=i

        return result

                  