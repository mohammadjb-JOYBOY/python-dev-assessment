# Filter and Sort Even numbers
def filter_sort_even(num):
    even = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
    even.sort()
    return even


# Count the character frequency
def count_char(str):
    Res = {}
    lower_text = str.lower()
    for i in lower_text:
        if i in Res:
            Res[i] += 1
        else:
            Res[i] = 1
    return Res


print(count_char("YOYOYO"))
