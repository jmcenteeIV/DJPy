import tkinter as tk

from playsound import playsound

class Music_Button(tk.Button):
    def __init__(self):
        self.selected = False
        super(Music_Button, self).__init__()
    
    def play_sound(self):
        note = "../music/sounds/piano-a.wav"
        playsound(note)
        print('ding')

    def is_switched(self):
        if self.selected:
            self.config(fg = "grey")
            self.selected = False
        else:
            self.config(fg = "green")
            self.selected = True


    def button_selection(self):
        self.is_switched()
        self.play_sound()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack()
        self.create_widgets()
    
    
        
    def create_widgets(self):
        list_num = [1, 2, 3, 4, 5, 6, 7, 8]
        list_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for number in list_num:
            for num, letter in enumerate(list_char):
                self.note_button = Music_Button()
                self.note_button["text"] = letter+str(num+1)
                self.note_button["command"] = self.note_button.play_sound
                self.note_button.grid(row=num, column=number)
                #self.note_button.pack(side="bottom")


    

root = tk.Tk()
app = Application(master=root)
app.mainloop()