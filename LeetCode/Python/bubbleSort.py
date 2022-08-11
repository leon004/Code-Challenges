def bubble(a):
    for i in range(len(a)):
        for x in range (len(a)-1):
            if a[x] > a[x+1]:
                aux = a[x]
                a[x] = a[x+1]
                a[x + 1] = aux

    return a