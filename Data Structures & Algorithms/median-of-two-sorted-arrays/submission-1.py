class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A                      # make A the shorter array

        total = len(A) + len(B)
        half = (total + 1) // 2              # size of the left half

        l, r = 0, len(A)

        while l <= r:
            i = (l + r) // 2                 # elements taken from A
            j = half - i                     # elements taken from B

            Aleft  = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i]     if i < len(A) else float('inf')
            Bleft  = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j]     if j < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:     # valid split
                if total % 2 == 1:
                    return float(max(Aleft, Bleft))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1                    # took too many from A
            else:
                l = i + 1                    # took too few from A