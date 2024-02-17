

import tkinter as tk

window = tk.Tk()
ROW = 5
COLUMNS = 3

buttons = []
for i in range(ROW):
    temp = []
    for j in range(COLUMNS):
        btn = tk.Button(window)
        temp.append(btn)
    buttons.append(temp)

for row_btn in buttons:
    print(row_btn)






window.mainloop()