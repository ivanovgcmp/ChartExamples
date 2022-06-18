import tkinter as tk

# Creating main window
window = tk.Tk()
window.geometry("450x450")
window.title("Examples of plotting")

# Creating button close program
btnClose = tk.Button(window, text="Close", font = ('Helvetica', 10, 'bold'))
btnClose.place(x=330, y=400, width=90, height=30)

# Starting the cycle
window.mainloop()
