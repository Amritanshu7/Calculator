from tkinter import *
import  parser

root = Tk()
root.title('Calculator')

#get user input & place it on display

index=0

def get_variables(num):
    global index
    display.insert(index,num)
    index+=1

def get_operators(operator):
    global index
    display.insert(index, operator)
    index += len(operator)


def clear_all():
    display.delete(0,END)

def backspace():
    curr_string = display.get()
    if len(curr_string):
        new_string = curr_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"ERROR!")

def calculate():
    cur_string = display.get()
    try:
        exp = parser.expr(cur_string).compile()
        result = eval(exp)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"ERROR!")

def fac():
    cur_string = display.get()

    try:
        num = int(cur_string)
        res = 1
        while num>0:
            res = res*num
            num-=1
        clear_all()
        display.insert(0,res)
    except Exception:
        clear_all()
        display.insert(0, "ERROR!")


#adding input field

display = Entry(root)
display.grid(row=1, columnspan=9, sticky=W+E)

#adding buttons to the calculator

Button(root, text="1", command = lambda :get_variables(1)).grid(row=2, column=0)
Button(root, text="2", command = lambda :get_variables(2)).grid(row=2, column=1)
Button(root, text="3", command = lambda :get_variables(3)).grid(row=2, column=2)

Button(root, text="4", command = lambda :get_variables(4)).grid(row=3, column=0)
Button(root, text="5", command = lambda :get_variables(5)).grid(row=3, column=1)
Button(root, text="6", command = lambda :get_variables(6)).grid(row=3, column=2)

Button(root, text="7", command = lambda :get_variables(7)).grid(row=4, column=0)
Button(root, text="8", command = lambda :get_variables(8)).grid(row=4, column=1)
Button(root, text="9", command = lambda :get_variables(9)).grid(row=4, column=2)

Button(root, text="0", command = lambda :get_variables(0)).grid(row=5, column=0)
Button(root, text="=", command = lambda :calculate()).grid(row=5, column=1)
Button(root, text="AC", command = lambda :clear_all()).grid(row=5, column=2)

Button(root, text="/", command = lambda :get_operators("/")).grid(row=2, column=3)
Button(root, text="*", command = lambda :get_operators("*")).grid(row=3, column=3)
Button(root, text="-", command = lambda :get_operators("-")).grid(row=4, column=3)
Button(root, text="+", command = lambda :get_operators("+")).grid(row=5, column=3)

Button(root, text="x!", command = lambda :fac()).grid(row=2, column=4)
Button(root, text="(", command = lambda :get_operators("(")).grid(row=3, column=4)
Button(root, text="pi", command = lambda :get_operators("3.14159")).grid(row=4, column=4)
Button(root, text=".", command = lambda :get_operators(".")).grid(row=5, column=4)

Button(root, text="<-", command = lambda :backspace()).grid(row=2, column=5)
Button(root, text=")", command = lambda :get_operators("(")).grid(row=3, column=5)
Button(root, text="%", command = lambda :get_operators("%")).grid(row=4, column=5)
Button(root, text="exp", command = lambda :get_operators("**")).grid(row=5, column=5)

status = Label(root, text="Developer: Amritanshu", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=6, column=3, columnspan=3, sticky="we")



root.mainloop()