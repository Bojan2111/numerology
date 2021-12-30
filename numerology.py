LETTERS = {"english": {'A': 1,	'B': 2,	'C': 3,	'D': 4,	'E': 9,
                       'F': 8,	'G': 3,	'H': 8,	'I': 1,	'J': 1,
                       'K': 2,	'L': 3,	'M': 4,	'N': 5,	'O': 7,
                       'P': 8,	'Q': 1,	'R': 2,	'S': 6,	'T': 9,
                       'U': 6,	'V': 6,	'W': 6,	'X': 5,	'Y': 1,
                       'Z': 7},
           "srpski": {'A': 1, 'B': 2, 'C': 3, 'Č': 9, 'Ć': 9,
                      'D': 4, 'DŽ': 1, 'Đ': 8, 'E': 9, 'F': 8,
                      'G': 3, 'H': 8, 'I': 1, 'J': 1, 'K': 2,
                      'L': 3, 'LJ': 7, 'M': 4, 'N': 5, 'NJ': 2,
                      'O': 7, 'P': 8, 'R': 2, 'S': 6, 'Š': 3,
                      'T': 9, 'U': 6, 'V': 6, 'Z': 7, 'Ž': 7}}

# TODO correct the letters from serbian alphabet (DŽ, LJ, NJ)


def num_reduce(number):
    return number % 9 if number % 9 != 0 else 9


def name_to_number(name, lang):
    name_num_sum = 0
    for i in name.upper():
        if i in LETTERS[lang]:
            name_num_sum += LETTERS[lang][i]
    return num_reduce(name_num_sum)


def vowels(name, lang, vowels=True):
    vowels_list = 'AEIOUY'
    vowels_sum = 0
    if vowels:
        for i in name.upper():
            if i in LETTERS[lang] and i in vowels_list:
                vowels_sum += LETTERS[lang][i]
    else:
        for i in name.upper():
            if i in LETTERS[lang] and i not in vowels_list:
                vowels_sum += LETTERS[lang][i]
    return num_reduce(vowels_sum)


def birth_num(day, month, year):
    res = day + month + year
    return num_reduce(res)


lang_choice = input(
    "Please choose alphabet of your name (1-English, 2-Srpski): ")
language = 'english' if lang_choice == 1 else 'srpski'
full_name = input("Enter your full name: ")
birth_day = int(input("Enter the day of your birth (1-31): "))
birth_month = int(input("Enter the month of your birth (1-12): "))
birth_year = int(input("Enter the year of your birth (YYYY): "))

life_path = birth_num(birth_day, birth_month, birth_year)
expression_number = name_to_number(full_name, language)
personality = vowels(full_name, language, False)
soul_urge = vowels(full_name, language)
accomplishment = num_reduce(life_path + expression_number)
pc_base = [num_reduce(birth_month), num_reduce(
    birth_day), num_reduce(birth_year)]
p1 = num_reduce(pc_base[0] + pc_base[1])
p2 = num_reduce(pc_base[1] + pc_base[2])
p3 = num_reduce(p1 + p2)
p4 = num_reduce(pc_base[0] + pc_base[2])
c1 = num_reduce(abs(pc_base[0]-pc_base[1]))
c2 = num_reduce(abs(pc_base[1]-pc_base[2]))
c3 = num_reduce(abs(c1-c2))
c4 = num_reduce(abs(pc_base[0]-pc_base[2]))
cycle1 = 36 - life_path
cycle2 = cycle1 + 9
cycle3 = cycle2 + 9

cycles = f"""Cycle 1: from 0 to {cycle1}, pinnacle - {p1}, life challenge - {c1};
Cycle 2: from {cycle1} to {cycle2}, pinnacle - {p2}, life challenge - {c2};
Cycle 3: from {cycle2} to {cycle3}, pinnacle - {p3}, life challenge - {c3};
Cycle 4: from {cycle3} to the rest of your life, pinnacle - {p4}, life challenge - {c4};"""

info = f"""Hi, {full_name}.
Your Life Path number is {life_path},
Your expression number is {expression_number},
Your personality number is {personality},
Your soul urge number is {soul_urge},
Your accomplishment number is {accomplishment}
"""
print(info)
print(cycles)
