# Reads two integers and prints their sum
def basic_io():
    import sys

    input = sys.stdin.read
    data = input().split()
    T = int(data[0])

    test_cases = []
    index = 1

    for _ in range(T):
        n = int(data[index])
        k = int(data[index + 1])

        test_cases.append((n, k))

        index += 2

    return test_cases

def calculate_factorial_combination (max_n):
    factorial = [1] * (max_n + 1)

    for i in range (2, max_n + 1):
        factorial[i] = factorial[i-1] * i

    combination = [[0] * (max_n + 1) for _ in range (max_n + 1)]

    for n in range (max_n + 1):
        for k in range (n + 1):
            if k == 0 or k == n:
                combination[n][k] = 1
            else:
                combination[n][k] = combination[n - 1][k - 1] + combination[n - 1][k]

    return factorial, combination

def num_of_ways (n, k, factorial, combination):
    if k == 0:
        return 1
    if k > n:
        return 0
    
    return combination[n][k] * combination[n][k] * factorial[k]

def main ():
    test_cases = basic_io()

    max_n = 30

    factorial, combination = calculate_factorial_combination (max_n)

    results = []

    for caseNumber, (n, k) in enumerate (test_cases, start=1):
        ways = num_of_ways(n, k, factorial, combination)
        results.append(f"Case {caseNumber}: {ways}")

    for result in results:
        print(result)

if __name__ == "__main__":
    main ()


