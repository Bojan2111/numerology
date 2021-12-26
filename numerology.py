LETTERS = {'A': 1,	'B': 2,	'C': 3,	'D': 4,	'E': 9,
           'F': 8,	'G': 3,	'H': 8,	'I': 1,	'J': 1,
           'K': 2,	'L': 3,	'M': 4,	'N': 5,	'O': 7,
           'P': 8,	'Q': 1,	'R': 2,	'S': 6,	'T': 9,
           'U': 6,	'V': 6,	'W': 6,	'X': 5,	'Y': 1,
           'Z': 7}


def name_to_number(name):
    name_num_sum = 0
    for i in name.upper():
        if i in LETTERS:
            name_num_sum += LETTERS[i]
    return name_num_sum % 9 if name_num_sum % 9 != 0 else 9


def birth_num(birthday):
    x = birthday.split("-")
    res = 0
    for i in x:
        res += int(i)
    return res % 9 if res % 9 != 0 else 9


a = input("Enter your name: ")
b = input("Enter your birth date (DD-MM-YYYY): ")

print(name_to_number(a))
print(birth_num(b))
