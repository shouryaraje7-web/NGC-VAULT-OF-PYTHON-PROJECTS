# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def maximize_window(win):
	try:
		win.state('zoomed')
	except tk.TclError:
		try:
			win.attributes('-zoomed', True)
		except tk.TclError:
			win.update_idletasks()
			win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenheight()}+0+0")


# Add your event handler script here 

expression = ""  # store the current expression globally

def click_handler(event):
    global expression
    button = event.widget
    value = button.cget("text")

    if value == "C":
        expression = ""
        label.config(text="0")
    elif value == "=":
        try:
            safe_expression = expression.replace("x", "*")
            result = str(eval(safe_expression))
            label.config(text=result)
            expression = result  # allow chaining
        except Exception:
            label.config(text="Error")
            expression = ""
    else:
        expression += value
        label.config(text=expression)


main = tk.Tk()
main.title("Main Window")
main.config(bg="#E4E2E2")
main.geometry("359x744")
main.update_idletasks()

geometryX = 0
geometryY = 0

main.geometry("+%d+%d"%(geometryX, geometryY))
maximize_window(main)


style = ttk.Style(main)
style.theme_use("clam")

menu = tk.Menu(main)
main.config(menu=menu)
menu_0 = tk.Menu(menu, tearoff=0)
menu_0.add_command(label="New", command=lambda: print("New clicked"))
menu_0.add_command(label="Open", command=lambda: print("Open clicked"))
menu.add_cascade(label="File", menu=menu_0)
menu_1 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=menu_1)

style.configure("label.TLabel", background="#E4E2E2", foreground="#000000", borderwidth=1, font=("", 13, "bold"), anchor="center")
label = ttk.Label(master=main, text="PYBank", style="label.TLabel")
label.configure(anchor="center")
label.place(x=0, y=4, height=70)

style.configure("label1.TLabel", background="#ffffff", foreground="#66e96b", font=("", 13, "bold"), anchor="center")
label1 = ttk.Label(master=main, text="$", style="label1.TLabel")
label1.configure(anchor="center")
label1.place(x=9, y=91, width=338, height=63)

style.configure("label2.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
label2 = ttk.Label(master=main, text="Created by Aryan, An intermediate python developer", style="label2.TLabel")
label2.configure(anchor="center")
label2.place(x=15, y=396, width=335, height=48)

style.configure("button.TButton", background="#66e96b", foreground="#000", font=("", 13, "bold"))
style.map("button.TButton", background=[("active", "#ffffff")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="Execute", style="button.TButton")
button.place(x=74, y=345, width=210, height=40)

style.configure("selection_menu.TCombobox", fieldbackground="#ffffff", foreground="#000")
selection_menu_options = ["Deposit","Withdraw","Loan","History"]
selection_menu_var = tk.StringVar(value="Select option")
selection_menu = ttk.Combobox(main, textvariable=selection_menu_var, values=selection_menu_options, style="selection_menu.TCombobox")
selection_menu.place(x=1, y=272, width=354, height=58)

style.configure("entry.TEntry", fieldbackground="#fff", foreground="#000", font=("", 13, "bold"))

entry = ttk.Entry(master=main, style="entry.TEntry")
entry.place(x=29, y=185, width=299, height=38)


main.mainloop()