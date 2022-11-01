import tkinter as tk
from sort_tam import SortTAM

def display_sort_tam():
    given_tam = tam_entry.get()
    st = SortTAM(given_tam)
    st.sort_tam()
    given_label["text"] = f"Given String: {given_tam}"
    sorted_label["text"] = f"Sorted String: {''.join(st.tamuk)}"

window = tk.Tk()
tam_label = tk.Label(text="Enter String of T's, A's, and M's")
tam_entry = tk.Entry()
enter_button = tk.Button(text="Submit", command=display_sort_tam)
given_label = tk.Label(text="Given String:")
sorted_label = tk.Label(text="Sorted String:")
tam_label.pack()
tam_entry.pack()
enter_button.pack()
given_label.pack()
sorted_label.pack()
window.mainloop()