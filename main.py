from tkinter import *
from tkinter import messagebox
import random

count = 0
def on_closing():
    messagebox.showerror("Bah ?", "Tu esquive la question ?")

def oui():
    messagebox.showinfo(' ', "Je le savais tu est GAYYY !\nTu peux m'appeler sur mon numéro <3\n04 42 37 93 00")
    quit()
def motionMouse (event):
    global count
    btnYes.place(x=random.randint(0,500), y=random.randint(0, 500))
    count += 1
    if count == 10:
        messagebox.showinfo("","Putain click sur Yes !")
    if count == 17:
        messagebox.showerror("","T'abuses")
    if count == 23:
        messagebox.showinfo("","Bon vazi t'es hétéro sale pd")
        win.quit()


win = Tk()
win.geometry('600x600')
win.title('Gay or Not ?')
win.resizable(width=False,height=False)
win['bg'] = 'white'

label = Label(win, text='Are you gay?', font='Arial 20 bold', bg='white')
label.pack()
btnYes = Button (win, text='No', font= 'Arial 20 bold')
btnYes.place (x=170, y=100)
btnYes.bind ('<Enter>', motionMouse)
btnNo = Button (win, text='Yes', font='Arial 20 bold', command=oui)
btnNo.place(x=350, y=100)

win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()



"""
                                              ╔═════════════╗
                                              ║ ▀███▀▀▀██▄  ║
                                              ║   ██   ▀██▄ ║
                                              ║   ██   ▄██  ║
                                              ║   ███████   ║
                                              ║   ██        ║
                                              ║   ██        ║
                                              ║ ▄████▄      ║
                                              ╚═════════════╝
"""