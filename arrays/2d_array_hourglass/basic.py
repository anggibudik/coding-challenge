# pylint: disable=missing-module-docstring
import os

# Complete the hourglassSum function below.
def hourglass_sum(arr):
    acc = [0]*(len(arr)-2)*(len(arr[0])-2)

    for i in range(len(arr)-2):
        n = i*(len(arr[i])-2)
        for j in range(len(arr[i])-2):
            acc[n+j] = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])

    return max(acc)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
