from tkinter import *
 
class GUIDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
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

if __name__ == '__main__':
    root = Tk()
    root.title("Hanabi Memo")
    app = GUIDemo(master=root)
    app.mainloop()
 
