def search_rotated_array(arr, target):
    left , right = 0, len(arr)-1 #step1: boundary condn , here we should use bundary condn for right as len(arr)-1
    # as we are going to use the value at arr[right]
    
    # This logic is only valid if duplicates are not present in the array 
    # 
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] == target:
            return mid
            
        if arr[left] <= arr[mid]:
            if target >= arr[left] and target < arr[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if target > arr[mid] and target <= arr[right]:
                left = mid+1
            else:
                right = mid-1
            
    return -1  # Here return condition is changed, we are not returning left or left-1



def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()

