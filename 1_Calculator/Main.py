import tkinter as tk
from tkinter import *

def Addition():
    n1=float(num1.get())#get: methodos tou objext Entry
    n2= float(num2.get())
    add=round(n1+n2,2)
    result['text']=f' {n1} + {n2} = {add}'

def Substraction():
    n1=float(num1.get())#get: methodos tou objext Entry
    n2= float(num2.get())
    sub=round(n1-n2,2)
    result['text']=f' {n1} - {n2} = {sub}'

def Multiply():
    n1=float(num1.get())#get: methodos tou objext Entry
    n2= float(num2.get())
    mult=round(n1*n2,2)
    result['text']=f' {n1} * {n2} = {mult}'

def Mod():
    n1=float(num1.get())#get: methodos tou objext Entry
    n2= float(num2.get())
    try:
        mod=round(n1%n2,2)
    except:
        result['text']='oxi diairesi me 0'
    else:
        result['text']=f' {n1} mod {n2} = {mod}'

def Div():
    n1=float(num1.get())#get: methodos tou objext Entry
    n2= float(num2.get())
    try:#an ola pan kala tha tha ektelesei tis entoles
        div=round(n1//n2,2)
    except:#an yparxei problima tou leo ti na kanei gia na min paro sfalma stin ektelesi
        result['text']='oxi diairesi me 0'
    else:
        result['text']=f' {n1} div {n2} = {div}'   

def Pow():
    n1=float(num1.get())#get: methodos tou objext Entry
    n2= float(num2.get())
    mult=round(pow(n1,n2),2)
    result['text']=f' {n1} ^ {n2} = {mult}'        
    
def Division():
    n1=float(num1.get())#get: methodos tou objext Entry
    n2= float(num2.get())
    try:#an ola pan kala tha tha ektelesei tis entoles
        div=round(n1/n2,2)
    except:#an yparxei problima tou leo ti na kanei gia na min paro sfalma stin ektelesi
        result['text']='oxi diairesi me 0'
    else:
        #afou den yparxei sfalma emfanizei to apotelesma
        result['text']=f' {n1} / {n2} = {div}'


root = tk.Tk()
root.title("calculator")#title: methodos tou object root
root.geometry('300x400')

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
labelFrame = tk.Frame(root)
labelFrame.grid(row=0, column=0, columnspan=2, sticky="ew")
labelFrame.grid_columnconfigure(0, weight=1)
label=Label(labelFrame, text="\ncalculator\n",font=("Arial",19))
label.grid(row=0,column=0, sticky="ew")

firstNumberLabel=Label(root,text="1ος αριθμός:",)
firstNumberLabel.grid(row=1,column=0)

num1 = Entry(root)
num1.grid(row=1,column=1)
secondNumberLabel=Label(root,text="2ος αριθμός:")
secondNumberLabel.grid(row=2,column=0)
num2 = Entry(root)
num2.grid(row=2,column=1)

buttonsFrame = tk.Frame(root)
buttonsFrame.grid(row=3, column=0, columnspan=2)

btn1=Button(buttonsFrame, text="+", command=Addition)
btn2=Button(buttonsFrame, text="-", command=Substraction)
btn3=Button(buttonsFrame, text="*", command=Multiply)
btn4=Button(buttonsFrame, text="/", command=Division)
btn5=Button(buttonsFrame, text="mod", command=Mod)
btn6=Button(buttonsFrame, text="div", command=Div)
btn7=Button(buttonsFrame, text="pow", command=Pow)
btn1.grid(row=2,column=0,padx=2)
btn2.grid(row=2,column=1,padx=2)
btn3.grid(row=2,column=2,padx=2)
btn4.grid(row=2,column=3,padx=2)
btn5.grid(row=3,column=0,padx=2)
btn6.grid(row=3,column=1,padx=2)
btn7.grid(row=3,column=2,padx=2)

result=Label(root,bg="#ffe600",fg="#000000")
result.grid(row=5,column=0,columnspan=4)

root.mainloop()
buttonsFrame.mainloop()
