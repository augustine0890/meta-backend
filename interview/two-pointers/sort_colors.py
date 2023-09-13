"""
Given an array, colors, which contains a combination of the following three elements:
    0 (red), 1 (white), and 2 (blue)
Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue.
Naive approach would be to sort the array --> O(nlogn)
Time O(n) and Space O(1)
"""


def sort_colors(colors):
    red, white = 0, 0
    blue = len(colors) - 1
    while white <= blue:
        if colors[white] == 0:
            colors[red], colors[white] = colors[white], colors[red]
            white += 1
            red += 1
        elif colors[white] == 1:
            white += 1
        else:
            colors[blue], colors[white] = colors[white], colors[blue]
            blue -= 1
    return colors

# Driver code


inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0],
          [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]
# Iterate over the inputs and print the sorted array for each
for i in range(len(inputs)):
    print(i + 1, ".\tcolors:", inputs[i].copy(),
          "\n\n\tThe sorted array is:", sort_colors(inputs[i]))
    print("-" * 100)
