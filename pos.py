from items import items
import tkinter as tk

currentCode = ""
currentBillItems = []
totalBill = 0
billframe = None
totalLabel = None

def setCurrentCode(code):
    global currentCode
    currentCode+=code

def getItem():
    global currentCode
    itemlist = list(filter(lambda x:x['code']==currentCode,items))
    if(len(itemlist)):
        currentBillItems.append(itemlist[0])
        print(currentBillItems)
        display['text']  = f"{list(itemlist)[0]['item']}   {list(itemlist)[0]['price']}"
    currentCode = ""

def totalPrice():
    global totalBill
    global currentBillItems
    global billframe
    global totalLabel
    totalBill = sum(item['price'] for item in currentBillItems)
    display['text'] = f"Total:  {totalBill}"
    billframe = tk.Frame(invoice)
    billframe.grid(column=0,row=1)
    for billIndex,billItem in enumerate(currentBillItems):
        billItemLabel = tk.Label(billframe,text=f"{billItem['item']}",bg="khaki",anchor="w")
        billItemLabel.grid(column=0,row=billIndex,sticky=tk.W+tk.E)
        billPriceLabel = tk.Label(billframe,text=f"{billItem['price']}",bg="khaki",anchor="e")
        billPriceLabel.grid(column=1,row=billIndex,sticky=tk.W+tk.E)
    totalLabel = tk.Label(invoice,text=f"Total:    {totalBill}",bg="khaki")
    totalLabel.grid(row=2,column=0)

def reset():
    global currentBillItems
    global totalBill
    global billframe
    global totalLabel
    currentBillItems = []
    totalBill = 0
    display['text'] = ""
    if billframe and totalLabel:
        billframe.destroy()
        totalLabel.destroy()

window = tk.Tk()
window.title("POS project")

frame = tk.Frame(window)
frame.pack()

display = tk.Label(frame,width=9,bg="lightgreen",height=2)
display.grid(row=0,column=0,columnspan=3,sticky=tk.W+tk.E,pady=10)

seven = tk.Button(frame,text="7",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('7'))
seven.grid(row=1,column=0)
eight = tk.Button(frame,text="8",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('8'))
eight.grid(row=1,column=1)
nine = tk.Button(frame,text="9",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('9'))
nine.grid(row=1,column=2)
four = tk.Button(frame,text="4",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('4'))
four.grid(row=2,column=0)
five = tk.Button(frame,text="5",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('5'))
five.grid(row=2,column=1)
six = tk.Button(frame,text="6",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('6'))
six.grid(row=2,column=2)
one = tk.Button(frame,text="1",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('1'))
one.grid(row=3,column=0)
two = tk.Button(frame,text="2",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('2'))
two.grid(row=3,column=1)
three = tk.Button(frame,text="3",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('3'))
three.grid(row=3,column=2)
zero = tk.Button(frame,text="0",bg="yellow",width=3,font=3,command=lambda:setCurrentCode('0'))
zero.grid(row=4,column=0)
enter = tk.Button(frame,text="Enter",bg="skyblue",width=3,font=3,command=getItem)
enter.grid(row=4,column=1,columnspan=2,sticky=tk.W+tk.E)
total = tk.Button(frame,text="Total",bg="red",width=3,font=3,command=totalPrice)
total.grid(row=5,column=0,columnspan=3,sticky=tk.W+tk.E)
reset = tk.Button(frame,text="Reset",bg="pink",width=3,font=3,command=reset)
reset.grid(row=6,column=0,columnspan=3,sticky=tk.W+tk.E)

invoice =  tk.Frame(frame,relief='solid',bd=1,bg="khaki")
invoice.grid(row=7,column=0,sticky=tk.W+tk.E,pady=10,columnspan=3)
invoice.grid_columnconfigure(0, weight=1)

bill = tk.Label(invoice,bg="khaki", text="Invoice", font=2)
bill.grid(column=0,row=0,sticky="ew")

window.mainloop()
