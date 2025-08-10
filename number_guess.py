import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Number Guess")
        master.geometry("520x520")
        master.resizable(False, False)

        # Gradient background using Canvas
        self.bg_canvas = tk.Canvas(master, width=520, height=520, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        for i in range(0, 520, 2):
            color = f'#{34+i//6:02x}{40+i//8:02x}{49+i//10:02x}'
            self.bg_canvas.create_rectangle(0, i, 520, i+2, outline="", fill=color)

        # Place widgets on canvas
        self.frame = tk.Frame(master, bg="#222831")
        self.bg_canvas.create_window(260, 260, window=self.frame)

        self.guesses = 0
        self.num = 0

        self.title_label = tk.Label(self.frame, text="🔢 Number Guess 🔢", font=("Arial Rounded MT Bold", 20, "bold"), fg="#FFD369", bg="#222831")
        self.title_label.pack(pady=(30, 12))

        self.difficulty_label = tk.Label(self.frame, text="Choose Difficulty:", font=("Arial", 13), fg="#EEEEEE", bg="#222831")
        self.difficulty_label.pack()

        self.difficulty_var = tk.StringVar(value="Easy")
        self.easy_radio = tk.Radiobutton(self.frame, text="🟢 Easy (9 guesses)", variable=self.difficulty_var, value="Easy", font=("Arial", 12), fg="#00ADB5", bg="#222831", selectcolor="#393E46", activebackground="#393E46")
        self.hard_radio = tk.Radiobutton(self.frame, text="🔴 Hard (5 guesses)", variable=self.difficulty_var, value="Hard", font=("Arial", 12), fg="#FF2E63", bg="#222831", selectcolor="#393E46", activebackground="#393E46")
        self.easy_radio.pack()
        self.hard_radio.pack()

        self.start_button = tk.Button(self.frame, text="▶ Start Game", command=self.start_game, font=("Arial Rounded MT Bold", 13), bg="#FFD369", fg="#222831", bd=0, relief="ridge", padx=12, pady=6, activebackground="#FFDE7A")
        self.start_button.pack(pady=12)

        self.info_label = tk.Label(self.frame, text="", font=("Arial", 12), fg="#EEEEEE", bg="#222831")
        self.info_label.pack(pady=5)

        self.guess_entry = tk.Entry(self.frame, font=("Arial", 13), justify="center", state="disabled", bg="#393E46", fg="#FFD369", relief="flat", highlightthickness=2, highlightbackground="#FFD369")
        self.guess_entry.pack(pady=7, ipadx=10, ipady=4)

        self.submit_button = tk.Button(self.frame, text="✅ Submit Guess", command=self.check_guess, font=("Arial Rounded MT Bold", 13), bg="#00ADB5", fg="#222831", bd=0, relief="ridge", padx=10, pady=6, activebackground="#00CFCF", state="disabled")
        self.submit_button.pack(pady=6)

        self.feedback_label = tk.Label(self.frame, text="", font=("Arial Rounded MT Bold", 14), fg="#FFD369", bg="#222831")
        self.feedback_label.pack(pady=12)

        self.reset_button = tk.Button(self.frame, text="🔄 Play Again", command=self.reset_game, font=("Arial Rounded MT Bold", 13), bg="#393E46", fg="#FFD369", bd=0, relief="ridge", padx=10, pady=6, activebackground="#FFD369", state="disabled")
        self.reset_button.pack(pady=6)

        self.footer_label = tk.Label(self.frame, text="stasnia 2022", font=("Arial", 10), fg="#EEEEEE", bg="#222831")
        self.footer_label.pack(side="bottom", pady=(18, 0))

    def start_game(self):
        difficulty = self.difficulty_var.get().upper()
        self.guesses = 9 if difficulty == "EASY" else 5
        self.num = random.randrange(2, 49)
        self.info_label.config(text=f"I'm thinking of a number between 1 and 50.\nYou have {self.guesses} guesses.")
        self.guess_entry.config(state="normal")
        self.submit_button.config(state="normal")
        self.start_button.config(state="disabled")
        self.feedback_label.config(text="")
        self.reset_button.config(state="disabled")
        self.guess_entry.delete(0, tk.END)
        self.animate_label(self.info_label, "#FFD369")

    def check_guess(self):
        guess_text = self.guess_entry.get()
        if not guess_text.isdigit():
            self.feedback_label.config(text="⚠️ Please enter a valid number.", fg="#FF2E63")
            self.animate_label(self.feedback_label, "#FF2E63")
            return
        guess = int(guess_text)
        self.guesses -= 1

        if guess > self.num:
            self.feedback_label.config(text="⬆️ Too high!", fg="#FFD369")
            self.animate_label(self.feedback_label, "#FFD369")
        elif guess < self.num:
            self.feedback_label.config(text="⬇️ Too low!", fg="#FFD369")
            self.animate_label(self.feedback_label, "#FFD369")
        else:
            self.feedback_label.config(text="🎉 You guessed correctly!", fg="#00FF00")
            self.animate_label(self.feedback_label, "#00FF00")
            self.end_game(True)
            return

        if self.guesses == 0:
            self.feedback_label.config(text=f"😢 Sorry, you did not guess correctly.\nThe number was {self.num}.", fg="#FF2E63")
            self.animate_label(self.feedback_label, "#FF2E63")
            self.end_game(False)
        else:
            self.info_label.config(text=f"Guesses left: {self.guesses}")
            self.animate_label(self.info_label, "#FFD369")

        self.guess_entry.delete(0, tk.END)

    def end_game(self, won):
        self.guess_entry.config(state="disabled")
        self.submit_button.config(state="disabled")
        self.reset_button.config(state="normal")
        if won:
            messagebox.showinfo("🎉 Congratulations!", "You guessed the number!")
        else:
            messagebox.showinfo("Game Over", f"You ran out of guesses.\nThe number was {self.num}.")

    def reset_game(self):
        self.start_button.config(state="normal")
        self.info_label.config(text="")
        self.feedback_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state="disabled")
        self.submit_button.config(state="disabled")
        self.reset_button.config(state="disabled")

    def animate_label(self, label, color):
        # Simple flash animation
        orig_color = label.cget("fg")
        def flash(count=0):
            if count % 2 == 0:
                label.config(fg=color)
            else:
                label.config(fg=orig_color)
            if count < 4:
                label.after(120, flash, count+1)
        flash()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGameGUI(root)
    root.mainloop()

