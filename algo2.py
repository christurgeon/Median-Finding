def median(ints, k):
    # Split into sublists of 5 and then create a list of those medians
    split = [ints[x:x+5] for x in range(0, len(ints), 5)]
    medians = [sorted(sublist)[int(len(sublist) / 2)] for sublist in split]

    # Deterministically select the pivot point as a probable median
    idx = int(len(medians) / 2)
    if (len(medians) <= 5): # Median of the only sublist
        pivot = sorted(medians)[idx]
    else:                   # Median of the medians recursively
        pivot = median(medians, idx)

    # Split into three sublists
    Left = []
    Right = []
    Same = []
    for val in ints:
        if (val > pivot):
            Right.append(val)
        elif (val < pivot):
            Left.append(val)
        else:
            Same.append(val)

    # Determine where k is and then recur
    if (k <= len(Left)):
        return median(Left, k)
    if (len(Left) < k and k <= len(Left) + len(Same)):
        return pivot
    if (k > len(Left) + len(Same)):
        return median(Right, k - len(Left) - len(Same))


# Driver Code
if __name__ == "__main__":
    k = int(input("Enter a value for k => "))
    file = open("input.txt", "r")
    ints = []
    for val in file.read().split():
        ints.append(int(val))
    n = len(ints)
    print("Input:", ints)
    print("Size: ", n)
    print("Deterministic Selection:", median(ints, k))
