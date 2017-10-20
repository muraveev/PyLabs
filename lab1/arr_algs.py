def minarr(arr):
    min1 = arr[1]
    for i in arr:
        if i < min1:
            min1 = i
    return min1

def average(arr):
    Sum = 0
    count = 0
    for i in arr:
        count += 1
        Sum += i
    Average = Sum / count
    return Average


arr = [26, 4, 8, 8, 1, 7, 8, 486, 48, 64, 4]
min1 = minarr(arr)
average = average(arr)


print(min1)
print(average)


