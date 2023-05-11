import tkinter as tk
import tkinter.scrolledtext as st


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
            # radera sista elementet som är ""
            #if(len(self.dataList)>1):
            #    self.dataList.pop()
            #print(self.dataList)
            #self.sort()
            #print(self.dataList)
            self.file.close()

            #self.writeToFile("Tomas","10","100")
        except AttributeError:
             print("Could not load file") 
    
    def addScore(self, inputtxt, score, streak):
        try: 
            name = inputtxt.get(1.0, "end-1c")
            self.file = open("leaderboard.txt", "a+")
            # opening the file in write mode, + creates the file if it doesn't exist
            self.file.write("\n" + name+" "+score+" "+streak)

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
                background = 'red',
                foreground = "white").grid(column = 0,
                                            row = 0)
        # TextBox Creation
        inputtxt = tk.Text(saveWin,
                        height = 2,
                        width = 20).grid(column = 0,
                                            row = 2)
        printButton = tk.Button(saveWin,
                                text = "Save", 
                                command = lambda: self.addScore(inputtxt,str(score),str(streak))).grid(column = 2,
                                                                                                  row =3)

    
        saveWin.mainloop()


        '''
        saveWin = tk.TK()
        saveWin.title("Save name") 
        # Title Label
       
        tk.Label(saveWin,
                text = "Write your name",
                font = ("Times New Roman", 15),
                background = 'white',
                foreground = "black").grid(column = 0,
                                            row = 0)


        # TextBox Creation
        inputtxt = tk.Text(saveWin,
                        height = 5,
                        width = 20)
        
        inputtxt.pack()
        
        # Button Creation
        printButton = tk.Button(saveWin,
                                text = "Save", 
                                command = lambda: self.addScore(str(score),str(streak)))
        printButton.pack()
        
        # Label Creation
        lbl = tk.Label(saveWin, text = "")
        lbl.pack()
        


        # save button
        saveWin.mainloop()
        '''
    '''
    0: Harald 200 3,
    1: Toto 100 2,
    2: Toto 10 5,
    3: Toto 100 2,
    4: Harald 200 3,
    5: Toto 1 0, 
    6: Harald 4000 8,
    '''
    
    def window(self): 

        # Creating tkinter window
        win = tk.Tk()
        win.title("Leaderboard")

        # Title Label
        tk.Label(win,
                text = "Name Score Streak",
                font = ("Times New Roman", 15),
                background = 'green',
                foreground = "white").grid(column = 0,
                                            row = 0)

        # Creating scrolled text area
        # widget with Read only by
        # disabling the state
        text_area = st.ScrolledText(win,
                                    width = 30,
                                    height = 8,
                                    font = ("Times New Roman",
                                            15))

        text_area.grid(column = 0, pady = 10, padx = 10)

        # Inserting Text which is read only
        text_area.insert(tk.INSERT,"Name:      Score:    Streak:\n")
        text_area.insert(tk.INSERT,self.data)

        # Making the text read only
        text_area.configure(state ='disabled')
        win.mainloop()

