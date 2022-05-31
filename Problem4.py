#Write a function which receives a list and returns a number. In the list, all numbers 
# have been repeated twice except one number that is repeated once. The function should 
# return the number that is repeated once and return it.


def singleelement(arr, n):
    low = 0
    high = n - 2
    mid = 0
    while (low <= high):
        mid = (low + high) // 2
        if (arr[mid] == arr[mid ^ 1]):
            low = mid + 1
        else:
            high = mid - 1
     
    return arr[low]
     
arr = [2,2,3,3,4,4,5]
size = len(arr)
arr.sort()
print(singleelement(arr, size))
