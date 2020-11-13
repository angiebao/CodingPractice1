#     for i in range(numReviews):
#         # transfrom to lower case review
#         review = reviews[i].lower()
#
#         # remove special charactors other than number or alphabate or space
#         cleanReview = ''
#         for s in review:
#             if (s >= '0' and s <= '9') or (s >= 'a' and s <= 'z') or s =' ':
#                 cleanReview.append(s)
#         splitReview = cleanReview.split(" ")
#
#         # remove the repeated keywords
#         splitReview = set(splitReview)
#
#         count = collections.defaultdict(int)
#         # check if keywords in the review
#         for j in range(numCompetitors):
#             if competitors[j] in splitReview:
#                 count[competitors[i]] += 1
#
#                 # sort the dictionary to get top frequent competitors
#         # if two competitors have same frequency, sort alphabetically
#
#         countList = [(k, v * (-1)) for k, v in count.items()]
#         countList.sort(key=lambda x: (x[1], x[0]))
#
#         result = [k for (k, v) in countList]
#
#         return result[:topN]


import collections
def topK(keywords, reviews,K):
    keywords_set = set(keywords)
    count = collections.defaultdict(int)
    for i in range(len(keywords)):
        for review in reviews:
            review = review.lower()
            cleanReview = ''
            for c in review:
                if 'a' <= c <= 'z' or '0' <= c <= '9' or c == '-' or c == ' ':
                    cleanReview += c
            words = cleanReview.split(' ')
            words = list(set(words))
            for word in words:
                if word in keywords_set:
                    count[word] += 1

    result = []
    for k, v in count.items():
        result.append((k, -v))

    result.sort(key = lambda x: (x[1], x[0]))
    result = result[:K]

    final_result = [item[0] for item in result]
    return final_result

# k = 2
# keywords = ["anacell", "cetracular", "betacellular"]
# reviews = [
#   "Anacell provides the best services in the city",
#   "betacellular has awesome services",
#   "Best services provided by anacell, everyone should use anacell",
# ]

k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]



print(topK(keywords, reviews, k))
