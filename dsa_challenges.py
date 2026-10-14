# Filter and Sort Even numbers
def filter_and_sort_evens(numbers):
    even = []
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


print(count_character_frequency("YOYOYO"))
