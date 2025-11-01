import tkinter as tk
import random
from tkinter import messagebox


def quit():
    window.destroy()


def turns_countdown():
    global TURNS
    TURNS -= 1
    return TURNS


def word_choose():
    with open('words.txt', 'r') as words_list:
        words = []
        for word in words_list:
            words.append(word)
    myword = random.choice(words)
    return myword[:5]


def guess():
    global WORD_TO_SHOW
    global USED_LETTERS
    letter = letter_entry.get()
    if len(letter) != 1 or letter.isalpha() == False:
        tk.messagebox.showwarning('Неверный ввод!', 'Нужно ввести букву!')
        return 0
    letter = letter.upper()
    letter_entry.delete(-1)
    turns_countdown()
    turns_label.configure(text=f'Осталось ходов: {TURNS}')

    USED_LETTERS += f'{letter} '
    log_label.configure(text=f'Использовано: {USED_LETTERS}')

    if letter in WORD_TO_GUESS:
        word_buf = WORD_TO_SHOW
        WORD_TO_SHOW = ''
        for i in range(5):
            if WORD_TO_GUESS[i] == letter:
                WORD_TO_SHOW += letter
            else:
                WORD_TO_SHOW += word_buf[i]
    word_label.configure(text=WORD_TO_SHOW)

    if WORD_TO_GUESS == WORD_TO_SHOW:
        tk.messagebox.showinfo('Победа!', 'Вы угадали слово!')
    if TURNS == 0 and WORD_TO_GUESS != WORD_TO_SHOW:
        tk.messagebox.showerror('Не победа(', 'Вы не угадали слово...')


WORD_TO_GUESS = word_choose()
WORD_TO_SHOW = '-----'
TURNS = 10
USED_LETTERS = ''

window = tk.Tk()
window.title('My app')
window.geometry('300x300')
window.resizable(0, 0)
bg_img = tk.PhotoImage(file='gradient.png')

bg_label = tk.Label(window, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

word_label = tk.Label(window,
                      text="-----",
                      font=('Cansolas', 50),
                      bg='red',
                      fg='white')
word_label.place(x=0, y=0, relwidth=1)

letter_label = tk.Label(window,
                        text="Введите букву:",
                        font=("Verdana 16"))
letter_label.place(relx=0.1, rely=0.33)
letter_entry = tk.Entry(window,
                        width=5,
                        font=("Verdana 16"))
letter_entry.insert(0, 'a')
letter_entry.place(relx=0.7, rely=0.33)

turns_label = tk.Label(window,
                      text=f'Осталось ходов: {TURNS}',
                      font=("Verdana 16"))
turns_label.place(relx=0.1, rely=0.5)

btn_guess = tk.Button(window,
                      text="OK",
                      width=15,
                      command=guess)
btn_guess.place(relx=0.1, rely=0.7)
btn_exit = tk.Button(window,
                      text="Cancel",
                      width=15,
                      command=quit)
btn_exit.place(relx=0.55, rely=0.7)

log_label = tk.Label(window,
                      text="Использовано: ")
log_label.place(relx=0.5, rely=0.9, anchor='center')

window.mainloop()