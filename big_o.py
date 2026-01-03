import math
import time


def find_max(nums) -> int:
    start = time.time()
    if not nums:
        raise ValueError("List is empty")
    max = -math.inf
    for num in nums:
        if num > max:
            max = num
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    return int(max)


def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            if first_name + last_name == full_name:
                return True
    return False


def get_avg_brand_followers(all_handles, brand_name):
    length_of_handles = len(all_handles)
    found = 0

    # O(mn)
    for handle_list in all_handles:
        for handle in handle_list:
            if brand_name in handle:
                found += 1

    avg = found / length_of_handles
    return round(avg, 2)


def find_last_name(names_dict, first_name):
    try:
        last_name = names_dict[first_name]
        return last_name
    except KeyError:
        return None
