def findMinimumCrazy(lst):
    length = len(lst)
    if length == 0:
        return None
    if length == 1:
        return lst[0]
    if length == 2:
        return lst[0] if lst[0] < lst[1] else lst[1]

    small = 0
    large = length - 1
    curr = 1
    if lst[small] > lst[large]:
        lst[small], lst[large] = lst[large], lst[small]
    while curr != large:
        if lst[small] > lst[curr]:
            lst[small], lst[curr] = lst[curr], lst[small]
        elif lst[large] < lst[curr]:
            lst[large], lst[curr] = lst[curr], lst[large]
        curr += 1
    return lst


def findMinimum(lst):
    smallest = lst[0]
    for elem in lst:
        if elem < smallest:
            smallest = elem

    return smallest


if __name__ == "__main__":
    print(findMinimum([9,2,3,6]))
    print(findMinimum([4,2,1,5,0]))
