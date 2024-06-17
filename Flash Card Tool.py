import tkinter as tk
from tkinter import messagebox


class FlashCardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Knowledge Cards: Flash Card Tool")
        self.root.geometry("420x420")

        self.flashcards = []
        self.current_card_index = 0

        self.front_text = tk.StringVar()
        self.back_text = tk.StringVar()

        self.front_text.trace("w", self.adjust_entry_size)
        self.back_text.trace("w", self.adjust_entry_size)

        self.label_font = ("Helvetica", 14)
        self.entry_font = ("Helvetica", 14)
        self.button_font = ("Helvetica", 12)

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Front:", font=self.label_font).pack(pady=5)
        self.front_entry = tk.Entry(self.root, textvariable=self.front_text, font=self.entry_font, justify='center')
        self.front_entry.pack(pady=5)

        tk.Label(self.root, text="Back:", font=self.label_font).pack(pady=5)
        self.back_entry = tk.Entry(self.root, textvariable=self.back_text, font=self.entry_font, justify='center')
        self.back_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Card", command=self.add_card, font=self.button_font)
        self.add_button.pack(pady=5)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        self.show_button = tk.Button(self.buttons_frame, text="Show Card", command=self.show_card, font=self.button_font)
        self.show_button.pack(side=tk.LEFT, padx=5)

        self.next_button = tk.Button(self.buttons_frame, text="Next Card", command=self.next_card, font=self.button_font)
        self.next_button.pack(side=tk.LEFT, padx=5)

        self.prev_button = tk.Button(self.buttons_frame, text="Previous Card", command=self.prev_card, font=self.button_font)
        self.prev_button.pack(side=tk.LEFT, padx=5)

        self.known_button = tk.Button(self.buttons_frame, text="Known", command=self.mark_known, font=self.button_font)
        self.known_button.pack(side=tk.LEFT, padx=5)

        # Display Area
        self.card_display = tk.Label(self.root, text="", font=("Helvetica", 26))
        self.card_display.pack(pady=20)

        self.flip_button = tk.Button(self.root, text="Flip Card", command=self.flip_card, font=self.button_font)
        self.flip_button.pack(side=tk.BOTTOM, pady=10)

    def adjust_entry_size(self, *args):
        front_length = len(self.front_text.get())
        back_length = len(self.back_text.get())
        self.front_entry.config(width=max(20, front_length))
        self.back_entry.config(width=max(20, back_length))

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

    def mark_known(self):
        if self.flashcards:
            del self.flashcards[self.current_card_index]
            if self.current_card_index >= len(self.flashcards):
                self.current_card_index = 0
            self.show_card()
        else:
            messagebox.showwarning("No Cards", "There are no flashcards to mark as known.")

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

