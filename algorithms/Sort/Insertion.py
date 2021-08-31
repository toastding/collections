def ins_sort(self, n):
    for i in range(1, len(self)):
        temp = self[i]
        j = i - 1
        while temp < self[j]:
            self[j + 1] = self[j]
            j -= 1
            if j == -1:
                break
        self[j + 1] = temp
    return self


c = [6, 2, 54, 12, 90, 7]
n = len(c)
print(ins_sort(c, n))

'''
[2, 6, 54, 12, 90, 7] 

[2, 6, 12, 54, 90, 7]

[2, 6, 12, 54, 7, 90]

[2, 6, 12, 7, 54, 90]

[2, 6, 7, 12, 54, 90] 
'''