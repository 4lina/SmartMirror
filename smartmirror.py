from tkinter import *
import tkinter.font
import time
from time import strftime

class GUI(Frame):

    
    def __init__(self, master):
        Frame.__init__(self, master)

        self.largeFont = tkinter.font.Font(family="Piboto", size=70)
        self.mediumFont = tkinter.font.Font(family="Piboto", size=40)
        self.normalFont = tkinter.font.Font(family="Piboto Light", size=20)
 

    def setupGUI(self):
        self.grid(row=0, column=0)

        
        # Time frame to hold time & date in grid
        time_frame = Frame(self, width=400, height=500, bg='black')
        time_frame.grid(row=0, column=2, sticky=NE)
        GUI.time_label = Label(time_frame, text=strftime("%H:%M", time.localtime()), fg='white', bg='black',
                               font=self.largeFont)
        GUI.time_label.grid(row=0, column=0, sticky=NE)

        GUI.date_label = Label(time_frame, text=strftime("%A, %B %d", time.localtime()), fg='white', bg='black',
                               font=self.normalFont)
        GUI.date_label.grid(row=1, column=0, sticky=NE)


    def updateGUI(self):
        # Constantly updates the time until the program is stopped
        GUI.time_label.configure(text=strftime("%H:%M", time.localtime()))
        GUI.date_label.configure(text=strftime("%A, %B %d", time.localtime()))
        self.after(1000, self.updateGUI)

    def close_escape(event=None):
        print("Smart mirror closed")
        window.destroy()



window = Tk()
window.title("Smart Mirror")
window.geometry('1920x1080')
window.configure(background='black')

#Removes borders from GUI and implements quit via esc
window.overrideredirect(1)
window.overrideredirect(0)
window.attributes("-fullscreen", True)
window.wm_attributes("-topmost", 1)
window.focus_set()

window.bind("<Escape>", GUI.close_escape)

mirror = GUI(window)
mirror.setupGUI()
window.after(1000, mirror.updateGUI)
window.mainloop()
