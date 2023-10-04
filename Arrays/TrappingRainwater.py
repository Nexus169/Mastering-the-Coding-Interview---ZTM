
def get_trapped_rainwater(height):
    """
    Function calculating the amount of rainwater collected in a array storing topographical heights as positive integers, using a more optimized solution
    """
    total_rainwater = 0

    left_side_index = 0
    right_side_index = len(height) - 1
    max_left = max_right = 0

    while left_side_index < right_side_index:
        left_height = height[left_side_index]
        right_height = height[right_side_index]

        if left_height <= right_height:              # if the left side is shorter, need to determine if there exists a wall to the left that our current column
            left_side_index += 1                     # if there is, then need to include water on top of current line, otherwise do the same logic for right side
            if left_height < max_left:
                total_rainwater += max_left - left_height
            max_left = max(left_height, max_left)
        else:
            right_side_index -= 1
            if right_height < max_right:
                total_rainwater += max_right - right_height
            max_right = max(right_height, max_right)

    return total_rainwater


def get_trapped_rainwater_bruteforce(height):
    """
    Function calculating the amount of rainwater collected in a array storing topographical heights as positive integers, using a bruteforce solution
    """
    total_rainwater = 0

    for current_line_index in range(len(height)):
        current_height = height[current_line_index]

        max_left = max_right = 0                                    # get the tallest lines to the left and right of current line
        for left_line_index in range(0, current_line_index):
            max_left = max(max_left, height[left_line_index])
        for right_line_index in range(current_line_index, len(height)):
            max_right = max(max_right, height[right_line_index])

        current_water = min(max_left, max_right) - current_height   # calculate the amount of water stored on top of current line, it will be whichever
        total_rainwater += max(current_water, 0)                              # is the lowest of left and right minus our current line's height

    return total_rainwater



chart = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
middle_chart = [5, 0, 3, 0, 0, 0, 2, 3, 4, 2, 1]
empty_chart = []
single_chart = [1]

print("Trapped Water Bruteforce")
print(get_trapped_rainwater_bruteforce(chart))          # 8
print(get_trapped_rainwater_bruteforce(middle_chart))   # 20
print(get_trapped_rainwater_bruteforce(empty_chart))    # 0
print(get_trapped_rainwater_bruteforce(single_chart))   # 0

print("Trapped Water Optimized")
print(get_trapped_rainwater(chart))          # 8
print(get_trapped_rainwater(middle_chart))   # 20
print(get_trapped_rainwater(empty_chart))    # 0
print(get_trapped_rainwater(single_chart))   # 0
