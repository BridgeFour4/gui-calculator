from tkinter import *
import random
class Application(Frame):
    def __init__(self,master):

        super(Application,self).__init__(master)
        self.grid()
        self.number1 = ""
        self.number2 = ""
        self.change = 0
        self.operator = ""
        self.total = 0
        self.create_widgets()

    def create_widgets(self):
        self.labelcount = Label(self,text="0")
        self.labelcount.grid()

        self.bttn1= Button(self, text="1", command=add_one)
        self.bttn2 = Button(self, text="2", command=add_two)
        self.bttn3 = Button(self, text="3", command=add_three)
        self.bttn4 = Button(self, text="4", command=add_four)
        self.bttn5 = Button(self, text="5", command=add_five)
        self.bttn6 = Button(self, text="6", command=add_six)
        self.bttn7 = Button(self, text="7", command=add_seven)
        self.bttn8 = Button(self, text="8", command=add_eight)
        self.bttn9 = Button(self, text="9", command=add_nine)
        self.bttn0 = Button(self, text="0", command=add_zero)

        self.bttn1.grid()
        self.bttn2.grid()
        self.bttn3.grid()
        self.bttn4.grid()
        self.bttn5.grid()
        self.bttn6.grid()
        self.bttn7.grid()
        self.bttn8.grid()
        self.bttn9.grid()
        self.bttn0.grid()

        self.bttnadd = Button(self,text="+",command=self.add_count)
        self.bttnsub = Button(self, text="-", command=self.subtract_count)
        self.bttntimes = Button(self, text="*", command=self.times_count)
        self.bttndiv = Button(self, text="/", command=self.divide_count)
        self.bttnequals = Button(self, text="/", command=self.total_up)

        self.bttnadd.grid()
        self.bttnsub.grid()
        self.bttntimes.grid()
        self.bttndiv.grid()


    def add_count(self):
        self.operator="+"
        self.change = 1

    def subtract_count(self):
        self.operator = "-"
        self.change = 1

    def times_count(self):
        self.operator = "*"
        self.change = 1

    def divide_count(self):
        self.operator = "/"
        self.change = 1

    def total_up(self):
        if self.opertor == "+":
            self.total = int(self.number1)+int(self.number2)
        elif self.opertor == "-":
            self.total = int(self.number1) - int(self.number2)
        elif self.opertor == "*":
            self.total = int(self.number1) * int(self.number2)
        elif self.opertor == "/":
            self.total = int(self.number1) / int(self.number2)
        self.change=0
        self.number1=""
    def clear(self):
        pass



root=Tk()
root.title("Click Counter")
root.geometry("100x200")
app=Application(root)

root.mainloop()