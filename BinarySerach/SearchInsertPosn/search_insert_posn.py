def search_insert_position(arr, ele):
    left , right = 0, len(arr) #step1: boundary condn
    while left < right:
        mid = left + (right-left)//2
        if ele <= arr[mid]:
            right = mid
        else:
            left = mid+1
    return left # step2: return left or left-1

input1 = [1,3,5,6]
ele1 = 5
ele2 = 2
print(search_insert_position(input1, ele1))
print(search_insert_position(input1, ele2))