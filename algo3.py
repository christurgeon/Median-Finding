import random
import time
from algo1 import random_select
from algo2 import median


# Takes in last elem as pivot, places it in correct location
# in sorted list, places all smaller to the left, and larger to
# the right and returns pivot idx
def partition(list, low, high):
    i = low - 1        # index of smaller elem
    pivot = list[high] # pivot
    for j in range(low, high):
        if (list[j] <= pivot):
            i += 1
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

    temp = list[i+1]
    list[i+1] = list[high]
    list[high] = temp
    return (i + 1)


# QUICKSORT -- O(nlogn)
def quicksort(list, low, high):
    if (low < high):
        pivot = partition(list, low, high)
        quicksort(list, low, pivot-1)
        quicksort(list, pivot+1, high)


# Driver Code
if __name__ == "__main__":
    test_one = [9, 14, 9, 5, 10, 6, 15, 6, 13, 9]
    k_one = 5
    test_two = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
    k_two = 10

    print("TEST ONE:", test_one)
    print("TEST TWO:", test_two)
    quicksort(test_one, 0, len(test_one)-1)
    quicksort(test_two, 0, len(test_two)-1)
    print(k_one, "th smallest in TEST ONE:", test_one[k_one])
    print(k_two, "th smallest in TEST TWO:", test_two[k_two])

    #n_1 = 10000    # 10^4
    #n_3 = 100000   # 10^5
    #n_3 = 1000000  # 10^6
    n_4 = 10000000 # 10^7
    #list_n1 = [random.randint(1, n_1 / 100) for i in range(0, n_1)]
    #list_n2 = [random.randint(1, n_2 / 100) for i in range(0, n_2)]
    #list_n3 = [random.randint(1, n_3 / 100) for i in range(0, n_3)]
    list_n4 = [random.randint(1, int(n_4 / 100)) for i in range(0, n_4)]

    print("")
    start_time = time.time()
    print("RANDOM SELECTION:", random_select(list_n4, int(n_4 / 2)))
    end_time = time.time() - start_time
    print("END TIME:", end_time)

    print("")
    start_time = time.time()
    print("MEDIAN OF MEDIANS", median(list_n4, int(n_4 / 2)))
    end_time = time.time() - start_time
    print("END TIME:", end_time)

    print("")
    start_time = time.time()
    quicksort(list_n4, 0, 9999999)
    print("QUICKSORT:", list_n4[5000000])
    end_time = time.time() - start_time
    print("END TIME:", end_time)
