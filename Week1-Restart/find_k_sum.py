def find_sum(lst, k):
    
    lst.sort()
    high = len(lst) - 1
    low = 0
    while True:
        sum = lst[low] + lst[high]
        print(high, low, ":", sum)
        if sum > k:
            high -= 1
            print("high")
        elif sum < k:
            low += 1
            print("low")
        elif sum == k:
            print("equal")
            return [lst[low], lst[high]]

        if low == high:
            print("none")
            return []


if __name__ == "__main__":
    
    print(find_sum([1,21,3,14,5,60,7,6], 81))


