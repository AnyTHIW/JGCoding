def solution(num_list):
    item1 = num_list[-1]-num_list[-2]
    item2 = 2*num_list[-1]
    
    if item1 > 0:
        new_item = item1
    else :
        new_item = item2
        
    num_list.append(new_item)
    return num_list
