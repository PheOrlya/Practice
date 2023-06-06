def convert_to_integer(char):
    if char.isdigit():
        return int(char)
    else:
        return None


input_char = input("Введите символ: ")
if len(input_char) == 1:
    result = convert_to_integer(input_char)
    if result is not None:
        print("Значение цифры:", result)
    else:
        print("Введенный символ не является цифрой.")
else:
    print("Пожалуйста, введите только один символ.")