from tkinter import *
from tkinter import ttk


class Numerology:

    def __init__(self, master):
        master.geometry('700x480')
        master.title('Numerology')

        self.input_frame = ttk.LabelFrame(
            master, width=200, height=300, text='Input Data')
        self.input_frame.grid(column=0, row=0, padx=10, ipadx=5, ipady=5)

        self.result_frame = ttk.LabelFrame(
            master, width=300, height=300, text='Results')
        self.result_frame.grid(column=3, row=0, padx=10,
                               sticky=N, ipadx=5, ipady=5)

        self.name_label = ttk.Label(
            self.input_frame, text='Full Name: ', anchor='w').grid(row=1, column=0, sticky=W+E)
        self.name_entry = ttk.Entry(
            self.input_frame, width=30)
        self.name_entry.grid(row=1, column=1, sticky=W+E, pady=5)

        self.date_label = ttk.Label(
            self.input_frame, text='Date of birth: ').grid(row=2, column=0, sticky=W+E)
        self.date_entry = ttk.Entry(self.input_frame, width=10)
        self.date_entry.grid(row=2, column=1, sticky=W+E, pady=5)

        self.alphabet = StringVar()
        ttk.Label(self.input_frame, text='Alphabet:').grid(
            row=3, column=0, sticky=W+E)
        ttk.Radiobutton(self.input_frame, text='English', variable=self.alphabet,
                        value='english').grid(row=4, column=0, sticky=W+E, padx=20)
        ttk.Radiobutton(self.input_frame, text='Serbian', variable=self.alphabet,
                        value='srpski').grid(row=5, column=0, sticky=W+E, padx=20)

        self.calculate_btn = ttk.Button(
            self.input_frame, command=self.calculate, text='Calculate').grid(row=6, column=0, columnspan=2, pady=10)

        ttk.Label(self.result_frame, text='Life Path: ').grid(
            row=1, column=3, sticky=W+E)
        self.entry_lp = ttk.Entry(self.result_frame, width=5)
        self.entry_lp.grid(row=1, column=4, sticky=W+E, pady=5)

        ttk.Label(self.result_frame, text='Expression: ').grid(
            row=2, column=3, sticky=W+E)
        self.entry_ex = ttk.Entry(self.result_frame, width=5)
        self.entry_ex.grid(row=2, column=4, sticky=W+E, pady=5)

        ttk.Label(self.result_frame, text='Personality: ').grid(
            row=3, column=3, sticky=W+E)
        self.entry_pe = ttk.Entry(self.result_frame, width=5)
        self.entry_pe.grid(row=3, column=4, sticky=W+E, pady=5)

        ttk.Label(self.result_frame, text='Soul urge: ').grid(
            row=4, column=3, sticky=W+E)
        self.entry_su = ttk.Entry(self.result_frame, width=5)
        self.entry_su.grid(row=4, column=4, sticky=W+E, pady=5)

        ttk.Label(self.result_frame, text='Accomplishment: ').grid(
            row=5, column=3, sticky=W+E)
        self.entry_ac = ttk.Entry(self.result_frame, width=5)
        self.entry_ac.grid(row=5, column=4, sticky=W+E, pady=5)

        # Table header - 1st row
        ttk.Label(self.result_frame, text='Cycle', relief=SOLID,
                  background='white').grid(row=6, column=4, ipady=1, ipadx=2, sticky=W+E)
        ttk.Label(self.result_frame, text='From', relief=SOLID,
                  background='white').grid(row=6, column=5, ipady=1, ipadx=2, sticky=W+E)
        ttk.Label(self.result_frame, text='To', relief=SOLID,
                  background='white').grid(row=6, column=6, ipady=1, ipadx=2, sticky=W+E)
        ttk.Label(self.result_frame, text='Pinnacle', relief=SOLID,
                  background='white').grid(row=6, column=7, ipady=1, ipadx=2, sticky=W+E)
        ttk.Label(self.result_frame, text='Challenge', relief=SOLID,
                  background='white').grid(row=6, column=8, ipady=1, ipadx=2, sticky=W+E)

        # Table data - 2nd row
        ttk.Label(self.result_frame, text='1', relief=SOLID,
                  background='white').grid(row=7, column=4, ipady=1, ipadx=2, sticky=W+E)
        ttk.Label(self.result_frame, text='0', relief=SOLID,
                  background='white').grid(row=7, column=5, ipady=1, ipadx=2, sticky=W+E)
        self.entry_cy1_end = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_cy1_end.grid(row=7, column=6, ipady=1, ipadx=2, sticky=W+E)
        self.entry_p1 = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_p1.grid(row=7, column=7, ipady=1, ipadx=2, sticky=W+E)
        self.entry_c1 = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_c1.grid(row=7, column=8, ipady=1, ipadx=2, sticky=W+E)

        # Table data - 3rd row
        ttk.Label(self.result_frame, text='2', relief=SOLID,
                  background='white').grid(row=8, column=4, ipady=1, ipadx=2, sticky=W+E)
        self.entry_cy2_start = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_cy2_start.grid(
            row=8, column=5, ipady=1, ipadx=2, sticky=W+E)
        self.entry_cy2_end = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_cy2_end.grid(row=8, column=6, ipady=1, ipadx=2, sticky=W+E)
        self.entry_p2 = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_p2.grid(row=8, column=7, ipady=1, ipadx=2, sticky=W+E)
        self.entry_c2 = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_c2.grid(row=8, column=8, ipady=1, ipadx=2, sticky=W+E)

        # Table data - 4th row
        ttk.Label(self.result_frame, text='3', relief=SOLID,
                  background='white').grid(row=9, column=4, ipady=1, ipadx=2, sticky=W+E)
        self.entry_cy3_start = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_cy3_start.grid(
            row=9, column=5, ipady=1, ipadx=2, sticky=W+E)
        self.entry_cy3_end = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_cy3_end.grid(row=9, column=6, ipady=1, ipadx=2, sticky=W+E)
        self.entry_p3 = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_p3.grid(row=9, column=7, ipady=1, ipadx=2, sticky=W+E)
        self.entry_c3 = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_c3.grid(row=9, column=8, ipady=1, ipadx=2, sticky=W+E)

        # Table data - 5th row
        ttk.Label(self.result_frame, text='4', relief=SOLID,
                  background='white').grid(row=10, column=4, ipady=1, ipadx=2, sticky=W+E)
        self.entry_cy4_start = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_cy4_start.grid(
            row=10, column=5, ipady=1, ipadx=2, sticky=W+E)
        ttk.Label(self.result_frame, text='end of life', relief=SOLID,
                  background='white').grid(row=10, column=6, ipady=1, ipadx=2, sticky=W+E)
        self.entry_p4 = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_p4.grid(row=10, column=7, ipady=1, ipadx=2, sticky=W+E)
        self.entry_c4 = ttk.Label(
            self.result_frame, text='', relief=SOLID, background='white')
        self.entry_c4.grid(row=10, column=8, ipady=1, ipadx=2, sticky=W+E)

        self.result_cycles = ttk.Label(self.result_frame, text='')
        self.result_cycles.grid(row=4, column=4)

        self.LETTERS = {"english": {'A': 1,	'B': 2,	'C': 3,	'D': 4,	'E': 9,
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

    def num_reduce(self, number):
        return number % 9 if number % 9 != 0 else 9

    def name_to_number(self, name, lang):
        name_num_sum = 0
        for i in name:
            if i in self.LETTERS[lang]:
                name_num_sum += self.LETTERS[lang][i]
        return self.num_reduce(name_num_sum)

    def vowels(self, name, lang, vowels=True):
        vowels_list = 'AEIOUY'
        vowels_sum = 0
        if vowels:
            for i in name:
                if i in self.LETTERS[lang] and i in vowels_list:
                    vowels_sum += self.LETTERS[lang][i]
        else:
            for i in name:
                if i in self.LETTERS[lang] and i not in vowels_list:
                    vowels_sum += self.LETTERS[lang][i]
        return self.num_reduce(vowels_sum)

    def birth_num(self, day, month, year):
        res = day + month + year
        return self.num_reduce(res)

    def name_to_arr(self, name):
        name = name.upper()
        test_letters = ['DŽ', 'LJ', 'NJ']
        conv_letters = ['*', '&', '$']
        name_arr = []
        for i in range(0, len(test_letters)):
            name = name.replace(test_letters[i], conv_letters[i])
        for i in name:
            if i == '*':
                name_arr.append('DŽ')
            elif i == '&':
                name_arr.append('LJ')
            elif i == '$':
                name_arr.append('NJ')
            else:
                name_arr.append(i)
        return name_arr

    def calculate(self):
        language = self.alphabet.get()
        birth_dat = self.date_entry.get()
        birth_date = birth_dat.split('-')
        birth_day = int(birth_date[0])
        birth_month = int(birth_date[1])
        birth_year = int(birth_date[2])
        full_name = self.name_to_arr(self.name_entry.get(
        )) if language == 'srpski' else self.name_entry.get().upper()
        life_path = self.birth_num(birth_day, birth_month, birth_year)
        self.entry_lp.insert(0, life_path)
        expression_number = self.name_to_number(full_name, language)
        self.entry_ex.insert(0, expression_number)
        personality = self.vowels(full_name, language, False)
        self.entry_pe.insert(0, personality)
        soul_urge = self.vowels(full_name, language)
        self.entry_su.insert(0, soul_urge)
        accomplishment = self.num_reduce(life_path + expression_number)
        self.entry_ac.insert(0, accomplishment)
        pc_base = [self.num_reduce(birth_month), self.num_reduce(
            birth_day), self.num_reduce(birth_year)]
        p1 = self.num_reduce(pc_base[0] + pc_base[1])
        p2 = self.num_reduce(pc_base[1] + pc_base[2])
        p3 = self.num_reduce(p1 + p2)
        p4 = self.num_reduce(pc_base[0] + pc_base[2])
        c1 = self.num_reduce(abs(pc_base[0]-pc_base[1]))
        c2 = self.num_reduce(abs(pc_base[1]-pc_base[2]))
        c3 = self.num_reduce(abs(c1-c2))
        c4 = self.num_reduce(abs(pc_base[0]-pc_base[2]))
        cycle1 = 36 - life_path
        cycle2 = cycle1 + 9
        cycle3 = cycle2 + 9
        self.entry_cy1_end.config(text=cycle1)
        self.entry_cy2_start.config(text=cycle1)
        self.entry_cy2_end.config(text=cycle2)
        self.entry_cy3_start.config(text=cycle2)
        self.entry_cy3_end.config(text=cycle3)
        self.entry_cy4_start.config(text=cycle3)
        self.entry_p1.config(text=p1)
        self.entry_p2.config(text=p2)
        self.entry_p3.config(text=p3)
        self.entry_p4.config(text=p4)
        self.entry_c1.config(text=c1)
        self.entry_c2.config(text=c2)
        self.entry_c3.config(text=c3)
        self.entry_c4.config(text=c4)


def main():
    root = Tk()
    numerology = Numerology(root)
    root.mainloop()


if __name__ == '__main__':
    main()
