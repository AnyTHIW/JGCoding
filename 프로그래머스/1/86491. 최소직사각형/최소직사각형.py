def solution(sizes):
    for size in sizes:
        w, h = size
        if w < h:
            size[0], size[1] = h, w
            
    list.sort(sizes, reverse=True)
    maxW = sizes[0][0]
    list.sort(sizes, key=lambda size:size[1], reverse=True)
    maxH = sizes[0][1]

    return (maxW * maxH)