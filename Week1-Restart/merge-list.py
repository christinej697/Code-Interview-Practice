def merge_list(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1

if __name__ == "__main__":
    print(merge_list([1,3,4,5], [2,6,7,8]))


