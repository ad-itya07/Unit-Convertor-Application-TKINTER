from tkinter import *

window = Tk()
window.title("Kilometers to Meters")
window.minsize(width=300,height=100)
window.config(padx=30,pady=30)

def convert():
    label_3.config(text=f"{float(km_inp.get())*1000}")


km_inp = Entry(width=15)
km_inp.grid(column=1,row=0)

# Labels:

label_1 = Label(text="Kilometers")
label_1.grid(column=2,row=0)

label_2 = Label(text="is equal to ")
label_2.grid(column=0,row=1)

label_3 = Label(text="0")
label_3.grid(column=1,row=1)

label_4 = Label(text="Meters")
label_4.grid(column=2,row=1)

# Button:

convertor = Button(text="Convert",command=convert)
convertor.grid(column=1,row=2)




window.mainloop()