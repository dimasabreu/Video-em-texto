import tkinter as tk
root = tk.Tk()
root.title('Videos em texto')

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)
text_box = tk.Text(root, height=20, width=80, padx=10, pady=15, font=("Helvetiva", 16), border=10)
text_box.insert(1.0, "content")
text_box.tag_configure("center", justify="center")
text_box.tag_add("center", 1.0, "end")
text_box.grid(column=3, row=3)

root.mainloop()