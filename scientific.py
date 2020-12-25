from tkinter import *
from math import *
def btnclick(numbers):
 global text_Input, operator
 operator = operator + str(numbers)
 text_Input.set(operator)
 
def btnclearDisplay():
 global operator
 operator=''
 text_Input.set('')

def btnEqualInput():
 global text_Input, operator
 operator = str(eval(operator))
 text_Input.set(operator)
 operator = ''

cal=Tk()
cal.title("Scientific Calculator")
#cal.geometry("800x400")
operator=''
text_Input = StringVar()
txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable=text_Input, bd=10,insertwidth=10, bg="powder blue", justify='right').grid(columnspan=4)
#Button=============================================================================
btn7=Button(cal,padx=16,bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="7",command=lambda:btnclick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="8",command=lambda:btnclick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="9",command=lambda:btnclick(9)).grid(row=1,column=2)
Addition=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="+",command=lambda:btnclick("+")).grid(row=1,column=3)
#====================================================================================
btn4=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="4",command=lambda:btnclick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="5",command=lambda:btnclick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="6",command=lambda:btnclick(6)).grid(row=2,column=2)
Subtraction=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="-",command=lambda:btnclick("-")).grid(row=2,column=3)
#====================================================================================
btn3=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="3",command=lambda:btnclick(3)).grid(row=3,column=0)
btn2=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="2",command=lambda:btnclick(2)).grid(row=3,column=1)
btn1=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="1",command=lambda:btnclick(1)).grid(row=3,column=2)
Multiplication=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="*",command=lambda:btnclick("*")).grid(row=3,column=3)
#====================================================================================
btn0=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="0",command=lambda:btnclick(0)).grid(row=4,column=0)
btnclear=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="C",command=btnclearDisplay).grid(row=4,column=1)
btnEquals=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="=",command=lambda:btnEqualInput()).grid(row=4,column=2)
division=Button(cal,padx=16, bd=6,fg="black",font=('arial',15,'bold'),width=2,
text="/",command=lambda:btnclick("/")).grid(row=4,column=3)

#Trignometry Function=================================================================
cos=Button(cal,padx=2, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=3,
text="cosθ",command=lambda:btnclick("cos(")).grid(row=1,column=4)
tan=Button(cal,padx=4, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=3,
text="tanθ",command=lambda:btnclick("tan(")).grid(row=2,column=4)
sin=Button(cal,padx=4, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=3,
text="sinθ",command=lambda:btnclick("sin(")).grid(row=3,column=4)
log=Button(cal,padx=4, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=3,
text="log",command=lambda:btnclick("log(")).grid(row=4,column=4)
#====================================================================================
sqrt=Button(cal,padx=8, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=2,
text="√",command=lambda:btnclick("sqrt(")).grid(row=1,column=5)
m=Button(cal,padx=8, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=2,
text="m+",command=lambda:btnclick("m+")).grid(row=2,column=5)
cosin=Button(cal,padx=3, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=3,
text="cosin",command=lambda:btnclick("cosin(")).grid(row=3,column=5)
cosec=Button(cal,padx=4, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=4,
text="cosec",command=lambda:btnclick("cosec(")).grid(row=4,column=5)
br=Button(cal,padx=16, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=1,
text=")",command=lambda:btnclick(")")).grid(row=1,column=6)
br1=Button(cal,padx=16, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=1,
text="(",command=lambda:btnclick("(")).grid(row=2,column=6)
x=Button(cal,padx=16, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=1,
text="x2",command=lambda:btnclick("x2")).grid(row=3,column=6)
m1=Button(cal,padx=16, bd=6,fg="white",bg="blue",font=('arial',15,'bold'),width=1,
text=".",command=lambda:btnclick(".")).grid(row=4,column=6)
#====================================================================================
cal.mainloop()
