
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# random_letters = letters[random.randint(0, len(letters))]
# random_numbers = numbers[random.randint(0, len(numbers))]
# random_symbols = symbols[random.randint(0, len(symbols))]
# print(password_selection, sep='')
# print(*[random.randint(1, 10) for _ in range(4)])
cleaned_letters = [(letters[random.randint(0, len(letters)-1)]) for _ in range (0, nr_letters)]
cleaned_numbers = [(numbers[random.randint(0, len(numbers)-1)]) for _ in range (0, nr_numbers)]
cleaned_symbols = [(symbols[random.randint(0, len(symbols)-1)]) for _ in range (0, nr_symbols)]
combination = cleaned_letters + cleaned_numbers + cleaned_symbols
random.shuffle(combination)
password = ''.join(combination)
print(f"Your Password is: {password}")

