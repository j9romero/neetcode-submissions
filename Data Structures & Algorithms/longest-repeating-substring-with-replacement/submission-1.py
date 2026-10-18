class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        left = 0
        best = 0

        for right, char in enumerate(s):
            seen[char] += 1

            while (right-left+1) - max(seen.values()) > k: #checking repla
                seen[s[left]] -= 1 #remove leftmost letter
                left += 1 # move left pointer
            best = max(best, right - left + 1)
        return best


