printed_strings = set()

def modern_print(s):
    # Проверяем, была ли строка уже выведена
    if s not in printed_strings:
        print(s)  
        printed_strings.add(s)  
modern_print("Hello, world!")
modern_print("Hello, world!")  
modern_print("Goodbye, world!")
