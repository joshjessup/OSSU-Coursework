def array_diff(a, b):
    for integerB in b:
        if integerB in a:
            for integerA in range(a.count(integerB)):
                a.remove(integerB)
    return a

a = list([1,2,2])
b = list([2])

print(array_diff(a,b))
