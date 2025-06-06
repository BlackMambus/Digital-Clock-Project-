import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
    clock_label.config(text=current_time)     # Update the label with the current time
    clock_label.after(1000, update_clock)      # Schedule the update_clock function to be called after 1000 ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
clock_label = tk.Label(root, font=("Helvetica", 48), fg="black")
clock_label.pack(pady=20)

# Start the clock
update_clock()

# Run the application
root.mainloop()
