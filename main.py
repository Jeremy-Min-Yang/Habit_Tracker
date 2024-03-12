import tkinter as tk
from tkinter import messagebox

class HabitTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Habit Tracker")
        self.habits = {}
        self.create_days()

        # Create widgets
        self.label = tk.Label(root, text="Enter a new habit:")
        self.entry = tk.Entry(root)
        self.add_button = tk.Button(root, text="Add Habit", command=self.add_habit)
        self.listbox = tk.Listbox(root)
        self.delete_button = tk.Button(root, text="Delete Habit", command=self.delete_habit)

        # Pack widgets
        self.label.pack()
        self.entry.pack()
        self.add_button.pack()
        self.listbox.pack()
        self.delete_button.pack()

    def create_days(self):
        for day in range(1, 366):
            self.habits[day] = []

    def add_habit(self):
        habit = self.entry.get()
        if habit:
            selected_day = self.listbox.curselection()
            if selected_day:
                day = selected_day[0] + 1
                self.habits[day].append(habit)
                self.listbox.delete(selected_day)
                self.listbox.insert(selected_day, f"Day {day}: {', '.join(self.habits[day])}")
            else:
                messagebox.showwarning("Warning", "Please select a day.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a habit.")

    def delete_habit(self):
        selected_day = self.listbox.curselection()
        if selected_day:
            day = selected_day[0] + 1
            self.listbox.delete(selected_day)
            self.habits[day] = []
        else:
            messagebox.showwarning("Warning", "Please select a day to delete habits.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HabitTracker(root)
    root.mainloop()
