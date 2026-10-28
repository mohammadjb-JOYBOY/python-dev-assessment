# Filter and Sort Even numbers
def filter_and_sort_evens(numbers):
    even = [3, 1, 4, 7, 1, 5, 9, 2, 6, 8]
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    even.sort()
    return even


# Count the character frequency
def count_character_frequency(text):
    Res = {}
    lower_text = text.lower()
    for i in lower_text:
        if i in Res:
            Res[i] += 1
        else:
            Res[i] = 1
    return Res


number_input = [3, 1, 4, 7, 1, 5, 9, 2, 6, 8]
text_input = "This my task for Basic Data Structures & Algorithms"

print(filter_and_sort_evens(number_input))
print(count_character_frequency(text_input))