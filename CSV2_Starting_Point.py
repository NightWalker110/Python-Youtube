import csv
from tkinter import *

filepath = '/Users/henrygilbert/Dev/Cars.csv'

File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)

list_of_entries = []
for x in list(range(1,len(Data))):
	list_of_entries.append(Data[x][0])
	
class Window:
	
	def __init__(self, root):
		self.root = root
		self.root.geometry('280x300')
		self.brandlabel = Label(self.root, text="Brand").grid(row=1,
		                                                      column=0,
		                                                      sticky='w')
		
		self.stockpricelabel = Label(self.root, text="Stock Price (USD)").grid(row=2,
		                                                                       column=0,
		                                                                       sticky='w')
		
		self.countrylabel = Label(self.root, text="Country").grid(row=3,
		                                                          column=0,
		                                                          sticky='w')
		
		self.datefoundedlabel = Label(self.root, text="Date Founded").grid(row=4,
		                                                                   column=0,
		                                                                   sticky='w')
		
		self.listbox1 = Listbox(self.root)
		self.listbox1.grid(row=0, column=0)
		# Insert column entries into Listbox
		
		self.button1 = Button(self.root, text="Update", command=self.update)
		self.button1.grid(row=5, column=0)
		
		self.brandlabel2 = Label(self.root, text='')
		self.brandlabel2.grid(row=1, column=1)
		self.stockpricelabel2 = Label(self.root, text='')
		self.stockpricelabel2.grid(row=2, column=1)
		self.countrylabel2 = Label(self.root, text='')
		self.countrylabel2.grid(row=3, column=1)
		self.datefoundedlabel2 = Label(self.root, text='')
		self.datefoundedlabel2.grid(row=4, column=1)
	
	def update(self):
		# Add a function to update GUI values on button press
		return None
	pass

def main():
	root = Tk()
	win1 = Window(root)
	win1.root.mainloop()

main()