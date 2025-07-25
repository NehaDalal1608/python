import tkinter as tk
from tkinter import ttk, messagebox
import random

# General knowledge questions, options, and answers
questions_data = [
    {"question": "What is the capital of India?", "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"], "answer": "New Delhi"},
    {"question": "Who is known as the 'Father of the Nation' in India?", "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Subhas Chandra Bose", "B.R. Ambedkar"], "answer": "Mahatma Gandhi"},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
    {"question": "Which festival is known as the Festival of Lights in India?", "options": ["Holi", "Eid", "Diwali", "Christmas"], "answer": "Diwali"},
    {"question": "Which river is known as the 'Holy River' in India?", "options": ["Yamuna", "Ganga", "Godavari", "Brahmaputra"], "answer": "Ganga"},
    {"question": "Which animal is known as the 'Ship of the Desert'?", "options": ["Camel", "Elephant", "Horse", "Dog"], "answer": "Camel"},
    {"question": "Who wrote the Indian national anthem?", "options": ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Mahatma Gandhi"], "answer": "Rabindranath Tagore"},
    {"question": "What is the smallest continent by land area?", "options": ["Asia", "Africa", "Australia", "Europe"], "answer": "Australia"},
    {"question": "Who invented the light bulb?", "options": ["Thomas Edison", "Albert Einstein", "Nikola Tesla", "Isaac Newton"], "answer": "Thomas Edison"},
    {"question": "Which organ purifies our blood?", "options": ["Liver", "Kidney", "Heart", "Lungs"], "answer": "Kidney"}
]

# Shuffle questions
random.shuffle(questions_data)

class Quiz:
    def __init__(self, root, user_name):
        self.root = root
        self.user_name = user_name
        self.root.title("General Knowledge Quiz")
        self.root.geometry("600x600")
        self.root.configure(bg="#333333")
        
        # Initialize question index and score
        self.question_index = 0
        self.score = 0
        
        # Store user answers
        self.user_answers = [None] * len(questions_data)

        # Create a frame for the question and options
        self.question_frame = tk.Frame(root, bg="#444444", pady=10)
        self.question_frame.pack(pady=20, fill="x")

        # Display the question and options
        self.display_question()
        self.display_options()

        # Progress bar
        self.progress_label = tk.Label(root, text=f"Welcome, {self.user_name}! Progress:", bg="#333333", fg="white", font=("Arial", 12))
        self.progress_label.pack(pady=10)
        self.progress = ttk.Progressbar(root, length=400, mode="determinate", maximum=len(questions_data))
        self.progress.pack(pady=5)

        # Frame for buttons
        self.button_frame = tk.Frame(root, bg="#333333")
        self.button_frame.pack(side=tk.BOTTOM, pady=20)

        # Button for submitting answer
        self.submit_button = tk.Button(self.button_frame, text="Submit", command=self.check_answer, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=15, pady=10, relief="flat")
        self.submit_button.pack(side=tk.LEFT, padx=20, ipadx=20)

        # Button for going back to the previous question
        self.back_button = tk.Button(self.button_frame, text="Back", command=self.go_back, bg="#f44336", fg="white", font=("Arial", 12, "bold"), padx=15, pady=10, relief="flat")
        self.back_button.pack(side=tk.LEFT, padx=20, ipadx=20)

    def display_question(self):
        for widget in self.question_frame.winfo_children():
            widget.destroy()

        question_text = questions_data[self.question_index]["question"]
        self.question_label = tk.Label(self.question_frame, text=question_text, font=("Arial", 16, "bold"), wraplength=400, bg="#444444", fg="white")
        self.question_label.pack(pady=20)

    def display_options(self):
        for widget in self.question_frame.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()

        self.selected_option = tk.StringVar()
        self.selected_option.set(self.user_answers[self.question_index])

        for option in questions_data[self.question_index]["options"]:
            option_button = tk.Radiobutton(self.question_frame, text=option, variable=self.selected_option, value=option, font=("Arial", 12), bg="#444444", fg="white", anchor="w", selectcolor="#666666")
            option_button.pack(anchor="w", padx=20, pady=5)

    def check_answer(self):
        selected = self.selected_option.get()
        self.user_answers[self.question_index] = selected
        if selected == questions_data[self.question_index]["answer"]:
            self.score += 1

        self.question_index += 1
        self.progress["value"] = self.question_index

        if self.question_index < len(questions_data):
            self.display_question()
            self.display_options()
        else:
            self.show_result()

    def go_back(self):
        if self.question_index > 0:
            self.question_index -= 1
            self.display_question()
            self.display_options()

    def show_result(self):
        correct_answers = self.score
        wrong_answers = len(questions_data) - self.score

        # Get incorrect answers
        incorrect_answers = [
            f"Q: {questions_data[i]['question']}\nYour Answer: {self.user_answers[i] or 'No Answer'}\nCorrect Answer: {questions_data[i]['answer']}"
            for i in range(len(questions_data)) if self.user_answers[i] != questions_data[i]["answer"]
        ]

        # Save the user's score to a file
        with open("quiz_results.txt", "a") as file:
            file.write(f"Name: {self.user_name}, Correct: {correct_answers}, Wrong: {wrong_answers}\n")

        # Show a popup message with the result and incorrect answers
        messagebox.showinfo(
            "Quiz Results",
            f"Congratulations, {self.user_name}!\n"
            f"Correct Answers: {correct_answers}\n"
            f"Wrong Answers: {wrong_answers}\n\n"
            f"Incorrect Answers:\n{chr(10).join(incorrect_answers)}"
        )

        # Close the quiz window
        self.root.destroy()

def start_quiz(root, name_entry):
    user_name = name_entry.get().strip()
    if user_name:
        for widget in root.winfo_children():
            widget.destroy()
        Quiz(root, user_name)
    else:
        messagebox.showwarning("Input Error", "Please enter your name to start the quiz.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quiz App")
    root.geometry("400x300")
    root.configure(bg="#333333")

    # Welcome screen
    welcome_label = tk.Label(root, text="Welcome to the Quiz!", font=("Arial", 16, "bold"), bg="#333333", fg="white")
    welcome_label.pack(pady=30)

    name_label = tk.Label(root, text="Enter your name:", font=("Arial", 12), bg="#333333", fg="white")
    name_label.pack(pady=10)

    name_entry = tk.Entry(root, font=("Arial", 12), width=30)
    name_entry.pack(pady=10)

    start_button = tk.Button(root, text="Start Quiz", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=lambda: start_quiz(root, name_entry))
    start_button.pack(pady=20)

    root.mainloop()
