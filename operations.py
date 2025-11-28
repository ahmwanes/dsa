def find_minimun(nums: list[int]) -> float:
    """
    Finds the minimum value in a list of integers.

    Args:
        nums (list[int]): The list of integers to search.

    Returns:
        float: The minimum value in the list.

    Raises:
        ValueError: If the input list is empty.
    """
    minimum = float("inf")

    if len(nums) == 0:
        raise ValueError("Input list is empty")

    for num in nums:
        if num < minimum:
            minimum = num

    return minimum


def find_maximum(nums: list[int]) -> float:
    """
    Finds the maximum value in a list of integers.

    Args:
        nums (list[int]): The list of integers to search.

    Returns:
        float: The maximum value in the list.

    Raises:
        ValueError: If the input list is empty.
    """
    maximum = float("-inf")

    if len(nums) == 0:
        raise ValueError("Input list is empty")

    for num in nums:
        if num > maximum:
            maximum = num

    return maximum
