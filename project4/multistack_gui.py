import tkinter as tk
from multistack import MultiStack

def display_push():
    given_elem = int(elem_entry.get())
    given_snum = int(snum_entry.get())
    ms.push(given_snum, given_elem)
    oper_label["text"] = f"Operation: pushed {given_elem} into stack {given_snum}"
    arr_label["text"] = f"Resulting array: {ms.arr}"
    stk0_label["text"] = f"Stack 0: {ms.arr[ms.bots[0]:ms.tops[0]+1]}"
    stk1_label["text"] = f"Stack 1: {ms.arr[ms.bots[1]:ms.tops[1]+1]}"
    stk2_label["text"] = f"Stack 2: {ms.arr[ms.bots[2]:ms.tops[2]+1]}"
    tops_label["text"] = f"Tops: {ms.tops}"
    bots_label["text"] = f"Bots: {ms.bots}"


def display_pop():
    given_snum = int(snum_entry.get())
    ms.pop(given_snum)
    oper_label["text"] = f"Operation: popped from stack {given_snum}"
    stk0_label["text"] = f"Stack 0: {ms.arr[ms.bots[0]:ms.tops[0]+1]}"
    stk1_label["text"] = f"Stack 1: {ms.arr[ms.bots[1]:ms.tops[1]+1]}"
    stk2_label["text"] = f"Stack 2: {ms.arr[ms.bots[2]:ms.tops[2]+1]}"
    tops_label["text"] = f"Tops: {ms.tops}"

def display_top():
    given_snum = int(snum_entry.get())
    top = ms.top(given_snum)
    oper_label["text"] = f"Operation: top element from stack {given_snum} is {top}"

ms = MultiStack()
window = tk.Tk()
elem_label = tk.Label(text="Enter element to be pushed")
elem_entry = tk.Entry()
snum_label = tk.Label(text="Enter stack number to be operated on")
snum_entry = tk.Entry()
push_button = tk.Button(text="Push", command=display_push)
pop_button = tk.Button(text="Pop", command=display_pop)
top_button = tk.Button(text="Top", command=display_top)
oper_label = tk.Label(text="Operation:")
arr_label = tk.Label(text=f"Resulting array: {ms.arr}")
stk0_label = tk.Label(text=f"Stack 0: {ms.arr[ms.bots[0]:ms.tops[0]+1]}")
stk1_label = tk.Label(text=f"Stack 1: {ms.arr[ms.bots[1]:ms.tops[1]+1]}")
stk2_label = tk.Label(text=f"Stack 2: {ms.arr[ms.bots[2]:ms.tops[2]+1]}")
tops_label = tk.Label(text=f"Tops: {ms.tops}")
bots_label = tk.Label(text=f"Bots: {ms.bots}")

elem_label.pack()
elem_entry.pack()
snum_label.pack()
snum_entry.pack()
push_button.pack()
pop_button.pack()
top_button.pack()
oper_label.pack()
arr_label.pack()
stk0_label.pack()
stk1_label.pack()
stk2_label.pack()
tops_label.pack()
bots_label.pack()

window.mainloop()