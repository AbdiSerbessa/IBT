
## EXercise1 
def total(nums):
    if not nums:
        return 0
   
    return nums[0] + total(nums[1:])


numbers = [2, 4, 6, 8, 10]
print(f"Sum of {numbers}:", total(numbers))



def total(nums):
    
    if not nums:
        return 0
    
    return nums[0] + total(nums[1:])

numbers = [2, 4, 6, 8, 10]
print(f"Sum of {numbers}:", total(numbers)) 




##Exercise 2

def binary_search(items, target):
    """
    Performs a binary search on a sorted list.
    Returns the index of the target if found, otherwise -1.
    """
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2

        if items[mid] == target:
            return mid  
        elif items[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1  

    return -1  



balances = [150.50, 420.00, 890.25, 1200.75, 3450.00, 5000.00, 10250.80]


target_1 = 1200.75
idx_1 = binary_search(balances, target_1)
print(f"Searching for ${target_1:.2f}: Found at index {idx_1}")

target_2 = 2500.00
idx_2 = binary_search(balances, target_2)
print(f"Searching for ${target_2:.2f}: Found at index {idx_2}")




## Exercise 3
import random

def merge(left, right):
    """Helper function to merge two sorted lists into one sorted list."""
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged


def merge_sort(items):
    """Recursively divides and sorts a list using Merge Sort."""
 
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left_half = merge_sort(items[:mid])
    right_half = merge_sort(items[mid:])

    return merge(left_half, right_half)



def test_merge_sort():
    num_tests = 5
    print("--- Testing Merge Sort vs. Built-in sorted() ---\n")

    for i in range(1, num_tests + 1):
      
        size = random.randint(10, 20)
        random_list = [random.randint(-100, 100) for _ in range(size)]

        our_result = merge_sort(random_list)
        expected_result = sorted(random_list)

        is_match = our_result == expected_result
        print(f"Test {i}: List Size = {size} | Matches `sorted()`? {is_match}")
        
        if not is_match:
            print(f"  FAILED!")
            print(f"  Input:    {random_list}")
            print(f"  Mine:     {our_result}")
            print(f"  Expected: {expected_result}")
            return

    print("\n All tests passed successfully!")

test_merge_sort()




###Exercise 4

accounts = [
    ("Abdi", 1200.75),
    ("Bona", 450.00),
    ("Cala", 5000.50),
    ("Diana", 890.25),
    ("Nohi", 3400.00)
]

sorted_accounts = sorted(accounts, key=lambda item: item[1], reverse=True)

print("Accounts sorted by balance (descending):")
for name, balance in sorted_accounts:
    print(f"{name}: ${balance:,.2f}")




 ##Exercise 5
def has_pair(nums, target):
    """
    Checks if there are two numbers in a sorted list that sum up to target.
    Uses the two-pointer technique running in O(n) time and O(1) extra space.
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True  
        elif current_sum < target:
            left += 1  
        else:
            right -= 1  

    return False 


sorted_numbers = [1, 3, 5, 8, 12, 15]

print(has_pair(sorted_numbers, 13))  
print(has_pair(sorted_numbers, 20)) 
print(has_pair(sorted_numbers, 7))      