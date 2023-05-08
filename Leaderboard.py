

class leaderboard():
    def __init__(self):
        try:
            self.file = open("leaderboard.txt", "a+")
            # opening the file in write mode, + creates the file if it doesn't exist
            self.data = self.file.read()
            # splitting the text it further when '.' is seen.
            self.dataList = self.data.replace('\n', ' ').split("|")
            print(self.dataList)
            self.file.close()
        except AttributeError:
             print("Could not load file") 
    
    def writeToFile(self, score, streak, hasStreak, hasLoosingCondition):
        try: 
            self.file = open("leaderboard.txt", "a+")
            # opening the file in write mode, + creates the file if it doesn't exist

        except AttributeError: 
            print("Could not write to file") 
