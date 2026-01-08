def extract_border_elements(arr: list) -> list:
    '''
    Given a list of integers, returns a new list with only the first and last elements
    if the list has more than one element. Returns the single element if the list has
    only one element, and an empty list if the input list is empty.

    Eg.
    extract_border_elements([1, 2, 3, 4]) -> [1, 4]
    extract_border_elements([5]) -> [5]
    extract_border_elements([]) -> []

    Args:
        arr (list): List of integers.

    Returns:
        list: List containing the first and last elements or appropriate value.
    '''
    
    
    if not arr:
        return []
    elif len(arr) == 1:
        return arr
    else:
        return [arr[0], arr[-1]]
    
# #Another method:

# def extract_border_elements(arr: list) -> list:
#     '''
#     Given a list of integers, returns a new list with only the first and last elements
#     if the list has more than one element. Returns the single element if the list has
#     only one element, and an empty list if the input list is empty.

#     Eg.
#     extract_border_elements([1, 2, 3, 4]) -> [1, 4]
#     extract_border_elements([5]) -> [5]
#     extract_border_elements([]) -> []

#     Args:
#         arr (list): List of integers.

#     Returns:
#         list: List containing the first and last elements or appropriate value.
#     '''
#     num=len(arr)
#     if num==0:
#         return arr 
#     elif num==1:
#         return arr
#     else:
#         return [arr[0],arr[-1]]
    
#  Extract Border Elements from a List
# Write a function extract_border_elements that takes a list of integers as input and returns a new list containing only the first and last elements if the list has more than one element.

# If the list has only one element, return it as a single-element list.
# If the list is empty, return an empty list.
# NOTE: This is a function type question, you don't have to take input or print the output, just complete the required function definition.

# Example
# extract_border_elements([1, 2, 3, 4]) → [1, 4]
# extract_border_elements([5]) → [5]
# extract_border_elements([]) → []
# extract_border_elements([7, 8, 9, 10, 11]) → [7, 11]   
    
