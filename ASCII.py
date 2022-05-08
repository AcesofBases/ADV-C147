# -*- coding: utf-8 -*-
"""
Created on Sat May  7 14:49:21 2022

@author: Ace
"""

from tkinter import *

root = Tk()

root.title("ASCII")
root.geometry("400x400")
root.configure(background = 'snow')


enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text="Name in Ascii:  ",bg="light yellow",fg="black")
Encrypted_message = Label(root, text="Name In Ecryption: ")



def Ascii():
    input_word = enter_word.get()

    
    for letter in input_word:
        
        label["text"] += str(ord(letter)) + " "
        Encrypted_message["text"] += chr(ord(letter)-3)
      
        
    
    
    
btn = Button(root,text=" Display The Ascii code and encrypted value", command= Ascii,bg='gold',fg = 'black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)  
    
label.place(relx=0.5,rely=0.6,anchor=CENTER)
Encrypted_message.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()