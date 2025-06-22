import random
import tkinter as tk


def main():
    def get_winner(user_choice, computer_choice):
        if computer_choice == user_choice:
            return "It's a draw!"

        elif (
                (user == "🪨 Rock" and computer == "✂️ Scissors") or
                (user == "📃 Paper" and computer == "🪨 Rock") or
                (user == "✂️ Scissors" and computer == "📃 Paper")
        ):

            return "You win!"
        else:
            return "Computer wins!"

    def make_choice(user_choice):
        computer_choice = random.choice(["✂️ Scissors", "🪨 Rock", "📃 Paper"])
        computer_label.config(text=f"Computer chose: {computer_choice}")
        result = get_winner(user_choice, computer_choice)
        result_label.config(text=result)
        return computer_choice

    window = tk.Tk()
    window.title("Rock Paper Scissors")
    window.geometry("400x200")

    computer_label = tk.Label(window, text="Computer chose: ???", font=("Arial", 12))
    computer_label.pack(pady=10)

    result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
    result_label.pack(pady=10)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=20)

    rock_button = tk.Button(button_frame, text="🪨 Rock", width=10, command=lambda: make_choice("🪨 Rock"))
    rock_button.grid(row=0, column=0, padx=5)

    paper_button = tk.Button(button_frame, text="📃 Paper", width=10, command=lambda: make_choice("📃 Paper"))
    paper_button.grid(row=0, column=1, padx=5)

    scissors_button = tk.Button(button_frame, text="✂️ Scissors", width=10, command=lambda: make_choice("✂️ Scissors"))
    scissors_button.grid(row=0, column=2, padx=5)

    window.mainloop()


if __name__ == "__main__":
    main()
