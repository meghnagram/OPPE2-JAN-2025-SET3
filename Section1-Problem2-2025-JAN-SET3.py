def absolute_time_difference(time1, time2):
    """
    Calculates the absolute time difference between two given times in the format HH:MM.

    Args:
        time1 (str): The first time in the format HH:MM.
        time2 (str): The second time in the format HH:MM.

    Returns:
        str: The absolute time difference between the two input times in the format HH:MM.

    Examples:
        >>> absolute_time_difference('14:30', '06:45')
        '07:45'
        >>> absolute_time_difference('06:45', '14:30')
        '07:45'
        >>> absolute_time_difference('23:59', '00:00')
        '23:59'
    """
    
    
    time1 = int(time1[:2])*60 + int(time1[-2:])
    time2 = int(time2[:2])*60 + int(time2[-2:])
    diff = abs(time2 - time1)
    return f"{diff//60:02}:{diff%60:02}"
    
# #Another Method:

# def hr_to_min(time1):
#     return(int(time1[0:2])*60+int(time1[-2:]))
    
# def min_to_hr(min):
#     return str(f"{min//60:02d}")+':'+str(f"{min%60:02d}")

# def absolute_time_difference(time1, time2):
#     """
#     Calculates the absolute time difference between two given times in the format HH:MM.

#     Args:
#         time1 (str): The first time in the format HH:MM.
#         time2 (str): The second time in the format HH:MM.

#     Returns:
#         str: The absolute time difference between the two input times in the format HH:MM.

#     Examples:
#         >>> absolute_time_difference('14:30', '06:45')
#         '07:45'
#         >>> absolute_time_difference('06:45', '14:30')
#         '07:45'
#         >>> absolute_time_difference('23:59', '00:00')
#         '23:59'
#     """
#     min1=hr_to_min(time1)
#     min2=hr_to_min(time2)
    
#     diff=abs(min1-min2)
    
#     return min_to_hr(diff)
    
#    Absolute Time Difference Between Two Times
# Write a function absolute_time_difference that takes two time strings in the format HH:MM as input and returns the absolute time difference between them in the same format.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# For example, given the times 14:30 and 06:45, the function should return 07:45, because this is the absolute time difference between the two input times.

# HINT: You might want to use formatted string with {val:02} for padding time with leading 0 in case of single digit

# Examples

# >>> absolute_time_difference('14:30', '06:45')
# '07:45'
# >>> absolute_time_difference('06:45', '14:30')
# '07:45'
# >>> absolute_time_difference('02:30', '03:10')
# '00:40'
# >>> absolute_time_difference('23:59', '00:00')
# '23:59' 
    
    
