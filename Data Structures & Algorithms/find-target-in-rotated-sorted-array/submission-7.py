class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start+end)//2
            print("start:", start, "end:", end, "mid:", mid, "nums[mid]:", nums[mid])

            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[end]:
                if nums[mid] < target <= nums[end]:
                    start = mid +1
                else:
                    end = mid -1
            else: # nums[mid] < target
                if nums[start] <= target < nums[mid]:
                    end = mid -1
                else:
                    start = mid +1

        return -1
