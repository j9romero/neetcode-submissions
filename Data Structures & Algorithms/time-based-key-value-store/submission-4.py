class TimeMap:

    def __init__(self):
        self.mapa = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapa[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapa:
            return ""
        arr = self.mapa[key]
        start, end = 0, len(arr)-1
        result = ""

        while start <= end:
            mid = (start + end) //2
            if arr[mid][0] <= timestamp:
                result = arr[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        return result

        
