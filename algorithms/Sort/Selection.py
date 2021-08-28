def sel_sort(self, n):
    for i in range(n):
        np = i
        for j in range(i + 1, n):
            if self[j] < self[np]:
                np = j
        temp = self[i]
        self[i] = self[np]
        self[np] = temp
    return self


b = [22, 49, 2, 10, 6]
n = len(b)

print(sel_sort(b, n))

'''
[2, 49, 22, 10, 6] i = 0

[2, 6, 22, 10, 49] i = 1

[2, 6, 10, 22, 49] i = 2
'''