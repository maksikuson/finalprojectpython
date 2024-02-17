
import tkinter as tk
from random import shuffle




class MyButton(tk.Button):
    
    def __init__(self, master, x, y, number, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
      
    def __repr__(self):
        return f'MyButton{self.x} {self.y} {self.number} {self.is_mine}'


class MineSweeper:
    
    window = tk.Tk()
    ROW = 5
    COLUMNS = 3
    MINES = 7
    
    def __init__(self):
        self.buttons = []
        count = 1
        for i in range(MineSweeper.ROW):
            temp = []
            for j in range(MineSweeper.COLUMNS):
                btn = MyButton(MineSweeper.window, x=i, y=j, number=count)
                temp.append(btn)
                count += 1
            self.buttons.append(temp)
    
    def create_widgets(self):
        for i in range(MineSweeper.ROW):
            for j in range(MineSweeper.COLUMNS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)    
    
    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.print_buttons()
        
        MineSweeper.window.mainloop()
    
                    
    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)
    
    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        for row_btn in self.buttons:
            for bth in row_btn:
                if bth.number in index_mines:
                    bth.is_mine = True
                    
    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.COLUMNS * MineSweeper.ROW + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]
        
game = MineSweeper() 
game.start()

