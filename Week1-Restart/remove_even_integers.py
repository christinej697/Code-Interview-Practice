# takes in a list w/ random integers, returns list w/ only odd integers
def remove_even(lst):
    n = len(lst)
    remove = []
    #flag = "Even"
    #if (n%2) != 0:
    #    flag = "odd"
    #for i in range(n//2):
    #    if (lst[i]%2) == 0:
    #        remove.append(i)
    #    if (lst[-1-i]%2) == 0:
    #        remove.append(-i)
    #    if (flag == "odd") and (i == (n//2 - 1)):
    #            if (lst[i+1]%2) == 0:
    #                remove.append(i+1)
    for i in reversed(range(n)):
        if (lst[i]%2) == 0:
            #remove.append(i)
            lst.pop(i)
    print(i,":",remove)
    #for num in remove:
        #lst.pop(num)
    return lst


if __name__ == "__main__":
    print(remove_even([1,2,4,5,10,6,3]))
