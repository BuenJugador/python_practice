# def reverse_word(word : str) -> str:
#     return word[::-1]

def reverse_word(word : str) -> str:
    """
    alternative way to reverse word without using slicing
    :param word: word to reverse
    :return: reversed word
    """
    result = ""
    for i in word:
        result = i + result
    return result

input_word = input("Enter a word: ")
if input_word == reverse_word(input_word):
    print(f"{input_word} is palindrome")
else:
    print(f"{input_word} is not palindrome")