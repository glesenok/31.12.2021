my_list = [25, 32, 3, 5, 8, 10, 12, 27, 52]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num]>my_list[num - 1]]
print(more_then)