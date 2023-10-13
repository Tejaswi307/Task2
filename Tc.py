import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
root=tk.Tk()
root.title("Temperature Converter")
root.geometry('300x90')
root.resizable(False,False)
def fahrenhit_to_celsius(f):
    return(f - 32)*5/9
frame=ttk.Frame(root)
options={'padx':5,'pady':5}
temperature_label=ttk.Label(frame,text='Fahrenheit')
temperature_label.grid(column=0,row=0,sticky='W',**options)
temperature=tk.StringVar()
temperature_entry=ttk.Entry(frame,textvariable=temperature)
temperature_entry.grid(column=1,row=0,**options)
temperature_entry.focus()
def convert_button_clicked():
    try:
        f=float(temperature.get())
        c=fahrenhit_to_celsius(f)
        result=f'{f}Fahrenhit={c:.2f}Celsisus'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error',message=error)
convert_button=ttk.Button(frame,text='Convert')
convert_button.grid(column=2,row=0,sticky='W',**options)
convert_button.configure(command=convert_button_clicked)
result_label=ttk.Label(frame)
result_label.grid(row=1,columnspan=3,**options)
frame.grid(padx=10,pady=10)
root.mainloop()
