import tkinter as tk
import tkinter.scrolledtext as st
from functools import partial
from tkinter import ttk


class leaderboard():
    def __init__(self):
        try:
            print("Leaderboards is ON")
            #  skapa filen om den inte finns
            self.file = open("leaderboard.txt", "a+")
            self.file.close()
            # öppna filen i read mode
            self.file = open("leaderboard.txt", "r")
            self.data = self.file.read()
            # splitting the text it further when '\n' is seen.
            self.dataList = self.data.split("\n")
            self.file.close()
            self.sort()
        except AttributeError:
             print("Could not load file") 
    
    def addScore(self, saveWin, name, score, streak):
        try: 
            #name = "jakob" #inputtxt.get(1.0, "end-1c")
            self.file = open("leaderboard.txt", "a+")
            # opening the file in write mode, + creates the file if it doesn't exist
            self.file.write("\n" + name+" "+score+" "+streak)
            saveWin.destroy()
        except AttributeError: 
            print("Could not write to file") 

    def sort(self):
        '''
        Sorts the leaderboard using insertion sort based on the highest score

        '''
        for row in range(1, len(self.dataList)):
            scoreOnRow = self.getScore(row)
            rowAbove = row - 1
            # As long as rowAbove is greater than row 0 and
            # score on the row we (ScoreOnRow) are looking at is greater than the score on the rowAbove
            # we want to switch places on the row with greater score to a higher index.         
            while rowAbove >= 0 and scoreOnRow > self.getScore(rowAbove):
                temp = self.dataList[rowAbove]                          # Saves data on rowAbove
                self.dataList[rowAbove] = self.dataList[rowAbove+1]     # Assigns the value on rowAbove+1 to rowAbove
                self.dataList[rowAbove+1] = temp                        # Assigns the value that stood on rowAbove to rowAbove+1       
                rowAbove = rowAbove - 1                                 # Decrements rowabove to compare with the row above rowAbove.
                


        
    # läsa in allt o-ordning 
    # sortera dataList med insertionsort 
    def getScore(self, index):
       row = self.dataList[index].split(" ")
       return int(row[1])
    
    def saveScore(self, score, streak):
        # Creating tkinter window
        saveWin = tk.Tk()
        saveWin.title("save score")

        # Title Label
        tk.Label(saveWin,
                text = "write your name",
                font = ("Times New Roman", 15),
                foreground = "black").grid(column = 0,
                                            row = 0)
        # TextBox Creation
        inputtxt = tk.Text(saveWin,
                        height = 2,
                        width = 20)
        inputtxt.grid(column = 0,row = 2, padx=10, pady=10)


        printButton = tk.Button(saveWin,
                                text = "Save", 
                                command = lambda: self.addScore(saveWin,inputtxt.get("1.0", 'end-1c'),str(score),str(streak)))
        printButton.grid(column = 2,row =2, padx=10, pady=10)
                                
    
        saveWin.mainloop()
    
    def window(self): 

        # Creating tkinter window
        win = tk.Tk()
        win.title("Leaderboard")

        # Title Label
        tk.Label(win,
                text = "LEADERBOARD",
                font = ("Times New Roman", 15),
                foreground = "black").grid(column = 0,
                                            row = 0)

        # Creating scrolled text area
        # widget with Read only by
        # disabling the state

        # Add a Treeview widget
        tree = ttk.Treeview(win, column=("c1", "c2", "c3"), show='headings', height=5)

        tree.column("# 1")
        tree.heading("# 1", text="NAME")
        tree.column("# 2")
        tree.heading("# 2", text="SCORE")
        tree.column("# 3")
        tree.heading("# 3", text="STREAK")

        # Insert the data in Treeview widget
        for row in self.dataList:
            rowData = row.split(" ")
            tree.insert('', 'end', text="1", values=(rowData[0], rowData[1], rowData[2]))

        tree.grid(column = 0, pady = 10, padx = 10)

        scrollbar = ttk.Scrollbar(win, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')

        '''text_area = st.ScrolledText(win,
                                    width = 30,
                                    height = 8,
                                    font = ("Times New Roman",
                                            15))

        text_area.grid(column = 0, pady = 10, padx = 10)

        # Inserting Text which is read only
        text_area.insert(tk.INSERT,"Name:      Score:    Streak:\n")
        for row in self.dataList:
            rowData = row.split(" ")
            text_area.insert(tk.INSERT,"Name: "+rowData[0]+"  Score: "+rowData[1]+"  Streak: "+rowData[2]+"\n")

        # Making the text read only
        text_area.configure(state ='disabled')'''

        
        win.mainloop()

