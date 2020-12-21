def getRangeDissimilarity(minVal: int, maxVal: int, val1: int, val2: int):
    range = maxVal - minVal
    if range > 0:
        return abs(val1 - val2) / range
    return 0
   
#print(getRangeDissimilarity(1,100, 10, 98))
#print(getRangeDissimilarity(1,100, 40, 45))