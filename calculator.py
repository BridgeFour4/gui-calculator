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
        self.count= Text(self,height=1,width=24)
        self.count.grid(row=0,column=0,columnspan=4)

        self.bttn1= Button(self, text="1", command=self.add_one,width=6)
        self.bttn2 = Button(self, text="2", command=self.add_two,width=6)
        self.bttn3 = Button(self, text="3", command=self.add_three,width=6)
        self.bttn4 = Button(self, text="4", command=self.add_four,width=6)
        self.bttn5 = Button(self, text="5", command=self.add_five,width=6)
        self.bttn6 = Button(self, text="6", command=self.add_six,width=6)
        self.bttn7 = Button(self, text="7", command=self.add_seven,width=6)
        self.bttn8 = Button(self, text="8", command=self.add_eight,width=6)
        self.bttn9 = Button(self, text="9", command=self.add_nine,width=6)
        self.bttn0 = Button(self, text="0", command=self.add_zero,width=6)

        self.bttn1.grid(row=1,column=0)
        self.bttn2.grid(row=1,column=1)
        self.bttn3.grid(row=1,column=2)
        self.bttn4.grid(row=2,column=0)
        self.bttn5.grid(row=2,column=1)
        self.bttn6.grid(row=2,column=2)
        self.bttn7.grid(row=3,column=0)
        self.bttn8.grid(row=3,column=1)
        self.bttn9.grid(row=3,column=2)
        self.bttn0.grid(row=4,column=0)

        self.bttnclear = Button(self, text="c", command=self.clear,width=6)
        self.bttnadd = Button(self,text="+",command=self.add_count,width=6)
        self.bttnsub = Button(self, text="-", command=self.subtract_count,width=6)
        self.bttntimes = Button(self, text="*", command=self.times_count,width=6)
        self.bttndiv = Button(self, text="/", command=self.divide_count,width=6)
        self.bttnequals = Button(self, text="=", command=self.total_up,width=6)

        self.bttnadd.grid(row=1,column=3)
        self.bttnsub.grid(row=2,column=3)
        self.bttntimes.grid(row=3,column=3)
        self.bttndiv.grid(row=4,column=3)
        self.bttnclear.grid(row=4,column=1)
        self.bttnequals.grid(row=4, column=2)



    def add_one(self):
        if self.change==0:
            self.number1+="1"
            self.number2=""
            self.total=""
            self.count.delete(0.0,END)
            self.count.insert(0.0,self.number1)
        else:
            self.number2+="1"
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number2)

    def add_two(self):
        if self.change==0:
            self.number1+="2"
            self.number2=""
            self.total=""
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number1)
        else:
            self.number2+="2"
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number2)

    def add_three(self):
        if self.change == 0:
            self.number1 += "3"
            self.number2 = ""
            self.total = ""
            self.count.delete(0.0, END)
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number1)
        else:
            self.number2 += "3"
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number2)

    def add_four(self):
        if self.change == 0:
            self.number1 += "4"
            self.number2 = ""
            self.total = ""
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number1)
        else:
            self.number2 += "4"
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number2)

    def add_five(self):
        if self.change == 0:
            self.number1 += "5"
            self.number2 = ""
            self.total = ""
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number1)
        else:
            self.number2 += "5"
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number2)

    def add_six(self):
        if self.change == 0:
            self.number1 += "6"
            self.number2 = ""
            self.total = ""
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number1)
        else:
            self.number2 += "6"
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number2)

    def add_seven(self):
        if self.change == 0:
            self.number1 += "7"
            self.number2 = ""
            self.total = ""
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number1)
        else:
            self.number2 += "7"
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number2)

    def add_eight(self):
        if self.change == 0:
            self.number1 += "8"
            self.number2 = ""
            self.total = ""
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number1)
        else:
            self.number2 += "8"
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number2)

    def add_nine(self):
        if self.change == 0:
            self.number1 += "9"
            self.number2 = ""
            self.total = ""
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number1)
        else:
            self.number2 += "9"
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number2)

    def add_zero(self):
        if self.change == 0:
            self.number1 += "0"
            self.number2 = ""
            self.total = ""
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number1)
        else:
            self.number2 += "0"
            self.count.delete(0.0, END)
            self.count.insert(0.0, self.number2)





    def add_count(self):
        self.operator="+"
        self.change = 1
        self.number2 = ""

    def subtract_count(self):
        self.operator = "-"
        self.change = 1
        self.number2 = ""

    def times_count(self):
        self.operator = "*"
        self.change = 1
        self.number2 = ""

    def divide_count(self):
        self.operator = "/"
        self.change = 1
        self.number2 = ""

    def total_up(self):
        if self.number1!="":
            if self.operator == "+":
                self.total = int(self.number1)+int(self.number2)
            elif self.operator == "-":
                self.total = int(self.number1) - int(self.number2)
            elif self.operator == "*":
                self.total = int(self.number1) * int(self.number2)
            elif self.operator == "/":
                self.total = int(self.number1) / int(self.number2)
        else:
            if self.operator == "+":
                self.total = self.total + int(self.number2)
            elif self.operator == "-":
                self.total = self.total - int(self.number2)
            elif self.operator == "*":
                self.total = self.total * int(self.number2)
            elif self.operator == "/":
                self.total = self.total / int(self.number2)

        self.count.delete(0.0, END)
        self.count.insert(0.0, self.total)
        self.change=0
        self.number1=""
    def clear(self):
        self.change=0
        self.operator=""
        self.number1=""
        self.number2=""
        self.total=0
        self.count.delete(0.0, END)



root=Tk()
root.title("Click Counter")
root.geometry("400x400")
app=Application(root)

root.mainloop()