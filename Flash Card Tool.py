import tkinter as tk
from tkinter import messagebox

class FlashCardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Knowledge Cards: Flash Card Tool")
        
        self.flashcards = []
        self.current_card_index = 0
        
        self.front_text = tk.StringVar()
        self.back_text = tk.StringVar()

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # Front Label
        tk.Label(self.root, text="Front:").pack(pady=5)
        self.front_entry = tk.Entry(self.root, textvariable=self.front_text)
        self.front_entry.pack(pady=5)

        # Back Label
        tk.Label(self.root, text="Back:").pack(pady=5)
        self.back_entry = tk.Entry(self.root, textvariable=self.back_text)
        self.back_entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Card", command=self.add_card)
        self.add_button.pack(pady=5)

        self.show_button = tk.Button(self.root, text="Show Card", command=self.show_card)
        self.show_button.pack(pady=5)

        self.next_button = tk.Button(self.root, text="Next Card", command=self.next_card)
        self.next_button.pack(pady=5)

        self.prev_button = tk.Button(self.root, text="Previous Card", command=self.prev_card)
        self.prev_button.pack(pady=5)

        # Display Area
        self.card_display = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.card_display.pack(pady=20)

        self.flip_button = tk.Button(self.root, text="Flip Card", command=self.flip_card)
        self.flip_button.pack(pady=5)

    def add_card(self):
        front = self.front_text.get()
        back = self.back_text.get()
        if front and back:
            self.flashcards.append((front, back))
            self.front_text.set("")
            self.back_text.set("")
            messagebox.showinfo("Success", "Flashcard added!")
        else:
            messagebox.showwarning("Input Error", "Both front and back text are required.")

    def show_card(self):
        if self.flashcards:
            front, back = self.flashcards[self.current_card_index]
            self.card_display.config(text=front)
            self.current_card_side = 'front'
        else:
            messagebox.showwarning("No Cards", "There are no flashcards to show.")

    def next_card(self):
        if self.flashcards:
            self.current_card_index = (self.current_card_index + 1) % len(self.flashcards)
            self.show_card()
        else:
            messagebox.showwarning("No Cards", "There are no flashcards to navigate.")

    def prev_card(self):
        if self.flashcards:
            self.current_card_index = (self.current_card_index - 1) % len(self.flashcards)
            self.show_card()
        else:
            messagebox.showwarning("No Cards", "There are no flashcards to navigate.")

    def flip_card(self):
        if self.flashcards:
            front, back = self.flashcards[self.current_card_index]
            if self.current_card_side == 'front':
                self.card_display.config(text=back)
                self.current_card_side = 'back'
            else:
                self.card_display.config(text=front)
                self.current_card_side = 'front'
        else:
            messagebox.showwarning("No Cards", "There are no flashcards to flip.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashCardApp(root)
    root.mainloop()
