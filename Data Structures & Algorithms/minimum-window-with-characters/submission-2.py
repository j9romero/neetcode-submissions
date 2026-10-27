class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        have = defaultdict(int)
        need = Counter(t)

        
        l = 0
        best = float("inf")
        start = 0
        required = len(need)
        have_count = 0
        for r, char in enumerate(s):
            if char in need:
                have[char] +=1
                if have[char] == need[char]:
                    have_count+=1
            while have_count == required:
                if r - l + 1 < best:
                    best = r-l+1
                    start = l
                left_char = s[l]
                if left_char in need:
                    if have[left_char] == need[left_char]:
                        have_count -= 1
                    have[left_char] -= 1
                l += 1
        if best == float("inf"):
            return ""
        return s[start:start+best]
            

        