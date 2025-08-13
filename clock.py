import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Format: Hours:Minutes:Seconds
    label.config(text=current_time)
    root.after(1000, update_time)  # call this function again after 1000 ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Clock label
label = tk.Label(root, font=("Arial", 50), fg="white", bg="black")
label.pack(padx=20, pady=20)

# Start the clock update
update_time()

# Run the application
root.mainloop()
