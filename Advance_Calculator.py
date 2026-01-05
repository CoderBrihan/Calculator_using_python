import tkinter


color_black="#1C1C1C"
color_white="white"

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count=len(button_values)
column_count=len(button_values[0])


window = tkinter.Tk()

window.title("Calculator")

window.resizable(False,False)

frame = tkinter.Frame(window)

label = tkinter.Label(frame,text='0',font=("Arial",45),background=color_black,foreground=color_white,anchor="e")

label.grid(row=0,column=0,columnspan=column_count,sticky="we")

def button_clicked(value):
    if(label.cget("text")=="0"):
        txt=value
    else:
        txt = label.cget("text") + value
    label.configure(text=txt)

def get_ans(equation):
    result = eval(equation)
    label.configure(text=result)
def all_clear():
    label.configure(text="0")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        if value=="=":
            button = tkinter.Button(frame, text=value, font=("Arial", 30), width=column_count - 1, height=1,command=lambda:get_ans(label.cget("text")))
        elif value=="AC":
            button = tkinter.Button(frame, text=value, font=("Arial", 30), width=column_count - 1, height=1,command=all_clear)
        else:
            button = tkinter.Button(frame,text=value,font=("Arial",30),width=column_count-1,height=1,command=lambda value=value:button_clicked(value))
        button.grid(row=row+1,column=column)
label.grid(row=0,column=0)
frame.pack()


window.mainloop()