import sys, os
import tkinter as tk
from tkinter import ttk

def runTrace():
    destIP = addressEntry.get()
    nHops = hopsEntry.get()

    if os.name == "nt":
        os.system(f"python tracesockets.py {destIP} {nHops}") # For Windows
    elif os.name == "posix":
        os.system(f"sudo python3 tracesockets.py {destIP} {nHops}") # For Linux/Mac
    else:
        print("Unknown system")
        sys.exit()

def close_application():
    root.destroy()

root = tk.Tk()
root.title("Setting up...")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(mainframe, text="Address:").grid(row=0, column=0, sticky=tk.W, columnspan=1)
addressEntry = tk.Entry(mainframe)
addressEntry.grid(row=1, column=0, sticky=(tk.W, tk.E), columnspan=1)

ttk.Label(mainframe, text="Hops:").grid(row=0, column=1, sticky=tk.W, columnspan=1)
hopsEntry = tk.Entry(mainframe)
hopsEntry.grid(row=1, column=1, sticky=(tk.W, tk.E), columnspan=1)

ttk.Button(mainframe, text="Trace", command=runTrace).grid(row=2, column=0, columnspan=1)
ttk.Button(mainframe, text="Close", command=close_application).grid(row=2, column=1, columnspan=3)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=3, pady=3)

root.mainloop()