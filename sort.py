def sort_list(inp):
    n = len(inp)
    for i in range(n):
        for j in range(0, n - i - 1):
            if inp[j] > inp[j + 1]:
                inp[j], inp[j + 1] = inp[j + 1], inp[j]
    return inp


print(sort_list([16, 83, 52, 77]))
print(sort_list([30, 12, 42, 9]))
