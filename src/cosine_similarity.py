import math
import functools, operator

def getCosineDissimilarity(str1: str, str2: str):
    s1 = str1.lower().split(' ')
    #print('s1', s1)
    
    s2 = str2.lower().split(' ')
    #print('s2', s2)
    
    uniqueWords = list(set(s1 + s2))
    #print('uniqueWords', uniqueWords)
    
    freq1 = { k: 0 for k in uniqueWords } 
    for w in s1:
        freq1[w] += 1
    #print('freq1', freq1)
    
    freq2 = { k: 0 for k in uniqueWords } 
    for w in s2:
        freq2[w] += 1
    #print('freq2', freq2)
    
    product = { k: x * freq2[k] for k, x in freq1.items()}
    #print('product', product)

    prodSum = functools.reduce(operator.add, product.values())
    #print('prodSum', prodSum)

    xVector = math.sqrt(functools.reduce(operator.add, [v * v for v in freq1.values()]))
    #print('xVector', xVector)

    yVector = math.sqrt(functools.reduce(operator.add, [v * v for v in freq2.values()]))
    #print('yVector', yVector)
    
    cosineSimilarity = prodSum / (xVector * yVector)
    #print('cosineSimilarity', cosineSimilarity)
    
    return 1 - cosineSimilarity

#print(getCosineDissimilarity("\"i am looking for a relationship that makes both of our lives better. i know what i like and i hope you do too.  i am from the mid-west originally (mn/wi) and i moved to sf eight years ago. people have described me as a bubbly", "\"i had said at one point that i wasn't looking for a primary partner...and then one found me. i am very blessed to call sexybhm_bbw partner and lover. i am open to meeting new people and seeing what happens. anything beyond just a simple meeting/date"))