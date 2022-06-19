import tkinter as tk


# Creating function close program
def do_Close():
	window.destroy()

# Creating main window
window = tk.Tk()
window.geometry("450x450")
window.title("Examples of plotting")

# Adding a header label
lblTitle = tk.Label(text = 'ПРИМЕРЫ ПОСТРОЕНИЯ ГРАФИКОВ', font = ('Helvetica', 14, 'bold'), fg = '#0000cc')
lblTitle.place(x=45, y=25)

# Adding a comments label
lblChart1 = tk.Label(text = 'График синуса matplotlib')
lblChart1.place(x=160, y=88)

lblChart2 = tk.Label(text = 'Нормальное распределение')
lblChart2.place(x=160, y=148)

# Adding buttons
btnChart1 = tk.Button(window, text = 'График 1', font = ('Helvetica', 10, 'bold'))
btnChart1.place(x=45, y=85, width=90, height=30)

btnChart2 = tk.Button(window, text = 'График 2', font = ('Helvetica', 10, 'bold'))
btnChart2.place(x=45, y=145, width=90, height=30)

# Creating button close program
btnClose = tk.Button(window, text="Close", font = ('Helvetica', 10, 'bold'), command=do_Close)
btnClose.place(x=330, y=400, width=90, height=30)

# Starting the cycle
window.mainloop()
