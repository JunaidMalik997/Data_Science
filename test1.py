def multiplyNumbers(a, b):
    result = 0
    for i in range(b):
        result+=a
        
    return result

def binarysearch(a, b):
    start = 0
    end = len(a)
    mid = (start + end) // 2
    
    while start < end:
        if b < a[mid]:
            end = mid - 1
            mid = (start + end) // 2
        elif b > a[mid]:
            start = mid + 1
            mid = (start + end) // 2
        elif b == a[mid]:
            return True
    return False

results = multiplyNumbers(3,4)
print(results)

boolresult = binarysearch([2,4,6,8,1], 7)
print(boolresult)