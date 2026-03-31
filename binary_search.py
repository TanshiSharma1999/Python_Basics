def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid
        elif arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Ask user to enter a list of items (any words)
user_input = input("Enter a sorted list of items separated by commas: ")
items = [item.strip().lower() for item in user_input.split(",")]

search_item = input("Enter the item to search for: ").strip().lower()

result = binarySearch(items, search_item)

if result != -1:
    print(f"'{search_item}' found at position {result + 1} in the list!")
else:
    print(f"'{search_item}' not found in the list.")