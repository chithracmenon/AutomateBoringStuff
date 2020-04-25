import tkinter as tk
import time

class SudokuGUI():
	MARGIN = 10
	SQUARE = 50
	HEIGHT = WIDTH = MARGIN + SQUARE * 9
	
	def __init__(self, board):
		self.board = board
		self.__initUI()
		

	def __initUI(self):
		self.window = tk.Tk()
		self.window.title("Sudoku")
		self.defaultbg = self.window.cget('bg')
		self.canvas = tk.Canvas(master = self.window, width = self.WIDTH, height = self.HEIGHT)
		self.canvas.pack( fill = tk.BOTH, side = tk.TOP)
		self.button = tk.Button(master = self.window, text = 'Solve', command = self.solve)
		self.button.pack( fill = tk.BOTH, side = tk.BOTTOM)
		
		
		self.__initialgrid()
		self.__initialfill(self.board)
		self.window.mainloop()
		
	def __initialgrid(self):
		for i in range(10):
			color = 'black' if (i % 3 == 0) else 'blue'
			
			x0 = self.MARGIN + i * self.SQUARE
			y0 = self.MARGIN
			x1 = self.MARGIN + i * self.SQUARE 
			y1 = self.HEIGHT - self.MARGIN
			self.canvas.create_line(x0, y0, x1, y1, fill = color)
			
			x0 = self.MARGIN
			y0 = self.MARGIN + i * self.SQUARE
			x1 = self.WIDTH - self.MARGIN
			y1 = self.MARGIN + i * self.SQUARE
			self.canvas.create_line(x0, y0, x1, y1, fill = color)
			
	def __initialfill(self, board):
		for i in range(9):
			for j in range(9):
				value = board[i][j]
				if value != 0:
					x = self.MARGIN + self.SQUARE / 2 + j * self.SQUARE 
					y = self.MARGIN + self.SQUARE / 2 + i * self.SQUARE
					self.canvas.create_text(x, y, text = value, fill = 'black')
		
	def solvegrid(self, i, j, value):
		x = self.MARGIN + self.SQUARE / 2 + self.SQUARE * j
		y = self.MARGIN + self.SQUARE / 2 + self.SQUARE * i 
		self.canvas.create_oval(x-10, y-10, x+10, y+10, fill = self.defaultbg, outline = self.defaultbg)
		self.canvas.create_text(x, y, text = value, fill = 'sea green', font = 'Helvetica 18 bold')
		self.window.update()
		
		
	def valid(self, board, i , j, k):
		if k in board[i]:
			return False
		for c in range(len(board)):
			if board[c][j] == k:
				return False
		box_hp = i // 3
		box_wp = j // 3
		
		for a in range(0,3):
			for b in range(0,3):
				if board[box_hp * 3 + a][box_wp * 3 + b] == k:
					return False
		return True

	def find_null(self, board):
		for i in range(len(board)):
			for j in range(len(board)):
				if board[i][j] == 0:
					return (i,j)
		
	def solve(self):
		
		find = self.find_null(board)
		
		if find is None:
			return True
		else:
			i, j = find
			for k in range(1,10):
				if self.valid(board, i, j, k):
					board[i][j] = k
					self.solvegrid(i, j, k)
					time.sleep(0.1)
					if self.solve():
						return True
					
					board[i][j] = 0
		
	   
		return False				
					
if __name__ == '__main__':

	board = [[7,8,0,4,0,0,1,2,0],
		[6,0,0,0,7,5,0,0,9],
		[0,0,0,6,0,1,0,7,8],
		[0,0,7,0,4,0,2,6,0],
		[0,0,1,0,5,0,9,3,0],
		[9,0,4,0,6,0,0,0,5],
		[0,7,0,3,0,0,0,1,2],
		[1,2,0,0,0,7,4,0,0],
		[0,4,9,2,0,6,0,0,7]]
		
	SudokuGUI(board)
			
		