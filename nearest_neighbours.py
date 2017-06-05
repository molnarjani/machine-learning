import json
import math
import itertools
from operator import itemgetter
from pprint import pprint


with open('movies.json', 'r') as f:
    data = json.load(f)

    users = {}
    for user in data['users']:
        # Not needed
        del user['timestamp']
        name = user.pop('name')
        users[name] = user

def euclidean_distance(user_a, user_b):
    sum_squares = 0
    # Sum the squares of the differences for each rating of the users
    sum_squares = sum((v1 - v2)**2 for v1, v2 in zip(user_a.values(), user_b.values()) if v1 and v2)
    return 1 / (math.sqrt(sum_squares) + 1)

def find_nearest_neighbours(name):
    """ Returns list of users sorted by euclidean distance """

    # Calculate euclidean distance if user is not itself
    distances = ( (neighbour, euclidean_distance(users[name], users[neighbour])) for neighbour in users if name != neighbour)
    # Sort users by euclidean distance then alpabetically
    users_by_distance = sorted(distances, key=lambda x: (-x[1], x[0]))

    # only return the users name
    return list(user for user, distance in users_by_distance)

print(find_nearest_neighbours('Kenneth'))
