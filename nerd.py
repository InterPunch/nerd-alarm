import tkinter as tk

def show_warning():
    # Create the warning window
    warning_window = tk.Toplevel(root)
    warning_window.title("Warning")

    # Configure window size and position
    warning_window.geometry("300x150+400+200")

    # Set the background color to red
    warning_window.configure(bg="red")

    # Add a label with the warning text
    warning_label = tk.Label(warning_window, text="Nerd Detected!", font=("Helvetica", 16), fg="white", bg="red")
    warning_label.pack(pady=20)

    # Add a button to close the warning window
    close_button = tk.Button(warning_window, text="OK", command=warning_window.destroy)
    close_button.pack(pady=10)

# Create the main application window
root = tk.Tk()
root.title("Main Window")

# Add a button to trigger the warning window
warning_button = tk.Button(root, text="Show Warning", command=show_warning)
warning_button.pack(pady=50)

# Start the Tkinter event loop
root.mainloop()
