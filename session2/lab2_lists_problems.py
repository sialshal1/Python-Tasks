"""List Problems - Testing student capability with list operations."""


def find_max_min(numbers):
    """Find the maximum and minimum values in a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        tuple: (max_value, min_value)
    """
    # Write your solution here
    initial = 0
    min = 1000
    max = 0 
    for i in range(len(numbers)):
        initial = numbers[i-1]
        if initial <= min: 
            min = initial
        if initial >= max: 
            max = initial
    return (max , min)

def reverse_list(items):
    """Reverse a list without using built-in reverse() method.

    Args:
        items (list): List to reverse

    Returns:
        list: Reversed list
    """
    # Write your solution here
    x = []
    list_length = len(items)
    while list_length > 0: 
        x.append(items[list_length-1])
        list_length=list_length-1
    return x 

    

def list_statistics(numbers):
    """Calculate basic statistics for a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        dict: Dictionary with sum, average, count
    """
    # Write your solution here
    list_length = len(numbers)
    avg = 0 
    sum = 0 
    for i in range(list_length): 
        sum = sum + numbers[i-1]
    avg = sum/list_length    
    statistics = {"sum":sum, "average" : avg , "count" : list_length }
    return statistics

def flatten_nested_list(nested_list):
    """Flatten a nested list structure.

    Args:
        nested_list (list): List containing sublists

    Returns:
        list: Flattened list
    """
    # Write your solution here
    list_length = len(nested_list)
    x = [] 
    for i in range(list_length): 
        for j in range(len(nested_list[i])):
            x.append(nested_list[i][j])
    return x 

if __name__ == "__main__":
    # Test cases
    print("Testing find_max_min...")
    result = find_max_min([1, 5, 3, 9, 2])
    assert result == (9, 1), f"Expected (9, 1), got {result}"

    print("Testing reverse_list...")
    result = reverse_list([1, 2, 3, 4, 5])
    assert result == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {result}"

    print("Testing list_statistics...")
    result = list_statistics([1, 2, 3, 4, 5])
    expected = {"sum": 15, "average": 3.0, "count": 5}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing flatten_nested_list...")
    result = flatten_nested_list([[1, 2], [3, 4], [5, 6]])
    assert result == [1, 2, 3, 4, 5, 6], f"Expected [1, 2, 3, 4, 5, 6], got {result}"

    print("All tests passed!")
