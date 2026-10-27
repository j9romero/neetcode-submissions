class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        longest = 1
        l=0

        for r, char in enumerate(s):
            seen[char] +=1
            while seen and (r-l+1) - max(seen.values()) > k:
                seen[s[l]] -=1
                l+=1
                print("l-1")
            
            longest = max(longest, r-l+1)
        return longest