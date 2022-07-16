from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Password Guesser")


label_guess = Label(root)
label_guess.place(relx = 0.5, rely = 0.3, anchor = CENTER)
label = Label(root)
label.place(relx = 0.5, rely = 0.7, anchor=CENTER)

guess_input = Entry(root)
guess_input.place(relx = 0.5, rely = 0.2, anchor = CENTER)


array1 = [[[1,2,3,4,5,6,7,8,9,0], ["Heads", "Tails", "True", "False"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],["!", "@", "#", "$", "%", "^", "&", "*"]]]


def guess():
    
    guess = guess_input.get()
    label_guess["text"] = guess
    

def solution():
    random1 = random.randint(0,9)
    random2 = random.randint(0,3)
    random3 = random.randint(0,10)
    random4 = random.randint(0,7)
    
    letter1 = str(array1[0][0][random1])
    letter2 = array1[0][1][random2]
    letter3 = array1[0][2][random3]
    letter4 = array1[0][3][random4]
    
    
    label["text"] = letter1 + letter2 + letter3 + letter4

button_guess = Button(root, command = guess, text="Set Guess")
button_guess.place(relx = 0.5, rely = 0.4, anchor = CENTER)
button_solution = Button(root, command = solution, text="Get Password")
button_solution.place(relx = 0.5, rely = 0.6, anchor = CENTER)
root.mainloop();    