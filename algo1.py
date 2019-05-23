import random


# Recursive Random Select
def random_select(list, k):
    # Get random pivot value
    pivot_idx = int(random.randint(1, 100) % len(list))
    pivot = list[pivot_idx]

    # Split into three sublists
    Left = []
    Right = []
    Same = []
    for val in list:
        if (val > pivot):
            Right.append(val)
        elif (val < pivot):
            Left.append(val)
        else:
            Same.append(val)

    # Determine where k is and then recur
    if (k <= len(Left)):
        return random_select(Left, k)
    if (len(Left) < k and k <= len(Left) + len(Same)):
        return pivot
    if (k > len(Left) + len(Same)):
        return random_select(Right, k - len(Left) - len(Same))


# Driver Code
if __name__ == "__main__":
    k = int(input("Enter a k value => "))
    A = [9, 14, 9, 5, 10, 6, 15, 6, 13, 9]
    print("Randomized Select Found:", random_select(A, k))
