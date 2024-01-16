# O(n^2) time
def find_first_unique(lst):
    if len(lst) == 0:
        return None

    seen = []
    nonUnique = []
    for item in lst:
        if item in seen:
            nonUnique.append(item)
        else:
            seen.append(item)

    for item in seen:
        if item not in nonUnique:
            return item
    return None

# O(n) time
def good_find_dict(lst):
    counts = {}
    # Initialize dictionary with pairs like (lst[i], count)
    counts = count.fromkeys(lst,0)
    for item in lst:
        counts[item] = counts[item] + 1     #iterate item count stored in dict
    
    for item in lst:
        if (counts[item] is 1):
            return item
    return None

if __name__ == "__main__":
    print(find_first_unique([9,2,3,2,6,6]))
    print(find_first_unique([4,5,1,2,0,4]))
