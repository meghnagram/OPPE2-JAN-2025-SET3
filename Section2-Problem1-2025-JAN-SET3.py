def words_with_consecutive_letters(words):
    
    
    result = []
    for word in words:
        lower_word = word.lower()  # Case-insensitive
        for i in range(len(lower_word) - 1):
            if lower_word[i] == lower_word[i + 1]:
                result.append(word)
                break
    return result
    
# #Another Method:

# def words_with_consecutive_letters(words):
#     l=[]
#     for j in words:
#         for i in range(len(j)-1):
#             if j[i]==j[i+1]:
#                 l.append(j)
#                 break
#     return l
            
            
#   Words with Consecutive Identical Letters
# Write a function words_with_consecutive_letters(words) that takes a list of words and returns a list of words that contain at least one pair of consecutive identical letters (e.g., "hello", "apple"). The function should be case-insensitive.

# The order of the words in the result should be same as they are present in the input.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Examples:
# words = ["hello", "apple", "ball", "test", "cat"] -> ["hello", "apple", "ball"]
# Explanation: "hello" has 'll', "apple" has 'pp', "ball" has 'll'.
# words = ["sky", "fly", "run", "jump"] -> []
Explanation: No words have consecutive identical letters.  
