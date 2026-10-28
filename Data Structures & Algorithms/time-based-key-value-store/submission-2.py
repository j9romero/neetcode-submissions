class TimeMap:

    def __init__(self):
        self.mapa = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapa[key].append(tuple((value, timestamp)))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.mapa[key]
        start = 0
        end = len(arr) -1
        result = ""

        while start <= end:
            mid = (start+end) // 2
            if arr[mid][1] <= timestamp:
                result = arr[mid][0]
                start = mid+1
            else:
                end = mid -1
        return result 


