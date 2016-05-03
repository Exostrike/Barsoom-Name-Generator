import tkinter as tk
import random

printout = []

def generate():
    del printout[:]
    for _ in range(var1.get()):   
        C = random.randrange(6)

        if C == 0:
            printout.append(random.choice(Prefix))
        elif 1 <= C <= 2:
            printout.append(random.choice(Prefix)+random.choice(Suffix))
        elif 3 <= C <= 5:
            printout.append(random.choice(Prefix)+" "+random.choice(Prefix)+random.choice(Suffix))
    printout2 = "\n".join(printout)
    var.set(printout2)
    print(printout)

root = tk.Tk()
root.title("Simple GUI")
root.geometry("200x430")

var = tk.StringVar()

app = tk.Frame(root)
app.grid()

list1 = [1, 5, 10, 25]
var1 = tk.IntVar(app)
var1.set(1)
drop = tk.OptionMenu(root,var1,*list1)
drop.grid(row=0, column=1, sticky="n")

label = tk.Label(app, text = "How many results:")
label.grid(row=0, column=0)

button1 = tk.Button(app, text = "Generate!", command=generate)
button1.grid(row=2)

label2= tk.Label(app, textvariable=var)
label2.grid(row=3, columnspan=2)

with open('barsoom prefix.txt') as f:
    Prefix = [line.rstrip('\n') for line in f]
with open('barsoom suffix.txt') as r:
    Suffix = [line.rstrip('\n') for line in r]

root.mainloop()