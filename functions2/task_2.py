def make_matrix(size, value=0):
    if isinstance(size, int):
         width = height = size
    else:
        width, height = size

    
    return [[value for _ in range(width)] for _ in range(height)]


result1 = make_matrix(3)
print(result1)  
# [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

result2 = make_matrix((4, 2), 1)
print(result2)  
# [
#     [1, 1, 1, 1],
#     [1, 1, 1, 1]
# ]
