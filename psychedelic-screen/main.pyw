import tkinter as tk
import random
import keyboard
import threading

def random_color():
    """Generates a random color in HEX format."""
    return "#" + "".join(random.choices("0123456789ABCDEF", k=6))

def update_color():
    """Updates the color with an instant transition."""
    global current_color

    current_color = random_color()
    canvas.config(bg=current_color)
    root.after(60, update_color)  # Reduced update speed

def monitor_space_key():
    """Checks the Spacebar keypress globally and closes the application."""
    while True:
        if keyboard.is_pressed("space"):
            root.destroy()
            break

# Initializing the window
root = tk.Tk()
root.title("Random Color Transition")

# Убираем границы окна
root.overrideredirect(True)

# Задаем размеры окна window_size = 400
window_size = 4000
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_size) // 2
y_position = (screen_height - window_size) // 2
root.geometry(f"{window_size}x{window_size}+{x_position}+{y_position}")

# Removing the window borders
canvas = tk.Canvas(root, width=window_size, height=window_size, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Starting a stream to monitor the Space bar
space_key_thread = threading.Thread(target=monitor_space_key, daemon=True)
space_key_thread.start()

# Initial color
current_color = random_color()

# Starting the animation
update_color()

# Starting the main application cycle
root.mainloop()
