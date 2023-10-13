import tkinter as tk
calculation=""
def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
    pass
def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"error")
        
def clear_field ():
    global calculation 
    calculation=""
    text_result.delete(1.0,"end")
    
    pass
root=tk.Tk()
root.geometry("300x275")
text_result=tk.Text(root,height=2,width=16,font=("ariel",24))
text_result.grid(columnspan=5)
btn1=tk.Button(root,text="1",command=lambda:add_to_calculation(1)
               ,width=5,font=("arial",15))
btn1.grid(row=2,column=1)
btn2=tk.Button(root,text="2",command=lambda:add_to_calculation(2)
               ,width=5,font=("arial",15))
btn2.grid(row=2,column=2)
btn3=tk.Button(root,text="3",command=lambda:add_to_calculation(3)
               ,width=5,font=("arial",15))
btn3.grid(row=2,column=3)
btn4=tk.Button(root,text="4",command=lambda:add_to_calculation(4)
               ,width=5,font=("arial",15))
btn4.grid(row=3,column=1)
btn5=tk.Button(root,text="5",command=lambda:add_to_calculation(5)
               ,width=5,font=("arial",15))
btn5.grid(row=3,column=2)
btn6=tk.Button(root,text="6",command=lambda:add_to_calculation(6)
               ,width=5,font=("arial",15))
btn6.grid(row=3,column=3)
btn7=tk.Button(root,text="7",command=lambda:add_to_calculation(7)
               ,width=5,font=("arial",15))
btn7.grid(row=4,column=1)
btn8=tk.Button(root,text="8",command=lambda:add_to_calculation(8)
               ,width=5,font=("arial",15))
btn8.grid(row=4,column=2)
btn9=tk.Button(root,text="9",command=lambda:add_to_calculation(9)
               ,width=5,font=("arial",15))
btn9.grid(row=4,column=3)
btn0=tk.Button(root,text="0",command=lambda:add_to_calculation(0)
               ,width=5,font=("arial",15))
btn0.grid(row=5,column=2)
btn_plus=tk.Button(root,text="+",command=lambda:add_to_calculation("+")
               ,width=5,font=("arial",15))
btn_plus.grid(row=2,column=4)
btn_minus=tk.Button(root,text="-",command=lambda:add_to_calculation("-")
               ,width=5,font=("arial",15))
btn_minus.grid(row=3,column=4)
btn_multiplication=tk.Button(root,text="x",command=lambda:add_to_calculation("x")
               ,width=5,font=("arial",15))
btn_multiplication.grid(row=4,column=4)
btn_div=tk.Button(root,text="/",command=lambda:add_to_calculation("/")
               ,width=5,font=("arial",15))
btn_div.grid(row=5,column=4)
btn_open=tk.Button(root,text="(",command=lambda:add_to_calculation("(")
               ,width=5,font=("arial",15))
btn_open.grid(row=5,column=1)
btn_close=tk.Button(root,text=")",command=lambda:add_to_calculation(")")
               ,width=5,font=("arial",15))
btn_close.grid(row=5,column=3)
btn_equal=tk.Button(root,text="=",command=evaluate_calculation
               ,width=5,font=("arial",15))
btn_equal.grid(row=6,column=1,columnspan=2)
btn_clear=tk.Button(root,text="C",command=clear_field
               ,width=5,font=("arial",15))
btn_clear.grid(row=6,column=3,columnspan=4)
root.mainloop()
    
    