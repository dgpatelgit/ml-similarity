import os
import csv
import json
import functools, operator

from range_similarity import getRangeDissimilarity
from sentence_similarity import getSentenceDissimilarity
from ordinal_similarity import getOrdinalDissimilarity

INPUT_DATA='./data/data.csv'
OUTPUT_DATA='./data/output.csv'

processedData = {}
rangeColumns = {
    'age': {
        'min': 100,
        'max': 1
    },
    'height': {
        'min': 500,
        'max': 1
    },
    'education_level': {
        'min': 100,
        'max': 0
    }
}
stringColumns = ['status', 'sex', 'orientation', 'job', 'location', \
    'pets', 'smokes', 'language', 'new_languages', 'body_profile', 'dropped_out', 'bio', \
    'interests', 'other_interests', 'location_preference']
    
ordinalColumns = {
    'drinks': ['not at all', 'rarely', 'socially', 'often', 'very often', 'desperately'],
    'drugs': ['never', 'sometimes', 'often'],
}

columnId = []
with open(INPUT_DATA, 'r') as f_input:
    csv_input = csv.reader(f_input)
    header = next(csv_input)
    for p in csv_input:
        #if len(p[0]) > 9:
        #    continue

        allData = ''
        for i in range(0, 21):
            allData += str(p[i]) + ' '

        person = {
            'id': p[0],
            'name': p[1],
            'age': float(p[2]),
            'status': p[3],
            'sex': p[4],
            'orientation': p[5],
            'drinks': p[6],
            'drugs': p[7],
            'height': float(p[8]),
            'job': p[9],
            'location': p[10],
            'pets': p[11],
            'smokes': p[12],
            'language': p[13],
            'new_languages': p[14],
            'body_profile': p[15],
            'education_level': float(p[16]),
            'dropped_out': p[17],
            'bio': p[18],
            'interests': p[19],
            'other_interests': p[20],
            'location_preference': p[21],
            'allData': allData,
        }
        processedData[p[0]] = person
        columnId.append(p[0])
        
        for k, v in rangeColumns.items():
            if v['min'] > person[k]:
                rangeColumns[k]['min'] = person[k]
            if v['max'] < person[k]:
                rangeColumns[k]['max'] = person[k]
                
        # Update ordinal column values, if not present
        for k, v in ordinalColumns.items():
            if person[k] not in v:
                print('Ordinal not found', person[k], 'adding it now')
                ordinalColumns[k].append(person[k])

# Compute ordinal rank for each value
tempOrdinal = {}
for k, v in ordinalColumns.items():
    tempOrdinal[k] = {
        'rank': { d : i for i, d in enumerate(v)},
        'maxRank': len(v) - 1
    }
ordinalColumns = tempOrdinal

totalUser = len(columnId)
matrixValues = [[0 for _ in range(totalUser)] for _ in range(totalUser)]

processingIndex = 0
for indx1, id1 in enumerate(columnId):
    processingIndex += 1
    p1 = processedData[id1]
    print('Processing', processingIndex, '/', totalUser, p1['name'])
    for indx2, id2 in enumerate(columnId):
        if id1 == id2:
            matrixValues[indx1][indx2] = 0
            break

        p2 = processedData[id2]
        '''dissimilarityValue = {}
        for k, v in rangeColumns.items():
            dissimilarityValue[k] = getRangeDissimilarity(v['min'], v['max'], p1[k], p2[k])
            
        for k in stringColumns:
            dissimilarityValue[k] = getSentenceDissimilarity(p1[k], p2[k])
            
        for k in ordinalColumns:
            dissimilarityValue[k] = getOrdinalDissimilarity(ordinalColumns[k], p1[k], p2[k])

        totalAttributes = len(dissimilarityValue.keys())
        dissSum = functools.reduce(operator.add, [v for v in dissimilarityValue.values()])
        dissimilarity = dissSum / totalAttributes'''
        dissimilarity = getSentenceDissimilarity(p1['allData'], p2['allData'])

        similarityValue = 1 - dissimilarity
        matrixValues[indx1][indx2] = round(similarityValue * 100, 2)
        matrixValues[indx2][indx1] = matrixValues[indx1][indx2]

matchMatrix = 'user_id'
for id in columnId:
    matchMatrix += ',' + id
matchMatrix += '\n'

with open(OUTPUT_DATA, 'w') as fp:
    fp.write(matchMatrix)
    for indx1, id1 in enumerate(columnId):
        fp.write(id1 + ',' + ','.join([str(v) for v in matrixValues[indx1]]) + '\n')
