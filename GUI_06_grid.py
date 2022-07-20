# Code by @AmirMotefaker

# GUI - Grid

# # Solution 1
# import tkinter as tk

# window = tk.Tk()

# label_input_name = tk.Label(
#     window,
#     text = 'First Name: ',
# )
# entry_name = tk.Entry(
#     window,
# )

# label_input_name.pack()
# entry_name.pack()

# window.mainloop()



# Solution 2 - Grid
import tkinter as tk

window = tk.Tk()

label_input_name = tk.Label(
    window,
    text = 'First Name: ',
)
entry_name = tk.Entry(
    window,
)

label_input_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1)
# label_input_name.pack()
# entry_name.pack()

window.mainloop()
