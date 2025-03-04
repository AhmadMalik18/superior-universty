#Task 1: LUHN Algorithm (Credit Card Validation)

def luhn_algorithm(card_number):
    card_number = str(card_number)
    if not card_number.isdigit():
        return False
    total = 0
    reverse = card_number[::-1]
    for i, digit in enumerate(card_number):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
        return total % 10 == 0
card_number = "1234 6744 7543 5334"
print(luhn_algorithm(card_number))

#Task 2: Remove Punctuations from UserInput String (without using remove function)
import string
def remove_punctuations(input_string):
    translation_table = str.maketrans("", "", string.punctuation)
    return input_string.translate(translation_table)
input_string = "Hello, World! How are you?"
result = remove_punctuations(input_string)
print(result)

#Task 3: Sort text (word) in Alphabetical Order without using sort() function (Using ASCII)

def sort_text(text):
    words = text.split()
    n = len(words)
    for i in range(n):
        for j in range(i+1, n):
            if words[j].lower() > words[i].lower():
                words[i], words[j] = words[j], words[i]
    return " ".join(words)
text = "Hello, World! Whats going on?"
result = sort_text(text)
print(result)
