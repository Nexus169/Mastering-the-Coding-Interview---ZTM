def get_max_water_container_bf(height):
    """
    Function that calculates the max size container that can be created from 2 numbers in an integer array containing heights using brute force
    """
    max_area = 0
    for left_side in range(len(height)):
        for right_side in range(left_side + 1, len(height)):
            short_side = min(height[left_side], height[right_side])
            current_area = short_side * (right_side - left_side)
            max_area = max(max_area, current_area)
    return max_area


def get_max_water_container(height):
    """
    Function that calculates the max size container that can be created from 2 numbers in an integer array containing heights using a two pointer solution
    """
    max_area = 0
    left_side = 0
    right_side = len(height) - 1

    while left_side < right_side:
        short_side = min(height[left_side], height[right_side])     # determine which side is the shorter height, then calculate current area of container
        current_area = short_side * (right_side - left_side)

        max_area = max(max_area, current_area)                      # update our current found max area

        if height[left_side] <= height[right_side]:                 # advance whichever side had the shorter height closer to the middle
            left_side += 1
        else: right_side -= 1

    return max_area

# Some tests

heights_empty = []                  # Expected: 0
heights_single = [5]                # Expected: 0
heights = [7, 1, 2, 3, 9]           # Expected: 28
heights_2 = [4, 8, 1, 2, 3, 9]      # Expected: 32

# with optimal solution
print("Optimal Solution:")
print(get_max_water_container(heights_empty))
print(get_max_water_container(heights_single))
print(get_max_water_container(heights))
print(get_max_water_container(heights_2))

# with brute force
print("Brute Force:")
print(get_max_water_container_bf(heights_empty))
print(get_max_water_container_bf(heights_single))
print(get_max_water_container_bf(heights))
print(get_max_water_container_bf(heights_2))

