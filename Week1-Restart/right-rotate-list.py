def right_rotate(lst, k):
    length = len(lst)
    if length == 0:
        return lst
    counter = -(k%length)
    new_list = []
    for loop in range(length):
        new_list.append(lst[counter])
        counter += 1
    return new_list

def super_smart_way(lst, k):
    length = len(lst)
    if length == 0:
        return lst
    k = k % length
    return lst[-k:] + lst[:-k]

if __name__ == "__main__":
    print(right_rotate([10,20,30,40,50],3))
