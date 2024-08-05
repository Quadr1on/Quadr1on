l = []
for i in range(1,100000000):
    l.append(i)
# print(l)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Target found, return the index
        elif mid_value < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target not found in the array

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 50000000

result = binary_search(l, target_value)

if result != -1:
    print(f'Target {target_value} found at index {result}')
else:
    print(f'Target {target_value} not found in the array')