numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
missing_value = None
for i, num in enumerate(numbers):
    if num is None:
        missing_index = i
        break
total_sum = sum(num for num in numbers if num is not None)
count = len(numbers)
if missing_index is not None:
    count -= 1
average = total_sum / count
# TODO заменить значение пропущенного элемента средним арифметическим
if missing_index is not None:
    numbers[missing_index] = average
print("Измененный список:", numbers)
