def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)
    except ZeroDivisionError:
        print("Error: Cannot calculate the average of an empty list.")
        return None


data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []

print(f"Average of data1:", calculate_average(data1))
print(f"Average of data2:", calculate_average(data2))
print(f"Average of data3:", calculate_average(data3))


def get_list_element(my_list, index):
    try:
        return my_list[index]
    except (IndexError, TypeError) as e:
        print(f"Error: {e}")
        return None


print("Valid test:", get_list_element([10, 20, 30], 1))
print("Out of bounds test:", get_list_element([10, 20, 30], 5))
print("Incorrect type test:", get_list_element("not_a_list", 1))
