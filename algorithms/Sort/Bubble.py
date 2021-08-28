def bub_sort(self, n):
    for i in range(n-1, 0, -1):
        sp = 1
        for j in range(n-1):
            if self[j] > self[j+1]:
                temp = self[j]
                self[j] = self[j+1]
                self[j + 1] = temp
                sp = 0
                if sp == 1:
                    break
    return self


a = [30, 1, 3, 6, 10, 9, 7, 0]

n = len(a)

print(bub_sort(a, n))

'''
[1, 3, 6, 10, 9, 7, 0, 30]
[1, 3, 6, 9, 7, 0, 10, 30]
[1, 3, 6, 7, 0, 9, 10, 30]
[1, 3, 6, 0, 7, 9, 10, 30]
[1, 3, 0, 6, 7, 9, 10, 30]
[1, 0, 3, 6, 7, 9, 10, 30]
[0, 1, 3, 6, 7, 9, 10, 30]
'''