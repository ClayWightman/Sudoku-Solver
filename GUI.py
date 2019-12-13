from tkinter import *


class SudokuGUI:
	def __init__(self,master):
		self.master = master
		master.title('SudokuSolver')
		self.frame_dict = {}
		self.entry_dict = {}


	def fill(self):
		#Creates and packs frames sequentially
		frame_column = 0
		frame_row = 0
		for i in range(9):
			frame_key = 'frame' + str(i)
			self.frame_dict[frame_key] = Frame(self.master, width = 2, highlightbackground = 'black', highlightthickness = 1)
			self.frame_dict[frame_key].grid(column = frame_column, row = frame_row)
			if frame_column == 2:
				frame_column = 0
				if frame_row == 2:
					frame_row = 0
				else:
					frame_row += 1
			else:
				frame_column += 1
		#Creates and packs all of the entry elements in their respective frames
		entry_row = 0
		entry_column = 0
		for i in range(81):
			entry_key = 'entry' + str(i)
			if i < 9:
				entry_parent = self.frame_dict['frame0']
			elif i < 18:
				entry_parent = self.frame_dict['frame1']
			elif i < 27:
				entry_parent = self.frame_dict['frame2']
			elif i < 36:
				entry_parent = self.frame_dict['frame3']
			elif i < 45:
				entry_parent = self.frame_dict['frame4']
			elif i < 54:
				entry_parent = self.frame_dict['frame5']
			elif i < 63:
				entry_parent = self.frame_dict['frame6']
			elif i < 72:
				entry_parent = self.frame_dict['frame7']
			elif i < 81:
				entry_parent = self.frame_dict['frame8']
			self.entry_dict[entry_key] = Entry(entry_parent, width = 2, cursor = 'hand2')
			self.entry_dict[entry_key].grid(column = entry_column, row = entry_row)
			if entry_column == 2:
				entry_column = 0
				if entry_row == 2:
					entry_row = 0
				else:
					entry_row += 1
			else:
				entry_column += 1
		submit_button = Button(self.master, text = 'submit', command = self.submit)
		submit_button.grid(column = 1, row = 3)

	#todo - Submit button should call the solver class that way you dont have to close the GUI to get the results
	def submit(self):
		valid_entries = ['1','2','3','4','5','6','7','8','9','']
		input = []
		for i in range(81):
			value = self.entry_dict['entry' + str(i)].get()
			if(not value in valid_entries):
				print('ERROR: A value you added was outside of the range (1-9) \nPlease fix and resubmit')
				break
			if(value == ''):
				input.append(0)
			else:
				input.append(value)
		text_file = open('Sudoku-File.txt', 'w')
		for i in input:
			text_file.write(str(i))
		text_file.close()



class solver:
	def __init__(self):
		self.rows = [[0,1,2,9,10,11,18,19,20]
					,[3,4,5,12,13,14,21,22,23]
					,[6,7,8,15,16,17,24,25,26]
					,[27,28,29,36,37,38,45,46,47]
					,[30,31,32,39,40,41,48,49,50]
					,[33,34,35,42,43,44,51,52,53]
					,[54,55,56,63,64,65,72,73,74]
					,[57,58,59,66,67,68,75,76,77]
					,[60,61,62,69,70,71,78,79,80]]
		self.columns = [[0,3,6,27,30,33,54,57,60]
						,[1,4,7,28,31,34,55,58,61]
						,[2,5,8,29,32,35,56,59,62]
						,[9,12,15,36,39,42,63,66,69]
						,[10,13,16,37,40,43,64,67,70]
						,[11,14,17,38,41,44,65,68,71]
						,[18,21,24,45,48,51,72,75,78]
						,[19,22,25,46,49,52,73,76,79]
						,[20,23,26,47,50,53,74,77,80]]
		text_file = open('Sudoku-File.txt','r')
		self.input = list(text_file.readline(81))
		text_file.close()

	#Double check this method to make sure it works correctly
	def position_checker(self, position, value):
		box_position = int(position / 9) * 9
		for i in range(9):
			if value == int(self.input[box_position + i]):
				return False
		for row in self.rows:
			if position in row:
				for square in row:
					if value == int(self.input[int(square)]):
						return False
		for column in self.columns:
			if position in column:
				for square in column:
					if value == int(self.input[int(square)]):
						return False
		return True

		#Maybe bring find next zero part to bottom and make a find FIRST zero function?
	def recursion(self, position):
		self.testprint()
		#return case
		if position == 81:
			return True
		#Finds next empty space
		while self.input[position] != '0':
			position += 1
			if position == 81:
				return True

		i = 0
		while True:
			print('trying recursion at ' + str(position) + ' with ' + str(i+1))
			if self.position_checker(position, i+1) == True:
				self.input[position] = i + 1
				if self.recursion(position + 1) == False:
					self.input[position] = '0'
					if i == 8:
						print('false 1')
						return False
					else:
						i += 1
					continue
				else:
					return(self.recursion(position + 1))
					i+= 1

			elif i == 8:
				print('false 3')
				self.input[position] = '0'
				i = 0
				return False
			else:
				i += 1






	#This is a function used only for testing. Delete for final project
	def testprint(self):
		for i in self.rows:
			print('')
			for j in i:
				print(str(self.input[j]) + ' ', end = '')
				if (j + 1) % 3 == 0:
					print('|', end = '')
		print('')
'''
root = Tk()
sudoku_gui = SudokuGUI(root)
sudoku_gui.fill()
root.mainloop()
'''
solver = solver()
print('final value is ' + str(solver.recursion(0)))
solver.testprint()
