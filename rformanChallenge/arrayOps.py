# This module is for functions defined to operate on arrays

# flatten a nested array
def flatten(array):
    """recursively flattens each item in a potentially nested list and returns the result
        Parameters:
            array (list): an arbitrarily nested array of integers

        Returns:
            (list) a flat array of integers
    """
    print "Array: ", array
    # if list is empty return empty list
    if array == []:
        return array
    # if 1st list item is a sublist, call flatten on it, concatenate to the flattened version of the rest of the potentially nested list, return result.
    if isinstance(array[0], list):
        return flatten(array[0]) + flatten(array[1:])
    # if the 1st item is not a sublist, return an array everything before the 2nd item, with flattened version the rest of the potentially nested list concatenated.
    return array[:1] + flatten(array[1:])
