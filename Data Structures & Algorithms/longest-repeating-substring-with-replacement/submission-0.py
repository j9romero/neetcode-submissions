class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        runs = {}
        start = 0
        best = 0

        for i , char in enumerate(s):
            runs[char] = runs.get(char, 0) +1
            while (i-start+1) - max(runs.values()) > k:
                runs[s[start]] -=1
                start += 1
            best = max(best, i-start+1)
        return best


#given a number of replacements and seeing where those replacements go to get the longest consecutive string of same letter 
#seems to be that you can pick any k characters, dont have to be consecutive

#maybe find the longest existing pattern and check if the same letter is k spots away and change those k spots, otherwise change the k spots closest to that string (doesnt work in the case of AAABBABB)

#maybe find all cases of each letter being in a consecutive string and see if there is k spots between two instances of it. if so we change those, if not, we look for the longest consecutive sequence and fill up the k nearest different letters 
#two biggest consecutive string that are k diff letters apart (find for each different letter), if none exist pick the longest sequence
#maybe just try each scenario and pick the longest