from tkinter import *

def miles_to_km():
    mile=float(mile_input.get())
    km=round((mile*1.609344),2)
    km_result.config(text=f"{km}")

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=100)
window.config(padx=20,pady=20)
mile_input=Entry(width=10)
mile_input.grid(column=3,row=0)
mile_label=Label(text="Miles")
mile_label.grid(column=4,row=0)
is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=2,row=1)
km_result=Label(text="0")
km_result.grid(column=3,row=1)
km_label=Label(text="Km")
km_label.grid(column=4,row=1)
calculate_button=Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=3,row=2)
window.mainloop()