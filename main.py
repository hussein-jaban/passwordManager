from tkinter import *
from tkinter import messagebox
from random import choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, 'end')
    pick = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', '0', '1', '2', '3', '4', '5', 'L', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', '6', '7', '8', '!', '#', '$', '%', '&', '(', '*', '+']
    password_len = int(spinbox.get())

    password_list = [choice(pick) for _ in range(password_len)]
    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)