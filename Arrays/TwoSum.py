def two_sum(nums, target):
    """
    One-pass solution for two sums array problem that relies on taking the value at each index, determining if any previous value requires
    it to sum to target and if not, storing what the current value would require to sum successfully
    """
    cache = {}      # Python dictionary stores

    for index in range(len(nums)):
        if cache.get(nums[index]) is not None:      # Check to see if we've previously stored this value as one a previous iteration needed to find
            return [cache[nums[index]], index]      # If so, return that and the current index (Note: None check explicitly used in case the NTF index is 0)
        else:
            number_to_find = target - nums[index]   # If not found, store the value we would have needed to sum with the current value in the cache
            cache[number_to_find] = index

    return []                                      # Failing to find the sum, return an empty array


def two_sum_two_pass(nums, target):
    """
    Two pass solution that relies on pre-processing the array, then checking to see for each value if we've stored the appropriate complement number
    """
    cache = {}
    for index in range(len(nums)):                  # Storing each array value  in the form { value: index }
        value = nums[index]
        cache[value] = index

    for index in range(len(nums)):                  # Iterate over the list once again, checking to see if the number to find was stored in the list previously
        number_to_find = target - nums[index]
        cached_index = cache.get(number_to_find)
        if cached_index is not None and index != cached_index:      # Second check required to handle possibility of repeats of values in nums
            return [index, cached_index]                            # (Potential complexity that this solution needs to handle due to pre-processing step)

    return []

