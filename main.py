def split_list(grade):
    over_middle_list = []
    under_middle_list = []

    sum = 0
    count = 0
    for g in grade:
        sum += g
        count += 1
    
    middle = sum / count

    for g in grade:
        if g > middle:
            over_middle_list.append(g)
        else:
            under_middle_list.append(g)

    tuple = (under_middle_list, over_middle_list)
 
    return tuple

split_list([1, 12, 3, 24, 5])