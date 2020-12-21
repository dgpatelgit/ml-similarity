# Welcome to Machine Learning algorithms on computing similarity score between personality.

The repo has many core files to compute dissimilarity / similarity between nominal / ordinal and string attributes.

Main idea ::
Idea is to find the similarity between two person based on various attributes associated with that person.
ML algorithm calculates the dissimilarity between each attributes of one person with another. 
Weighted disimilarty is computed based on these mixed attributes dissimilarity.
Finally similarity rank is obtained from dissimilarity value by inverting.

Source files:
1. main.py                  => Main file that reads input, transforms into dict object and comuptes matches.
2. range_similarity.py      => Expose single function to compute dissimilarity ratio between range attributes.
3. ordinal_similarity.py    => Expose single function to compute dissimilarity ratio between ordinal attributes.
4. sentence_similarity.py   => Computes sentances dissimilarity using fuzzywuzzy package.

Details Algo Steps:
STEP 1 :: DATA TRANSFORMATION
    1.1. Identify range attributes, ordinal attributes and string attributes.
    1.2. Read CSV and build dict object of structure data. 
    1.3. Computes min & max values for range attributes.
    1.4. Build ordinal values in order list.
    1.5. Assign rank to ordinal values and set max rank.
    
STEP 2 :: COMPUTE SIMILARITY MATRIX
    2.1. Build two dimensional matrix of similarity value between two person.
    2.2. For each person pair 
        2.2.1. Compute disimilarty for range attributes
        2.2.2. Compute disimilarty for string attributes
        2.2.3. Compute disimilarty for ordinal attributes
        2.2.4. Compute final disimilarty based on mixed attributes disimilarty
        2.2.5. Compute similarity by inverting disimilarty value
        2.2.6. Update matrix with result at two places.

STEP 3 :: STORE DATA
    3.1. Write data header to output file.
    3.2. Use similarity matrix to output the values into output file.

Custom code:
There are customer function written using basic Python functions to compute the dissimilarity between two range value attributes and disimilarty between ordinal attributes.

Dependencies:
This code also uses 'fuzzywuzzy' packages 'fuzz' class to compute the ratio of similarity between to NLP sentances.

## How to run
1. Goto terminal and navigate to source root, where this readme file is present.
2. Create virtual environment at root folder by following command.
`virtualenv -p python3 venv`
3. Activate virtual environment.
`source venv/bin/activate`
4. Install project dependencies.
`pip install -r requirements.txt`
5. Run machine learning analysis.
`python src/main.py`
6. To deactivate the virtual environment.
`deactivate`