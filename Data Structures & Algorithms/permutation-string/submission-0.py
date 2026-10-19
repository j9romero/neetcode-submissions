class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window = len(s1)
        string = [0]*26
        for i in s1:
            string[(ord(i)-ord('a'))] +=1

        for start in range(len(s2)- window +1):
            seen = [0]*26
            for j in range(start, start + window):
                seen[(ord(s2[j])-ord('a'))] +=1
            if seen == string:
                return True
        return False
        

        