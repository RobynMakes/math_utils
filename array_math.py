"""Performs maths regarding data sets stored in arrays or lists."""
import math


def average(array):
    """Calculates the average value from an array of numbers

    Keyword arguments:
        array: the array to calculate the average from

    Returns:
        the average of the given array
    """
    pos = 0
    total = 0

    # Summing all array values
    while True:
        total += array[pos]
        pos += 1

        # if the value of pos == length of the array -> break the loop
        if pos == len(array):
            break

    avg = total / len(array)
    return avg


def median(array):
    """Calculates the median value from an array of numbers

    Keyword arguments:
        array: the array to calculate the median from

    Returns:
        the median of the given array
    """
    sorted_array = sorted(array)
    half_length = (len(sorted_array) - 1) / 2
    if half_length.is_integer():
        med = sorted_array[int(half_length)]
    else:
        med = average([sorted_array[math.floor(half_length)], sorted_array[math.ceil(half_length)]])
    return med