from tkinter import *
 
class GUIDemo(Frame):
    def __init__(self, master=None, pipe=None, player_num=4, ID=0):
        Frame.__init__(self, master)
        self.grid()
        self.pipe = pipe 
        self.player_num = player_num
        self.ID = ID
        self.createWidgets()

    def createWidgets(self):

        self.cards      = []
        # self.listboxes  = []
        color_list = ['Orange', 'Green', 'Yellow', 'Blue', 'Purple']
        for i in range(4):
            card = Label(self, height=5)
            card["text"] = str(i)
            card.grid(row=0, column=2*i, columnspan=2)
            self.cards.append(card)
            # memo
            var_color   = IntVar()
            var_number  = IntVar()
            for j in range(5):
                radio = Radiobutton(self, text=color_list[j], variable=var_color, indicatoron=0, value=j, width=7, bg=color_list[j])
                radio.grid(row=1+j,column=2*i)
                radio = Radiobutton(self, text=str(j+1), variable=var_number, indicatoron=0, value=j, width=5)
                radio.grid(row=1+j,column=2*i+1)

        # button
        hitbut0 = Button(self, text="Hit", command=lambda:self.hitcommand(0))
        hitbut0.grid(row=6, column=1)    
        hitbut1 = Button(self, text="Hit", command=lambda:self.hitcommand(1))
        hitbut1.grid(row=6, column=3)    
        hitbut2 = Button(self, text="Hit", command=lambda:self.hitcommand(2))
        hitbut2.grid(row=6, column=5)    
        hitbut3 = Button(self, text="Hit", command=lambda:self.hitcommand(3))
        hitbut3.grid(row=6, column=7)    
        throwbut0 = Button(self, text="Throw", command=lambda:self.throwcommand(0))
        throwbut0.grid(row=6, column=0)    
        throwbut1 = Button(self, text="Throw", command=lambda:self.throwcommand(1))
        throwbut1.grid(row=6, column=2)    
        throwbut2 = Button(self, text="Throw", command=lambda:self.throwcommand(2))
        throwbut2.grid(row=6, column=4)    
        throwbut3 = Button(self, text="Throw", command=lambda:self.throwcommand(3))
        throwbut3.grid(row=6, column=6)    
        
        # label
        label = Label(self, text="Hint")
        label.grid(row=7, column=0, columnspan=8)

        # hint
        hbut_list = ['None'] * self.player_num
        for i in range(self.player_num):
            plabel = Label(self, text="Player"+str(i))
            plabel.grid(row=8+2*i, column=0, rowspan=2)
            hbut_list[i] = ['None'] * 5 
            for j in range(5):
                hbut_list[i][j] = Button(self, text="Hint #" + str(j+1), command=lambda i=i, j=j:self.hintcommand(i, 1, j+1))
                hbut_list[i][j].grid(row=8+2*i, column=j+1)
                hbut = Button(self, text="Hint", bg=color_list[j], command=lambda i=i, j=j:self.hintcommand(i, 0, j+1))
                hbut.grid(row=8+2*i+1, column=j+1)


    def hitcommand(self, ID):
        self.pipe.write("hit " + str(ID))
        self.pipe.flush()
    
    def throwcommand(self, ID):
        self.pipe.write("throw " + str(ID))
        self.pipe.flush()

    def hintcommand(self, ID, hint_type, hint_number):
        msg = "hint " + str(ID) + " " + str(hint_type) + " " + str(hint_number)
        self.pipe.write(msg)
        self.pipe.flush()


if __name__ == '__main__':
    root = Tk()
    root.title("Hanabi Memo")
    app = GUIDemo(master=root)
    app.mainloop()
 
