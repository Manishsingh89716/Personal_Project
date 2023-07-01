#Registration Form using Tkinter module

from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Registration Form")


label_0 = Label(root, text="Registration Form", width=20,
                font=("bold",20))
label_0.place(x=90, y=60)

label_1 = Label(root, text="FullName(In Capital Letter)", width=20,
                font=("bold",10))
label_1.place(x=80, y=130)
entry_1 = Entry(root)
entry_1.place(x=240, y=130)


label_2 = Label(root, text="Email/PhoneNumber", width=20,
                font=("bold",10))
label_2.place(x=68, y=180)
entry_2 = Entry(root)
entry_2.place(x=240, y=180)


label_3 = Label(root, text="Gender", width=20,
                font=("bold",10))
label_3.place(x=70, y=230)


var = IntVar()

Radiobutton(root, text="Male", padx=5, variable=var,
            value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20, variable=var,
            value=2).place(x=290, y=230)

label_4 = Label(root, text="Country", width=20,
                font=("bold",10))
label_4.place(x=70, y=280)


country = ['India', 'US', 'Germany', 'Australia', 'France']
c = StringVar()
droplist = OptionMenu(root, c, *country)
droplist.config(width=15)
c.set('Select Your Country')
droplist.place(x=240, y=280)


label_5 = Label(root, text="Language", width=20,
                font=("bold",10))
label_5.place(x=75, y=330)

var1 = IntVar()
Checkbutton(root, text="English", variable=var1).place(x=230, y=330)
var2 = IntVar()
Checkbutton(root, text="German", variable=var2).place(x=290, y=330)
var3 = IntVar()
Checkbutton(root, text="French", variable=var3).place(x=355, y=330)


Button(root, text='Submit', width=20, bg="black",
       fg='white').place(x=180, y=380)
root.mainloop()

