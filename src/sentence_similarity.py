from fuzzywuzzy import fuzz

def getSentenceDissimilarity(str1: str, str2: str):
    sentences = [
        str1.replace('"', '').replace("'", ""), 
        str2.replace('"', '').replace("'", "")
    ]

    r = fuzz.ratio(sentences[0], sentences[1])
    dist_1 = (100 - r) / 100
    
    return dist_1  


