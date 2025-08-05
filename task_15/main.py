# def reverseWord(w):
#   return ' '.join(w.split()[::-1])

def reverse_string(string : str) -> str:
    split_words = string.split()
    result = ""
    for word in reversed(split_words):
        result += word + " "
    return result

text = "My name is Michele"
print(reverse_string(text))