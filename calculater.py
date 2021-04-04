from tkinter import*
root =Tk()
root.geometry("300x340+100+50")
root.title("ANKIT calc")

Tops= Frame(root,width=300,height=20,bd=4)
Tops.pack(side=TOP)


Below=Frame(root,width=3000,height=300, bd=4)
Below.pack(side=BOTTOM)


def btnClick(numbers):
    global operator
    operator= operator+str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator=""
    text_input.set("")

def btnEqual():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

operator=""
text_input=StringVar()

txtdisplay=Entry(Tops,font=('arial',18,'bold'),textvariable=text_input,width=21,bd=4,justify='right')
txtdisplay.grid(row=0,column=0)


btn7=Button(Below,padx=16,pady=1,bd=4, fg="black",font=('arial',16,'bold'),width=2,height=2,text="7",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Below,padx=16,pady=1,bd=4, fg="red",font=('arial',16,'bold'),width=2,height=2,text="8",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Below,padx=16,pady=1,bd=4, fg="red",font=('arial',16,'bold'),width=2,height=2,text="9",command=lambda:btnClick(9)).grid(row=2,column=2)

btn1=Button(Below,padx=16,pady=1,bd=4,fg="pink",font=('arial',16,'bold'),width=2,height=2,text="1",command=lambda:btnClick(1)).grid(row=0,column=0)
btn2=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="2",command=lambda:btnClick(2)).grid(row=0,column=1)
btn3=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="3",command=lambda:btnClick(3)).grid(row=0,column=2)

btn4=Button(Below,padx=16,pady=1,bd=4,fg="green",font=('arial',16,'bold'),width=2,height=2,text="4",command=lambda:btnClick(4)).grid(row=1,column=0)
btn5=Button(Below,padx=16,pady=1,bd=4,fg="brown",font=('arial',16,'bold'),width=2,height=2,text="5",command=lambda:btnClick(5)).grid(row=1,column=1)
btn6=Button(Below,padx=16,pady=1,bd=4,fg="blue",font=('arial',16,'bold'),width=2,height=2,text="6",command=lambda:btnClick(6)).grid(row=1,column=2)

btnmul=Button(Below,padx=16,pady=1,bd=4,fg="orange",font=('arial',16,'bold'),width=2,height=2,text="*",command=lambda:btnClick("*")).grid(row=0,column=3)
btnadd=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="+",command=lambda:btnClick("+")).grid(row=1,column=3)
btnsub=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="-",command=lambda:btnClick("-")).grid(row=2,column=3)

btnequal=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="=",command=btnEqual).grid(row=4,column=0)
btndiv=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="/",command=lambda:btnClick("/")).grid(row=4,column=1)
btnclear=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="C",command=btnClear).grid(row=4,column=2)
btn0=Button(Below,padx=16,pady=1,bd=4, fg="black",font=('arial',16,'bold'),width=2,height=2,text="0",command=lambda:btnClick(0)).grid(row=4,column=3)
btnmodulus=Button(Below,padx=16,pady=1,bd=4, fg="black",font=('arial',16,'bold'),width=2,height=2,text="%",command=lambda:btnClick("%")).grid(row=4,column=4)
btndecimal=Button(Below,padx=16,pady=1,bd=4, fg="black",font=('arial',16,'bold'),width=2,height=2,text=".",command=lambda:btnClick(".")).grid(row=2,column=4)
root.mainloop()

