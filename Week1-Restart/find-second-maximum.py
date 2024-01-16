def find_second_maximum(lst) -> int:
    
    if len(lst) < 2:
        return None

    first_elem = sec_elem = float('-inf')
    for item in lst:
        if item > sec_elem:
            if item > first_elem:
                sec_elem = first_elem
                first_elem = item
                continue
            sec_elem = item
    return sec_elem


if __name__ == "__main__":
    print(find_second_maximum([9,2,3,6]))
    
    # this way doesn't work if there are duplicates of the largest number!
    arr = [9,2,3,6]
    arr.sort()
    print(arr)
    print(arr[-2])


