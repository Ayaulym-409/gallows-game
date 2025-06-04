import tkinter as tk
import random

root = tk.Tk()
root.geometry('1000x500')
root.title('Виселица')

possible_variant = ['pepsi', 'spongebob', 'apple', 'dead']

attempt = 10
gameover = False
word = random.choice(possible_variant)
user = []
buttons = []

hellotext = tk.Label(root, text='Hello, This is Gallows!', font=('Arial', 15))
hellotext.pack(padx=10, pady=10)

ans = tk.Label(root, text='', font=('Arial', 15))
ans.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.pack()

label1 = tk.Label(root, text='Try to guess the word! (one letter)', font=('Arial', 10))
label1.pack(padx=10, pady=10)

user_input = tk.Entry(root)
user_input.pack(padx=10, pady=10)

label2 = tk.Label(root, text='У вас осталось попыток:', font=('Arial', 10))
label2.pack(padx=10, pady=5)
label3 = tk.Label(root, text=str(attempt), font=('Arial', 10))
label3.pack(padx=10, pady=5)

guessed_label = tk.Label(root, text='Угаданные буквы: ', font=('Arial', 10))
guessed_label.pack(padx=10, pady=5)

# Кнопка начать снова
startagain_button = tk.Button(root, text='Начать снова', font=('Arial', 15), command=lambda: reset_game())
startagain_button.pack_forget()


# Обработка ввода
def input_all():
    global attempt, gameover
    user_let = user_input.get().lower()

    if not user_let or gameover:
        return

    if len(user_let) != 1 or not user_let.isalpha():
        ans.config(text='Введите ОДНУ БУКВУ!')
        user_input.delete(0, tk.END)
        return

    if user_let in word and user_let not in user:
        user.append(user_let)
        ans.config(text='Угадали!', fg='green')
        for i, letter in enumerate(word):
            if letter == user_let:
                buttons[i].config(text=letter)
    elif user_let in user:
        ans.config(text='Эта буква уже угадана!', fg='orange')
    else:
        ans.config(text='Не угадали!', fg='red')
        attempt -= 1
        label3.config(text=str(attempt))

    guessed_label.config(text='Угаданные буквы: ' + ', '.join(user))
    user_input.delete(0, tk.END)

    if attempt == 0:
        ans.config(text='ВЫ ПРОИГРАЛИ! Было слово: ' + word, fg='red')
        user_input.config(state='disabled')
        gameover = True
        startagain_button.pack(padx=10, pady=10)
        return

    if all(letter in user for letter in word):
        ans.config(text='Вы выиграли! Это слово - ' + word, fg='green')
        user_input.config(state='disabled')
        gameover = True
        startagain_button.pack(padx=10, pady=10)


# Кнопка OK
button1 = tk.Button(root, text='OK', font=('Arial', 15), command=input_all)
button1.pack(padx=10, pady=10)

# Нажатие Enter = OK
user_input.bind('<Return>', lambda event: input_all())


# Перезапуск игры
def reset_game():
    global attempt, user, gameover, word, buttons
    attempt = 10
    user = []
    gameover = False
    word = random.choice(possible_variant)
    ans.config(text='', fg='black')
    label3.config(text=str(attempt))
    guessed_label.config(text='Угаданные буквы: ')
    user_input.config(state='normal')
    user_input.delete(0, tk.END)

    # Удалить старые кнопки
    for btn in buttons:
        btn.destroy() # Удаляет кнопку с окна!
    buttons = [] # Уже очищает сам список

    # Создать новые кнопки
    for index, _ in enumerate(word):
        btn = tk.Button(buttonframe, text=' ', font=('Arial', 18), width=4)
        btn.grid(row=0, column=index, padx=2, pady=2)
        buttons.append(btn)

    # Спрятать кнопку "начать снова"
    startagain_button.pack_forget()

reset_game()

root.mainloop()
