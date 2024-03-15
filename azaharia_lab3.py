import sys


def print_matrix(e):
    for row in e:
        print(row)


def levenshtein(a, b):
    # Create variables to hold lengths of string inputs 'a' and 'b'
    m = len(a)
    n = len(b)

    # Initialize E, a matrix, by populating with 0's
    E = []
    for x in range(m + 1):
        row = []
        for y in range(n + 1):
            row.append(0)
        E.append(row)

    # Populate the first row/col by starting with 1 and incrementing to the length of input 'a' and 'b' respectively
    for x in range(m + 1):
        E[x][0] = x
    for y in range(n + 1):
        E[0][y] = y

    # Fill out the rest of the elements in matrix 'E'
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            # print("", a, a[x - 1], "\n", b, b[y - 1])
            if a[x - 1] == b[y - 1]: # if the letters are equal, use the diagonal value
                E[x][y] = E[x - 1][y - 1]
            else: # if they are different, use the minimum from the left, top, or diagonal (top left)
                E[x][y] = min(E[x - 1][y], E[x][y - 1], E[x - 1][y - 1]) + 1
            # print_matrix(E)

    # return the edit distance, which is the last value in the matrix --> E[m][n]
    return E[m][n]


if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    #a = "snowy"
    #b = "sunny"
    #a = "exponential"
    #b = "polynomial"
    E = levenshtein(a, b)
    print(E)
