import tkinter as tk

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]


bg_color = "#121212"
btn_dark = "#2C2C2C"
btn_light = "#A5A5A5"
btn_orange = "#FF9F0A"
text_color = "pink"


window = tk.Tk()
window.title("Maytinh cua Duy")
window.configure(bg=bg_color)
window.resizable(False, False)

frame = tk.Frame(window, bg=bg_color, padx=10, pady=10)
frame.pack()

label = tk.Label(
    frame,
    text="0",
    font=("Segoe UI", 40),
    bg=bg_color,
    fg=text_color,
    anchor="e",
    padx=10,
    pady=20
)
label.grid(row=0, column=0, columnspan=4, sticky="we")


A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)

                clear_all()

        else:
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            label["text"] = remove_zero_decimal(float(label["text"]) * -1)
        elif value == "%":
            label["text"] = remove_zero_decimal(float(label["text"]) / 100)

    else:
        if value == ".":
            if "." not in label["text"]:
                label["text"] += "."
        else:
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value


def on_enter(e):
    e.widget["bg"] = "#3A3A3A"

def on_leave(e, color):
    e.widget["bg"] = color


for r, row in enumerate(button_values):
    for c, value in enumerate(row):
        if value in top_symbols:
            color = btn_light
            fg = "red"
        elif value in right_symbols:
            color = btn_orange
            fg = "green"
        else:
            color = btn_dark
            fg = "green"

        btn = tk.Button(
            frame,
            text=value,
            font=("Segoe UI", 18, "bold"),
            bg=color,
            fg=fg,
            width=5,
            height=2,
            bd=0,
            command=lambda v=value: button_clicked(v)
        )

        btn.grid(row=r+1, column=c, padx=5, pady=5)

        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", lambda e, col=color: on_leave(e, col))




window.update()
w = window.winfo_width()
h = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (w // 2)
y = (window.winfo_screenheight() // 2) - (h // 2)
window.geometry(f"{w}x{h}+{x}+{y}")

window.mainloop()



 
     











 









   






