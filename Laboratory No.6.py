from tkinter import*
window = Tk()
window.geometry("500x500")
window.title("Table")

class Table:
    def __init__(self,win):
        self.num_rows_a = 3
        self.num_cols = 10
        self.num_rows = 4
    def create_table(self):
        #Create a^1, a^2, a^3
        for i in range(1,self.num_rows_a + 1):
            label_text = "a^" + str(i) + "   "
            label = Label(text = label_text)
            label.grid(row = 0, column= i)
        #Create table for a^1
        for i in range(1,self.num_rows + 1):
            label_text1 = str(i)
            label1 = Label(text = label_text1)
            label1.grid(row = i + 1, column = 1)
        #Create table for a^2
        for i in range(1,self.num_rows + 1):
            label_text1 = int(i) * int(i)
            label1 = Label(text = str(label_text1))
            label1.grid(row = i + 1, column = 2)
            # Create table for a^3
        for i in range(1, self.num_rows + 1):
            label_text1 = int(i) * int(i) * int(i)
            label1 = Label(text=str(label_text1))
            label1.grid(row=i + 1, column=3)

mywin = Table(window)
mywin.create_table()
window.mainloop()
