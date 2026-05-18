import tkinter as tk 
from tkinter import scrolledtext


# Summarize Function
def summarize_text():
    text = input_text.get("1.0", tk.END)

    if len(text.strip()) == 0:
        return

    summary = text[:300]

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)

# Main Window
root = tk.Tk()
root.title("AI Text Summarizer")
root.geometry("700x500")
root.configure(bg="#1e1e1e")

# Title
title = tk.Label(
    root,
    text="AI Text Summarizer",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=10)

# Input Label
input_label = tk.Label(
    root,
    text="Enter Text:",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12)
)
input_label.pack()

# Input Text
input_text = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=80,
    height=10,
    font=("Arial", 12),
    bg="#2b2b2b",
    fg="white",
    insertbackground="white"
)
input_text.pack(padx=10, pady=10)

# Button
summarize_button = tk.Button(
    root,
    text="Summarize",
    command=summarize_text,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white"
)
summarize_button.pack(pady=10)

# Output Label
output_label = tk.Label(
    root,
    text="Summary:",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12)
)
output_label.pack()

# Output Text
output_text = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=80,
    height=8,
    font=("Arial", 12),
    bg="#2b2b2b",
    fg="white",
    insertbackground="white"
)
output_text.pack(padx=10, pady=10)

root.mainloop()