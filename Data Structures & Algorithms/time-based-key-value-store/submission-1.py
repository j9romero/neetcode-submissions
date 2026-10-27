class TimeMap:

    def __init__(self):
        self.mapa = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapa.setdefault(key, []).append(((timestamp, value)))


    def get(self, key: str, timestamp: int) -> str:
        array = self.mapa.get(key, [])
        start = 0
        end = len(array)-1
        result = ""
        while start <= end:
            mid = (start+end)//2
            if array[mid][0] <= timestamp:
                result = array[mid][1]
                start = mid +1
            else:
                end = mid -1
        return result 

        
