import json
import math
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

def euclidean_distance(name_a, name_b):
    try:
        user_a, user_b = users[name_a], users[name_b]
    except KeyError as e:
        return 'User not found: {}'.format(e)

    sum_squares = 0
    # Sum the squares of the differences for each rating of the users
    sum_squares = sum((v1 - v2)**2 for v1, v2 in zip(user_a.values(), user_b.values()) if v1 and v2)
    return 1 / (math.sqrt(sum_squares) + 1)

def find_nearest_neighbours(name):
    """ Returns list of users sorted by euclidean distance """

    # Calculate euclidean distance if user is not itself
    distances = ( (neighbour, euclidean_distance(name, neighbour)) for neighbour in users if name != neighbour)
    # Sort users by euclidean distance then alpabetically
    users_by_distance = sorted(distances, reverse=True, key=itemgetter(1, 0))

    # only return the users name
    return list(user for user, distance in users_by_distance)

print(find_nearest_neighbours('Alca'))
