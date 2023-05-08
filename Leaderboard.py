import tkinter as tk
import tkinter.scrolledtext as st


class leaderboard():
    def __init__(self):
        try:
            print("Leaderboards is ON")
            self.file = open("leaderboard.txt", "a+")
            # opening the file in write mode, + creates the file if it doesn't exist
            self.file.write("Toto 100 2,Harald 200 3")
            self.data = self.file.read()
            
            print(self.data)
            # splitting the text it further when '.' is seen.
            self.dataList = self.data.replace('\n', ' ').split(",")
            print(self.dataList[0])
            print(self.dataList[1])
            self.file.close()
        except AttributeError:
             print("Could not load file") 
    
    def writeToFile(self, score, streak, hasStreak, hasLoosingCondition):
        try: 
            self.file = open("leaderboard.txt", "a+")
            # opening the file in write mode, + creates the file if it doesn't exist

        except AttributeError: 
            print("Could not write to file") 
    
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
        text_area.insert(tk.INSERT,self.data)

        # Making the text read only
        text_area.configure(state ='disabled')
        win.mainloop()

