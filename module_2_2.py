first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

if first == second == third:
    print(f"{first} {second} {third}")
elif first == second:
    print(f"{first} {second}")
elif first == third:
    print(f"{first} {third}")
elif second == third:
    print(f"{second} {third}")
else:
    print(0)