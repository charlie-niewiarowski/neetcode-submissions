# Implement some dictionary based data structure that avoids collision by using timestamps

# Setting the value should set the given key's value at the given timestamp to the given value

# Sets calls are in increasing order (sorted)

# Get returns  the most recent value for the given key
    # If set was called on it and the most recent timestamp is less than or equal the given timestamp
    # If there are no values returns ""




class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((timestamp, value))
        else:
            self.data[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        arr = self.data[key]
        
        if arr[0][0] > timestamp:
            return ""
        
        # Binary Search to find timestamp
        n = len(arr)
        l, r = 0, n - 1

        if arr[l][0] > timestamp:
            return ""

        while l <= r:
            m = (l + r) // 2

            if arr[m][0] <= timestamp:
                if m == n - 1 or arr[m + 1][0] > timestamp:
                    return arr[m][1]
                else:
                    l = m + 1
            else:
                r = m - 1

