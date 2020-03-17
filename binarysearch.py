# Given an array/list, write an algorithm that will search and return a boolean for whether or not that number is in that array/list
def BinarySearch(arr, num):
    # Setting the starting bounds of the subset of the array to search
    start = 0
    # Setting the ending bounds of the subset of the array to search
    end = len(arr)-1
    # Setting the middle, which is the value we actually want to check and compare
    mid = (start+end)//2

    # If start == end, then we've whittled our set down to a single array, so no more whittling down.
    while start != end:
        # If the number we're searching is the middle value of the array subset, then we found the number!
        if num == arr[mid]:
            return True

        # If the number we're searching for is less than the middle of the array subset, 
        # then we want to check the subset of the array to the LEFT of that element
        elif num < arr[mid]:
            end = mid-1
            mid = (start+end)//2
        # If the number we're searching for is greater than the middle of the array subset,
        # then we want to check the subset of the array to the RIGHT of that element
        else:
            start = mid+1
            mid = (start+end)//2

    # Once start == end, and we break out of the while loop, we want to check to see if the only element left is the right number!
    if arr[start] == num:
        return True
    else: 
        return False

