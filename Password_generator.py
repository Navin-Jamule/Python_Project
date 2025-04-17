letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

final_password = []
# easy version
import random
order = [0,1,2]
for i in range(len(order)):
    sq = random.choice(order)
    if sq == 0:
        for x in range(nr_letters):
            final_password.append(random.choice(letters))
    if sq == 1:
        for x in range(nr_numbers):
            final_password.append(random.choice(numbers))
    else:
        for x in range(nr_symbols):
            final_password.append(random.choice(symbols))
    
result = ''.join(final_password)
print(result)
    
    