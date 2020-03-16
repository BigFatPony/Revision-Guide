import os.path
import time
import tkinter as tk
from tkinter import *

def createFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
createFolder("Flashcards")

def createFolderQ(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
createFolder("Quizzes")

def createFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
createFolder("Usernames")
    
def settings():
    print("Feature in development")

def quizzes():
    print("Feature in development")

def saved():
    saved = tk.Label(screen7,bg="#a6a6a6", text = "Flashcard saved", fg = "green", font = ("Century Gothic", 11))
    saved.pack()
    screen7.after(1500, saved.destroy)

def save():
    directory = 'Flashcards'
    flashcard = raw_flashcards.get()
    filename = raw_filename.get()
    file_patha = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    fdata = open(file_patha, "w")
    fdata.write(flashcard)
    fdata.close()
    saved()

def create_flashcard():
    global raw_filename
    global raw_flashcards
    global screen7
    raw_filename = StringVar()
    raw_flashcards = StringVar()

    screen7 = Toplevel(screen)
    screen7.title("Info")
    screen7.geometry("300x250")
    screen7.configure(bg="#a6a6a6")
    
    Label(screen7,bg="#a6a6a6", text = "Please enter a flashcard for the note below:").pack()
    Entry(screen7, textvariable = raw_filename).pack()
    Label(screen7,bg="#a6a6a6", text = "Please enter the flashcard for the file below:").pack()
    Entry(screen7, textvariable = raw_flashcards).pack()
    Button(screen7,bg="grey", text = "Save", width = 10, height = 1, command = save).pack()
    Button(screen7,bg="grey", text = "Back", width = 10, height = 1, command=lambda: screen7.destroy()).pack()    


def view_flashcards1():
    screen9 = Toplevel(screen)
    screen9.title("Flashcards")
    screen9.geometry("600x600")
    screen9.configure(bg="#a6a6a6")
    
    filename1 = raw_filename1.get()
    
    list_flash = os.listdir("Flashcards")
    if filename1 in list_flash:
        flashcardj =open("Flashcards/"+filename1,"r")
    else:
        print("Not found")
        
    Label(screen9,bg="#a6a6a6", text = "").pack()
    Label(screen9,bg="#a6a6a6", text = "").pack()        
    Label(screen9,bg="#a6a6a6", text = flashcardj.read()).pack()
    Button(screen9,bg="grey", text = "Back", width = 10, height = 1, command=lambda: screen9.destroy()).pack()

def view_flashcards():
    global raw_filename1
    raw_filename1 = StringVar()
    
    screen8 = Toplevel(screen)
    screen8.title("Flashcards")
    screen8.geometry("600x600")
    screen8.configure(bg="#a6a6a6")

    all_files = os.listdir("Flashcards")
    
    Label(screen8,bg="#a6a6a6", text = "Please use one of the file names below").pack()
    Label(screen8,bg="#a6a6a6", width = 100, height = 5, text = all_files).pack()
    Entry(screen8, textvariable=raw_filename1).pack()
    Button(screen8,bg="grey", text = "Okay", width = 10, height = 1, command = view_flashcards1).pack()
    Button(screen8,bg="grey", text = "Back", width = 10, height = 1, command=lambda: screen8.destroy()).pack()

def delete_flashcards1():
    filename3 = raw_filename2.get()

    filec = filename3
    location = ("Flashcards")
    pathc = os.path.join(location, filec)
    os.remove(pathc)
    
    del_flashcards1 = tk.Label(screen10,bg="#a6a6a6", text = "File removed", fg = "green", font = ("Century Gothic", 11))
    del_flashcards1.pack()
    screen10.after(1500, del_flashcards1.destroy)

def delete_flashcards():
    global screen10
    global raw_filename2
    screen10 = Toplevel(screen)
    screen10.title("Delete flashcard(s)")
    screen10.geometry("500x500")
    screen10.configure(bg="#a6a6a6")
    
    all_files = os.listdir("Flashcards")
    
    Label(screen10,bg="#a6a6a6", text = "Please enter the name of the file you wish to delete").pack()
    Label(screen10,bg="#a6a6a6", text = all_files).pack()
    raw_filename2 = StringVar()
    Entry(screen10, textvariable=raw_filename2).pack()
    Button(screen10,bg="grey", text = "Okay", width = 10, height = 1, command = delete_flashcards1).pack()
    Button(screen10,bg="grey", text = "Back", width = 10, height = 1,  command=lambda: screen10.destroy()).pack()

def flash_card():
    screen9 = Toplevel(screen)
    screen9.title("Flash cards")
    screen9.geometry("700x700")
    screen9.configure(bg="#a6a6a6")

    Label(screen9,bg="#666666",width="2000",height="4", text = "Flashcards", font = ("Century Gothic", 15)).pack()
    Label(screen9,bg="#a6a6a6", text = "").pack()
    Button(screen9,bg="grey", text = "Create Flashcards", width = 25, height = 4, command = create_flashcard).pack()
    Label(screen9,bg="#a6a6a6", text = "").pack()
    Button(screen9,bg="grey", text = "View Flashcards", width = 25, height = 4, command = view_flashcards).pack()
    Label(screen9,bg="#a6a6a6", text = "").pack()
    Button(screen9,bg="grey", text = "Delete Flashcards", width = 25, height = 4, command = delete_flashcards).pack()
    Label(screen9,bg="#a6a6a6", text = "").pack()
    Button(screen9,bg="grey", text = "Back", width = 25, height = 4,  command=lambda: screen9.destroy()).pack()

def dashboard():
    screen6 = Toplevel(screen)
    screen6.title("Dashboard")
    screen6.geometry("700x700")
    screen6.configure(bg="#a6a6a6")
    
    Label(screen6,bg="#666666",width="2000",height="4", text = "Welcome to the dashboard", font = ("Century Gothic", 15)).pack()
    Label(screen6,bg="#a6a6a6", text = "").pack()
    Button(screen6,bg="grey", text = "Flashcards", command = flash_card, width = 25, height = 4).pack()
    Label(screen6,bg="#a6a6a6", text = "").pack()
    Button(screen6,bg="grey", text = "Quizzes", command = quizzes, width = 25, height = 4).pack()
    Label(screen6,bg="#a6a6a6", text = "").pack()
    Button(screen6,bg="grey", text = "Settings", command = settings, width = 25, height = 4).pack()    
    Label(screen6,bg="#a6a6a6", text = "").pack()
    Button(screen6,bg="grey", text = "Quit", command = exit, width = 25, height = 4).pack()

def login_success():
    dashboard()

def incorrect_password():
    incorrect = tk.Label(screen2,bg="#a6a6a6", text = "Incorrect password!", fg = "red", font = ("Century Gothic", 11))
    incorrect.pack()
    screen2.after(1500, incorrect.destroy)

def user_not_found():
    unf = tk.Label(screen2,bg="#a6a6a6", text = "User not found!", fg = "red", font = ("Century Gothic", 11))
    unf.pack()
    screen2.after(1500, unf.destroy)

    
def register_user():
    username_info = username.get()
    password_info = password.get()

    directory = 'Usernames'
    filename = username_info
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    file = open(file_path, "w")
    file.write(password_info)
    file.close()

    register_success = tk.Label(screen1,bg="#a6a6a6", text = "Registration Successful", fg = "green", font = ("Century Gothic", 11))
    register_success.pack()
    screen1.after(1500, register_success.destroy)


def register():
    global screen1
    global username
    global password
    global username_entry
    global password_entry
    
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x300")
    screen1.configure(bg="#a6a6a6")

    username = StringVar()
    password = StringVar()

    Label(screen1,bg="#a6a6a6", text = "Please enter details below",font =13).pack()
    Label(screen1,bg="#a6a6a6", text = "").pack()
    Label(screen1,bg="#a6a6a6", text = "Username").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    
    Label(screen1,bg="#a6a6a6",  text = "Password").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    
    Label(screen1,bg="#a6a6a6", text = "").pack()
    Button(screen1,bg="grey", text = "Register", width = 10, height = 1, command = register_user).pack()
    Button(screen1,bg="grey", text = "Back", width = 10, height = 1,  command=lambda: screen1.destroy()).pack()


def login_verify():
    global username_verify
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()

    
    list_of_files = os.listdir("Usernames")
    if username1 in list_of_files:
        file1 = open("Usernames/"+username1, "r")
        verify = file1.read().splitlines()
    
        if password1 in verify:
            login_success()
        else:
            incorrect_password()       
    else:
        user_not_found()
    
def login():
    global screen2
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x300")
    screen2.configure(bg="#a6a6a6")
    Label(screen2,bg="#a6a6a6", text = "Please enter details below to log in",font =13).pack()
    Label(screen2,bg="#a6a6a6", text = "").pack()

    username_verify = StringVar()
    password_verify = StringVar()
    
    Label(screen2,bg="#a6a6a6", text = "Username").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2,bg="#a6a6a6", text = "Password").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify,show="*")
    password_entry1.pack()
    Label(screen2,bg="#a6a6a6", text = "").pack()
    Button(screen2,bg="grey", text = "Login", width = 10, height = 1, command = login_verify).pack()
    Button(screen2,bg="grey", text = "Back", width = 10, height = 1, command=lambda: screen2.destroy()).pack()    

def main_screen():
    global screen
    screen = Tk()
    screen.title("Login")
    screen.geometry("500x500")
    screen.configure(bg="#a6a6a6")
    photo = PhotoImage(file="logo.png")
    Label(screen,bg="#666666",width="2000",height="90", image=photo).pack()     
    
    Label(bg="#a6a6a6",text = "").pack()
    Button(text = "Login",bg="grey", height = "3", width = "30",font = ("Century Gothic", 13), command = login).pack()
    Label(bg="#a6a6a6",text="").pack()
    Button(text= "Register",bg="grey", height = "3", width = "30",font = ("Century Gothic", 13), command = register).pack()
    Label(bg="#a6a6a6",text="").pack()
    Button(text= "Exit",bg="grey", height = "3", width = "30",font = ("Century Gothic", 13), command = exit).pack()

    screen.mainloop()

main_screen()
