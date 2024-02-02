import tkinter as tk
from screeninfo import get_monitors
import numpy as np

def configure_window(width, height):
    # Create the main window
    window = tk.Tk()
    window.title("Guessing Game")

    # Set the window size
    window.geometry(f"{width}x{height}")

    # Center the window on the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

    return window
    

def guess_game(correct_number, entry, label, attempts_label):
    input_num = entry.get()
    attempts = int(attempts_label.cget("text"))

    attempts += 1

    if input_num == str(correct_number):
        answer = f"Correct! You guessed the number in {attempts} attempts."
    else:
        answer = f"Wrong answer. Try again."

    entry.delete(0, tk.END)
    label.config(text=answer)
    attempts_label.config(text=str(attempts))


def main():
    # Generate a random number
    correct_number = np.random.randint(0, 9)

    # Create the main window
    main_window = configure_window(400, 300)

    # Create an Entry widget for user input
    entry = tk.Entry(main_window, width=30)

    # Create a button widget
    button = tk.Button(main_window, text="Enter number", command=lambda: guess_game(correct_number, entry, label, attempts_label))

    # Create a label widget
    label = tk.Label(main_window, text="Try guessing a number!")

    # Create a label for attempts
    attempts_label = tk.Label(main_window, text="0")

    # Pack the widgets into the window
    label.pack(pady=10)
    entry.pack(pady=10)
    button.pack(pady=10)
    attempts_label.pack(pady=10)

    # Start the main event loop
    main_window.mainloop()

if __name__ == "__main__":
    main()

