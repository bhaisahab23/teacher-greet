import tkinter as tk
import itertools
import threading
import time

colors = ["red", "green", "blue", "orange", "purple", "magenta", "cyan"]
messages = itertools.cycle([
    "🎓 Happy Teachers' Day 🎓",
    "🙏 Thank You Gurujis 🙏",
    "📚 You Inspire Us 📚",
    "🌟 Keep Shining 🌟"
])

def show_gui_greeting():
    def animate(label):
        def run():
            while True:
                msg = next(messages)
                for color in colors:
                    label.config(text=msg, fg=color)
                    time.sleep(0.3)
        threading.Thread(target=run, daemon=True).start()

    root = tk.Tk()
    root.title("Teachers' Day Tribute")
    root.geometry("500x300")
    root.configure(bg="black")

    label = tk.Label(root, text="", font=("Helvetica", 24, "bold"), bg="black")
    label.pack(expand=True)

    animate(label)
    root.mainloop()
