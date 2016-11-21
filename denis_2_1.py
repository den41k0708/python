import random
import time

def create_matrix(n):
    random_matrix = [[random.randint(1, 100) for e in range(n)] for e in range(n)]

    rows = random.randint(1, n)

    for i in range(rows):
        row = random.randint(0, n - 1)
        random_matrix[row].sort(reverse=True)

    return random_matrix

def check_vector(vector):
    if(vector == sorted(vector, reverse=True)):
        return True
    else:
        return False

def create_vector(matrix):
    vector = []
    for index, row in enumerate(matrix):
        if(check_vector(row)):
            vector.append(index + 1)
    return vector

def printByTen(vector):
    print vector[0:10]
    print vector[11:15]

matrix = create_matrix(15)
print matrix

vector = create_vector(matrix)

printByTen(vector)

time.sleep(5)
