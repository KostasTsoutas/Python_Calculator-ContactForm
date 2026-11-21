import tkinter as tk
from tkinter import messagebox
def Ok():
    resultLabel.config(text=f"Όνομα: {name.get()}\nΗληκία: {age.get()}\nEmail: {email.get()}")

def Alert():
    alert = messagebox.showinfo("Στοιχεία", f"Όνομα: {name.get()}\nΗληκία: {age.get()}\nEmail: {email.get()}")
    Ok()

def Cancel():
    name.delete(0,tk.END)
    age.delete(0,tk.END)
    email.delete(0,tk.END)
    resultLabel.config(text="")

def Close():
    root.destroy()
    
root = tk.Tk()

# Πάνω τίτλος
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Στοιχεία Χρήστη", font=("Arial", 14)).pack()

# Κεντρική φόρμα
form_frame = tk.Frame(root)
form_frame.pack(padx=20, pady=10)

tk.Label(form_frame, text="Όνομα:").grid(row=0, column=0, sticky="e")
name = tk.Entry(form_frame)
name.grid(row=0, column=1)

tk.Label(form_frame, text="Ηλικία:").grid(row=1, column=0, sticky="e")
age = tk.Entry(form_frame)
age.grid(row=1, column=1)

tk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky="e")
email = tk.Entry(form_frame)
email.grid(row=2, column=1)

# Κουμπιά κάτω
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

tk.Button(bottom_frame, text="OK", command=Alert).pack(side="left", padx=5)
tk.Button(bottom_frame, text="Ακύρωση", command=Cancel).pack(side="left", padx=5)
tk.Button(bottom_frame, text="Close", command=Close).pack(side="left", padx=5)

resultFrame = tk.Frame(root)
resultFrame.pack(pady=10)

resultLabel = tk.Label(resultFrame, bg="#2E2E2E", fg="#9F0000")
resultLabel.pack(pady=10)

root.mainloop()