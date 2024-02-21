# pylint: disable=missing-module-docstring
import os
import glob
import traceback
import json
from timeit import default_timer as timer
import psutil

file_path = os.path.dirname(__file__) + r"/input/*"
files = [os.path.basename(i) for i in glob.glob(file_path)]

def check_memory_usage():
    '''
    [DON'T MODIFY] Function to check memory consumption
    '''
    process = psutil.Process()
    memory_usage = process.memory_info().rss / (1024 ** 2)  # in megabytes
    return memory_usage

def array_manipulation(n, queries): # pylint: disable=redefined-outer-name
    '''
    Prefix sum to solve even edge cases
    '''
    init_array = [0] * (n+1) # Zeros in array initialization with an extra element

    # Perform prefix sum:
    # - Add k to the a index
    # - Substract k from the b index
    for query in queries:
        a, b, k = query
        init_array[a - 1] += k
        init_array[b] -= k

    # Find the max value in the array
    max_value = 0
    prefix_sum = 0
    for value in init_array:
        prefix_sum += value
        max_value = max(max_value, prefix_sum)

    return max_value

if __name__ == '__main__':
    with open(os.path.dirname(__file__) + '/expected-output','r', encoding='utf-8') as json_file:
        expected_output=json.load(json_file)

    for idx, test_file in enumerate(files):
        print(f"[Test case {idx+1}]")

        with open(os.path.dirname(__file__) + '/input/' + test_file,'r',encoding='utf-8') as data:
            lines = [line.rstrip() for line in data]

        first_multiple_input = lines[0].rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        queries = []

        for x in range(m):
            queries.append(list(map(int, lines[x+1].rstrip().split())))

        try:
            start = timer()
            result = array_manipulation(n, queries)
            end = timer()
            elapsed_time = end - start

            
            # Runtime error simulation 1: failed if execution time exceeds 10 seconds
            if elapsed_time > 10:
                print("Status: FAILED | Reason: Execution time exceeded 10 seconds. Skipping to next iteration.") # pylint: disable=line-too-long
                continue

            # Runtime error simulation 2: failed if memory consumption exceeds 512 MB (ML = 1024 MB) | pylint: disable=line-too-long
            if check_memory_usage() > 512:
                print("Status: FAILED | Reason: Memory usage exceeded 512 MB. Skipping to next iteration.") # pylint: disable=line-too-long
                continue

            print(f"Status: {'PASSED' if result == expected_output[test_file] else 'FAILED'} | Result: {result} | Expected: {expected_output[test_file]} | Elapsed time: {round(elapsed_time, 3)}s") # pylint: disable=line-too-long
        except: # pylint: disable=bare-except
            traceback.print_exc()
