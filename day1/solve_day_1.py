import functools
import itertools
import sys

def calc_distance(ids1, ids2):
    ids1.sort()
    ids2.sort()
    distance = 0
    for i in range(len(ids1)):
        distance += abs(ids1[i] - ids2[i])
    return distance

def calc_similarity(ids1, ids2):
    occurences = dict()
    for x in ids1:
        occurences[x] = 0
    for x in ids2:
        if x in ids1:
            occurences[x] += 1

    similarity = 0
    for x in occurences:
        similarity += occurences[x] * x
    return similarity

ids1 = []
ids2 = []

for line in sys.stdin:
    data = line.split()
    ids1.append(int(data[0]))
    ids2.append(int(data[1]))

print("the distance is {}".format(calc_distance(ids1, ids2)))
print("the similarity is {}".format(calc_similarity(ids1, ids2)))

