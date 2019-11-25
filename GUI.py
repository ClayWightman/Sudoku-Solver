from tkinter import *


class SudokuTester:
	def __init__(self,master):
		self.master = master
#		master.minsize(500,500)
		master.title('SudokuSolver')


#Creates and packs frames sequentially
		frame_dict = {}
		frame_column = 0
		frame_row = 0
		for i in range(9):
			frame_key = 'frame' + str(i)
			frame_dict[frame_key] = Frame(master, width = 2, highlightbackground = 'black', highlightthickness = 1)
			frame_dict[frame_key].grid(column = frame_column, row = frame_row)
			if frame_column == 2:
				frame_column = 0
				if frame_row == 2:
					frame_row = 0
				else:
					frame_row += 1
			else:
				frame_column += 1


#Creates and packs all of the entry elements in their respective frames
		entry_dict = {}
		entry_row = 0
		entry_column = 0
		for i in range(81):
			entry_key = 'entry' + str(i)
			if i < 9:
				entry_parent = frame_dict['frame0']
			elif i < 18:
				entry_parent = frame_dict['frame1']
			elif i < 27:
				entry_parent = frame_dict['frame2']
			elif i < 36:
				entry_parent = frame_dict['frame3']
			elif i < 45:
				entry_parent = frame_dict['frame4']
			elif i < 54:
				entry_parent = frame_dict['frame5']
			elif i < 63:
				entry_parent = frame_dict['frame6']
			elif i < 72:
				entry_parent = frame_dict['frame7']
			elif i < 81:
				entry_parent = frame_dict['frame8']
			entry_dict[entry_key] = Entry(entry_parent, width = 2, cursor = 'hand2')
			entry_dict[entry_key].grid(column = entry_column, row = entry_row)
			if entry_column == 2:
				entry_column = 0
				if entry_row == 2:
					entry_row = 0
				else:
					entry_row += 1
			else:
				entry_column += 1
		submit_button = Button(master, text = 'submit')
		submit_button.grid(column = 1, row = 3)

root = Tk()
sudoku_gui = SudokuTester(root)
root.mainloop()