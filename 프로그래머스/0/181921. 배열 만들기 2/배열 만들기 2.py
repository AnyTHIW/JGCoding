def solution(l, r):
    result = []
    queue = ['5']

    while queue:
        num_str = queue.pop(0)
        num = int(num_str)

        if l <= num <= r:
            result.append(num)

        if queue:
            last_num = int(queue[-1])
        else:
            last_num = num

        if last_num <= r:
            next_num_str_0 = num_str + '0'
            next_num_str_5 = num_str + '5'
            next_num_0 = int(next_num_str_0)
            next_num_5 = int(next_num_str_5)

            if next_num_0 <= r:
                queue.append(next_num_str_0)
            if next_num_5 <= r:
                queue.append(next_num_str_5)

    return sorted(result) if result else [-1]
