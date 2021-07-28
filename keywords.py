from math import log
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# get keyword
# retrieval = "find olympic player schedule"


def getKeyword(searchWord):
    data = pd.read_csv('dataSet.csv', low_memory=False)
    # print(data)

    data['Tag'] = data['Tag'].fillna('')

    data = data.append({'Title':'retrieval', 'Tag':searchWord}, ignore_index=True)

    # print(data)
    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(data['Tag'])
    # print(tfidf_matrix)
    # print(tfidf.get_feature_names())

    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    # print(cosine_sim)

    indices = pd.Series(data.index, index=data['Title'])
    # print(indices.head())

    idx = indices['retrieval']

    # similarty calculate for input
    sim_scores = list(enumerate(cosine_sim[idx]))
    # print(sim_scores)

    # sort lists for highest similarty
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # print(sim_scores)

    sim_scores = sim_scores[1:]
    # print(sim_scores)
    keyword_indices = [i[0] for i in sim_scores]
    # print(keyword_indices)

    return data['Title'].iloc[keyword_indices[0]]

# print(getKeyword(retrieval))