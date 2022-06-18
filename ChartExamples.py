import tkinter as tk

# Creating function close program
def do_Close():
	window.destroy()

# Creating main window
window = tk.Tk()
window.geometry("450x450")
window.title("Examples of plotting")

# Creating button close program
btnClose = tk.Button(window, text="Close", font = ('Helvetica', 10, 'bold'), command=do_Close)
btnClose.place(x=330, y=400, width=90, height=30)

# Starting the cycle
window.mainloop()
