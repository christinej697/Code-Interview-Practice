def find_product(lst):
    product = 1
    zero_index = []
    for i in range(len(lst)):
        if lst[i] == 0:
            zero_index.append(i)
            continue
        product *= lst[i]
    
    for i in range(len(lst)):
        if zero_index:   
            if i == zero_index[0] and len(zero_index) == 1:
                lst[i] = product
            else:
                lst[i] = 0
        else:
            lst[i] = product/lst[i]

    return lst


if __name__ == "__main__":
    print(find_product([1,2,3,4]))
    print(find_product([1,2,3,4,0]))
    print(find_product([0,2,3,4,0]))
