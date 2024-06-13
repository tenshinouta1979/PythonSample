#https://docs.python.org/3/library/functions.html
#b-search, List, Recursive

def binary_search(arr, low, high, key):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    else:
        return False

# Driver code
arr = [10, 20, 30, 40, 50]
key = 30
result = binary_search(arr, 0, len(arr)-1, key)

if result:
    print("Yes, the key is in the list.")
else:
    print("No, the key is not in the list.")
