import tkinter as tk
import random

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Score tracking
user_score = 0
computer_score = 0

def play(choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)
    
    result_label.config(text=f"You chose: {choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def determine_winner(user, computer):
    global user_score, computer_score
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your choice!")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x400")

# Labels
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Score - You: {user_score} | Computer: {computer_score}", font=("Arial", 12))
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12), command=lambda: play("Rock"))
paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12), command=lambda: play("Paper"))
scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12), command=lambda: play("Scissors"))

rock_button.grid(row=0, column=0, padx=10, pady=5)
paper_button.grid(row=0, column=1, padx=10, pady=5)
scissors_button.grid(row=0, column=2, padx=10, pady=5)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_game)
reset_button.pack(pady=10)

# Run the application
root.mainloop()
