import re
# Введення/виведення рядка
row=input("\nInput your string: ")
print("\nYour string is: ", row)

# Виділення цифр для слів
extract_letter=" ".join(re.split("[0-9]", row))
extract_number="".join(re.split("[a-zA-Z]", row))
# Простий розподіл комами
extract_com_let=", ".join(extract_letter.split())
extract_com_num=", ".join(extract_number.split())

print("\nAll numbers: ", str(extract_com_num))

print("\nAll words between numbers: ", str(extract_com_let))
# Виведення першої та останньої букви в першому реєстрі
for let in extract_letter.split():
    print("\nCapital first and last letters of each word: ", let[0].upper() + let[-1].upper(), end="\n")

# Робимо з рядка список, щоб потім звертатися до конкретних елементів
new_num_max=list(map(int, extract_number.split()))
# Максимальне значення нового списку
max_num=max(new_num_max)
# Виведення максимального значення
print("\nMax element from numbers is: ", max_num)
# Число до степення
for element in new_num_max:
    if element != max_num:
        element=element**new_num_max.index(element)
        print("\nnumbers power to its index: ", element)
    else:
        continue