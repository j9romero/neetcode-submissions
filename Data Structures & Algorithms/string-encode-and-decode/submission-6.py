class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result
    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        result = []
        while j < len(s):
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            result.append(word)
            j+= length+1
            i = j
        return result

