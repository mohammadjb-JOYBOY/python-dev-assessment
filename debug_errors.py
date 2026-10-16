def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)
    except ZeroDivisionError:
        print("Error: Cannot calculate the average of an empty list.")
        return None


data1 = [20, 50, 20]
data2 = [20, 15, 20, 25]
data3 = []

print("Average 1:", calculate_average(data1))
print("Average 2:", calculate_average(data2))
print("Average 3:", calculate_average(data3))


def get_list_element(my_list, index):
    try:
        return my_list[index]
    except (IndexError, TypeError) as e:
        print(f"Error: {e}")
        return None


print("Valid test:", get_list_element([10, 20, 30], 1))
print("Out of bounds test:", get_list_element([10, 20, 30], 5))
print("Incorrect type test:", get_list_element("not_a_list", 1))
