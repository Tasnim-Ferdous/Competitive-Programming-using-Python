input_matrix = [
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]

def main (input_matrix):
    n = len(input_matrix)
    m = len(input_matrix[0])
    answer = 0

    for i in range (n):
        for j in range (m):
            if input_matrix[i][j] == 1:
                continue
            else:
                if i-1 >= 0 and input_matrix [i-1][j] == 1:
                    answer += 1
                if i+1 < n and input_matrix [i+1][j] == 1:
                    answer += 1
                if j-1 >= 0 and input_matrix [i][j-1] == 1:
                    answer += 1
                if j+1 < m and input_matrix [i][j+1] == 1:
                    answer += 1

    print(answer)

if __name__ == "__main__":
    main (input_matrix)