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
		text_file = open('Sudoku-File.txt','r')
		self.input = text_file.readline(81)
		text_file.close()


	def position_checker(self, position, value):
		position = int(position / 9 * 9)
		for i in range(9):
			if value == input[position]:
				return False
		



root = Tk()
sudoku_gui = SudokuGUI(root)
sudoku_gui.fill()
root.mainloop()
