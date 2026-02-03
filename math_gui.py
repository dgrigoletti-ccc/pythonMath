import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import math_menu as mm

def show_result(text_widget, text):
    text_widget.config(state='normal')
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, text)
    text_widget.config(state='disabled')

def run_fibonacci(entry, out):
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input error", "Enter a positive integer for terms.")
        return
    res = mm.get_fibonacci(n)
    show_result(out, res)

def run_factorial(entry, out):
    try:
        n = int(entry.get())
        if n < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input error", "Enter a non-negative integer.")
        return
    res = mm.get_factorial(n)
    show_result(out, res)

def run_multiplication(entry, out):
    try:
        n = int(entry.get())
    except ValueError:
        messagebox.showerror("Input error", "Enter an integer.")
        return
    res = mm.get_multiplication_table(n)
    show_result(out, res)

def run_exponentiation(base_entry, exp_entry, out):
    try:
        base = float(base_entry.get())
        exp = int(exp_entry.get())
        if exp < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input error", "Enter valid base and positive integer exponent.")
        return
    res = mm.get_exponentiation_table(base, exp)
    show_result(out, res)

def run_trigonometry(entry, out):
    try:
        angle = float(entry.get())
    except ValueError:
        messagebox.showerror("Input error", "Enter a valid angle.")
        return
    res = mm.get_trigonometry(angle)
    show_result(out, res)

def run_descriptive(entry, out):
    raw = entry.get().strip()
    if not raw:
        messagebox.showerror("Input error", "Enter comma-separated numbers (at least 1).")
        return
    try:
        values = [float(x) for x in raw.split(',') if x.strip() != ""]
        if len(values) == 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input error", "Could not parse numbers. Use comma-separated floats.")
        return
    res = mm.get_descriptive_stats_from_values(values)
    show_result(out, res)

def create_tab(parent, label, widgets):
    frame = ttk.Frame(parent)
    for w in widgets:
        w.pack(padx=6, pady=6, anchor='w')
    return frame

def main():
    root = tk.Tk()
    root.title("Python Math Tools")

    nb = ttk.Notebook(root)
    nb.pack(fill='both', expand=True, padx=8, pady=8)

    # Fibonacci tab
    fib_frame = ttk.Frame(nb)
    ttk.Label(fib_frame, text="Number of terms:").pack(anchor='w', padx=6, pady=(6,0))
    fib_entry = ttk.Entry(fib_frame, width=20)
    fib_entry.pack(padx=6, pady=6, anchor='w')
    fib_out = scrolledtext.ScrolledText(fib_frame, width=40, height=8, state='disabled')
    ttk.Button(fib_frame, text="Run", command=lambda: run_fibonacci(fib_entry, fib_out)).pack(padx=6, pady=6, anchor='w')
    fib_out.pack(padx=6, pady=6)
    nb.add(fib_frame, text='Fibonacci')

    # Factorial tab
    fact_frame = ttk.Frame(nb)
    ttk.Label(fact_frame, text="Number:").pack(anchor='w', padx=6, pady=(6,0))
    fact_entry = ttk.Entry(fact_frame, width=20)
    fact_entry.pack(padx=6, pady=6, anchor='w')
    fact_out = scrolledtext.ScrolledText(fact_frame, width=40, height=8, state='disabled')
    ttk.Button(fact_frame, text="Run", command=lambda: run_factorial(fact_entry, fact_out)).pack(padx=6, pady=6, anchor='w')
    fact_out.pack(padx=6, pady=6)
    nb.add(fact_frame, text='Factorial')

    # Multiplication tab
    mult_frame = ttk.Frame(nb)
    ttk.Label(mult_frame, text="Number:").pack(anchor='w', padx=6, pady=(6,0))
    mult_entry = ttk.Entry(mult_frame, width=20)
    mult_entry.pack(padx=6, pady=6, anchor='w')
    mult_out = scrolledtext.ScrolledText(mult_frame, width=40, height=8, state='disabled')
    ttk.Button(mult_frame, text="Run", command=lambda: run_multiplication(mult_entry, mult_out)).pack(padx=6, pady=6, anchor='w')
    mult_out.pack(padx=6, pady=6)
    nb.add(mult_frame, text='Multiplication')

    # Exponentiation tab
    exp_frame = ttk.Frame(nb)
    ttk.Label(exp_frame, text="Base:").pack(anchor='w', padx=6, pady=(6,0))
    base_entry = ttk.Entry(exp_frame, width=20)
    base_entry.pack(padx=6, pady=6, anchor='w')
    ttk.Label(exp_frame, text="Max Exponent:").pack(anchor='w', padx=6, pady=(6,0))
    exp_entry = ttk.Entry(exp_frame, width=20)
    exp_entry.pack(padx=6, pady=6, anchor='w')
    exp_out = scrolledtext.ScrolledText(exp_frame, width=40, height=8, state='disabled')
    ttk.Button(exp_frame, text="Run", command=lambda: run_exponentiation(base_entry, exp_entry, exp_out)).pack(padx=6, pady=6, anchor='w')
    exp_out.pack(padx=6, pady=6)
    nb.add(exp_frame, text='Exponentiation')

    # Trigonometry tab
    trig_frame = ttk.Frame(nb)
    ttk.Label(trig_frame, text="Angle (degrees):").pack(anchor='w', padx=6, pady=(6,0))
    trig_entry = ttk.Entry(trig_frame, width=20)
    trig_entry.pack(padx=6, pady=6, anchor='w')
    trig_out = scrolledtext.ScrolledText(trig_frame, width=40, height=8, state='disabled')
    ttk.Button(trig_frame, text="Run", command=lambda: run_trigonometry(trig_entry, trig_out)).pack(padx=6, pady=6, anchor='w')
    trig_out.pack(padx=6, pady=6)
    nb.add(trig_frame, text='Trigonometry')

    # Descriptive Stats tab
    stats_frame = ttk.Frame(nb)
    ttk.Label(stats_frame, text="Enter comma-separated numbers (e.g. 1, 2, 3.5):").pack(anchor='w', padx=6, pady=(6,0))
    stats_entry = ttk.Entry(stats_frame, width=50)
    stats_entry.pack(padx=6, pady=6, anchor='w')
    stats_out = scrolledtext.ScrolledText(stats_frame, width=40, height=8, state='disabled')
    ttk.Button(stats_frame, text="Run", command=lambda: run_descriptive(stats_entry, stats_out)).pack(padx=6, pady=6, anchor='w')
    stats_out.pack(padx=6, pady=6)
    nb.add(stats_frame, text='Descriptive Stats')

    root.mainloop()

if __name__ == "__main__":
    main()
