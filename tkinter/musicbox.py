import threading
import tkinter as tk
import os
import asyncio
import time
from threading import Thread

from playsound import playsound

class Music_Button(tk.Button):
    def __init__(self, frame):
        self.selected = False
        super(Music_Button, self ).__init__(master=frame)
    
    async def play_sound(self):
        dirname = os.path.dirname(__file__)
        note = os.path.join(dirname, "../music/sounds/piano-a.wav")
        print('ding')
        await playsound(note)

    def is_switched(self):
        if self.selected:
            self.config(fg = "grey")
            self.selected = False
        else:
            self.config(fg = "green")
            self.selected = True


    def button_selection(self):
        self.is_switched()
       


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
            for num, letter in enumerate(list_char):
                note_button = Music_Button(column)
                note_button["text"] = letter+str(num+1)
                note_button["command"] = self.button_command
                note_button.config(bg="green")
                #self.note_button.grid(row=num, column=number)
                note_button.pack(side="top")
                button_list.append(note_button)
            self.column_list.append(button_list)


    
        
    def button_command(self):
        self.start_stuff() 

    def start_stuff(self):
        self.toggle_changes()
        self.change_buttons()

    def toggle_changes(self):
        if self.toggled:
            self.toggled = False
        else:
            self.toggled = True

    def change_buttons(self):
        while self.toggled:
            for button in self.column_list[self.current_column]:
                button.config(bg="black")
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