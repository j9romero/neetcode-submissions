class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            seen = [0]*26
            for char in word: 
                seen[ord(char) - ord('a')] +=1
            result[tuple(seen)].append(word)
        return list(result.values())

