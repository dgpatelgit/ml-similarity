import math
from sentence_similarity import getSentenceDissimilarity

def getOrdinalDissimilarity(ordinalRanks, str1, str2):    
    rnk1 = ordinalRanks['rank'].get(str1, None)
    rnk2 = ordinalRanks['rank'].get(str2, None)
    
    # Incase rank are not found, perform string compare
    if not rnk1 or not rnk2:
        return getSentenceDissimilarity(str1, str2)
        
    num1 = rnk1 / ordinalRanks['maxRank']
    num2 = rnk2 / ordinalRanks['maxRank']
    
    # Compute euclidian distance
    dist = math.sqrt((num1 - num2) * (num1 - num2))
    
    return 1 - dist