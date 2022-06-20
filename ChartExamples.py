import tkinter as tk
import chart1
import chart2
import chart3

# Creating function close program
def do_Close():
	window.destroy()

# Creating main window
window = tk.Tk()
window.geometry("450x550")
window.title("Examples of plotting")

# Adding a header label
lblTitle = tk.Label(text = 'ПРИМЕРЫ ПОСТРОЕНИЯ ГРАФИКОВ', font = ('Helvetica', 14, 'bold'), fg = '#0000cc')
lblTitle.place(x=45, y=25)

# Adding label & button for graph1
lblChart1 = tk.Label(text = 'График синуса matplotlib')
lblChart1.place(x=160, y=88)

btnChart1 = tk.Button(window, text = 'График 1', font = ('Helvetica', 10, 'bold'), command=chart1.plot_chart)
btnChart1.place(x=45, y=85, width=90, height=30)

# Adding label & button for graph2
lblChart2 = tk.Label(text = 'Нормальное распределение')
lblChart2.place(x=160, y=148)

btnChart2 = tk.Button(window, text = 'График 2', font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart2.place(x=45, y=145, width=90, height=30)

# Adding label & button for graph3
lblChart3 = tk.Label(text = 'Нормальное распределение - 3 графика')
lblChart3.place(x=160, y=208)

btnChart3 = tk.Button(window, text = 'График 3', font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart3.place(x=45, y=205, width=90, height=30)

# Adding label & button for graph4
lblChart4 = tk.Label(text = 'Гистограмма Seaborn')
lblChart4.place(x=160, y=268)

btnChart4 = tk.Button(window, text = 'График 4', font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart)
btnChart4.place(x=45, y=265, width=90, height=30)

# Adding label & button for graph5
lblChart5 = tk.Label(text = 'Двойная гистограмма Seaborn')
lblChart5.place(x=160, y=328)

btnChart5 = tk.Button(window, text = 'График 5', font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart2)
btnChart5.place(x=45, y=325, width=90, height=30)

# Adding label & button for graph6
lblChart6 = tk.Label(text = 'Нормальное распределение')
lblChart6.place(x=160, y=388)

btnChart6 = tk.Button(window, text = 'График 6', font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart6.place(x=45, y=385, width=90, height=30)

# Adding label & button for graph7
lblChart7 = tk.Label(text = 'Нормальное распределение')
lblChart7.place(x=160, y=448)

btnChart7 = tk.Button(window, text = 'График 7', font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart7.place(x=45, y=445, width=90, height=30)


# Creating button close program
btnClose = tk.Button(window, text="Close", font = ('Helvetica', 10, 'bold'), command=do_Close)
btnClose.place(x=330, y=500, width=90, height=30)

# Starting the cycle
window.mainloop()
