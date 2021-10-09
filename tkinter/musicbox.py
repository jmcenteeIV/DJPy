import threading
import tkinter as tk
import os
import asyncio
import time
from threading import Thread

from playsound import playsound

class Music_Button(tk.Button):
    selected = False
    button_id = ""

    def __init__(self, frame, app, button_id):
        self.selected = False
        self.app = app
        self.button_id = button_id
        super(Music_Button, self ).__init__(master=frame)
    
    async def play_sound(self):
        dirname = os.path.dirname(__file__)
        note = os.path.join(dirname, "../music/sounds/piano-a.wav")
        print('ding')
        await playsound(note)

    def is_toggled(self):
        return self.selected


    def button_toggle(self):
        if self.selected:
            self.config(fg = "black")
            self.selected = False
        else:
            self.config(fg = "grey")
            self.selected = True
       
    def print_button(self):
        print(f'button id is {self.button_id}')

    def start_stuff(self):
        self.button_toggle()
        self.app.toggle_changes()
        self.app.change_buttons()
        self.print_button()

class Application(tk.Frame):
    toggled = False
    current_column = 0
    column_list = []

    def __init__(self, master=None):
        super().__init__(master) 
        self.master = master
        self.pack()
        self.create_widgets()
        
        
    def create_widgets(self):
        list_num = [1, 2, 3, 4, 5, 6, 7, 8]
        list_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for number in list_num:
            column = tk.Frame(self.master)
            column.pack( side = "left")
            button_list = []
            for letter in list_char:
                note_button = Music_Button(column, self, letter+str(number))
                note_button["text"] = letter+str(number)
                note_button["command"] = note_button.start_stuff
                note_button.config(bg="green")
                #self.note_button.grid(row=num, column=number)
                note_button.pack(side="top")
                button_list.append(note_button)
            self.column_list.append(button_list)

    def print_hello(self):
        print("Hello I am App")
    
        
    def button_command(self, note_button):
        note_button.button_toggle()
        print(f'{note_button.button_id} clicked')
        self.start_stuff() 



    def toggle_changes(self):
        if self.toggled:
            no_buttons_toggled = True
            for column in self.column_list:
                for button in column:
                    if button.is_toggled():
                        no_buttons_toggled = False
            if no_buttons_toggled:
                self.toggled = False
        else:
            self.toggled = True

    def change_buttons(self):
        while self.toggled:
            for button in self.column_list[self.current_column]:
                button.config(bg="black")
                button.play_sound()
            self.update()
            time.sleep(.5)
            for button in self.column_list[self.current_column]:
                button.config(bg="green")
            
            if (self.current_column  < 7):
                self.current_column += 1
            else:
                self.current_column = 0
            self.update()
    
    
root = tk.Tk()
app = Application(master=root)
app.mainloop()