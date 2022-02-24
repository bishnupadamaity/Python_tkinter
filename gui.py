

# starter code
import tkinter as tk
from tkinter import NW, ttk
win = tk.Tk()
win.title('GUI')

# label

name_label = ttk.Label(win,text='Enter your name: ')
name_label.grid(row=0,column=0,sticky=tk.NW)

email_label = ttk.Label(win,text='Enter your email: ')
email_label.grid(row=1,column=0,sticky=tk.NW)

age_label = ttk.Label(win,text='Enter your age: ')
age_label.grid(row=2,column=0,sticky=tk.NW)

gender_label = ttk.Label(win,text = "Gender:")
gender_label.grid(row=3,column=0,sticky=NW)

# Entry box

name_var = tk.StringVar()
name_entrybox = ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)


# combo box

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win,width=14,textvariable=gender_var,state='readonly')
gender_combobox['values'] = ('----  select  ----','Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)


# Radio button

usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win,text='Student', value='Student',variable=usertype)
radiobtn1.grid(row=4,column =0)

radiobtn2 = ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobtn2.grid(row=4,column=1)



# button 

def action():
    user_name = name_var.get()
    user_email = email_var.get()
    user_age = age_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()

    print(f"{user_name}, your age is {user_age} and gender is {user_gender},email is {user_email} usertype is {user_type}")


submit_button=ttk.Button(win,text='Submit',command=action)
submit_button.grid(row=5,columnspan=2)















win.mainloop()