def op (a):
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
        print(a)
a = [9,11,13,4,6,5,7,12,1,10,2,8,3,6,16,14]
op(a)