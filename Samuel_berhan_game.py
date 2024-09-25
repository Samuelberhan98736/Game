import tkinter as tk
from tkinter import messagebox
import random
import math

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class CircularLinkedList:
    def  __init__(self):
        self.head = None
        self. tail = None
        
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
            self.tail = new_node
        else:                        
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
    
    def eliminate_random(self, steps):
        if self.head and self.head.next != self.head:
            eliminated_node = self.head
            prev_node = None
            random_index = random.randint(1, steps)# Generates a random index to eliminate
            for _ in range(random_index):
                prev_node = eliminated_node
                eliminated_node = eliminated_node.next
            prev_node.next = eliminated_node
            if eliminated_node == self.head:
                self.head = self.head.next
                return eliminated_node.value
            return None
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
            if current == self.head:
                break
            return count        
def start_game():
    global cll, n, k
    try:
        n = int(entry_n.get())
        k = int(entry_k.get())
        cll = CircularLinkedList()
        for i in range(1, n + 1):
            cll.append(i)
        create_number_squares()
        update_display()
        eliminate_button.config(state=tk.NORMAL)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers for n and k.")

def eliminate_number():
    global cll, n
    try:
        k = int(entry_k.get())
        eliminated_value = cll.eliminate_random(k)
        if eliminated_value is not None:
            messagebox.showinfo("Eliminated", f"Number {eliminated_value} has been eliminated.")
            update_display()
        else:
            messagebox.showinfo("Winner", f"The last remaining person is number {cll.head.value}")
            eliminate_button.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for k.")

def create_number_squares():
    global number_labels
    number_labels = []
    center_x, center_y = canvas_width // 2, canvas_height // 2
    radius = min(canvas_width, canvas_height) // 3
    angle_step = 360 / n
    for i in range(1, n + 1):
        angle = math.radians(i * angle_step)
        x = center_x + int(radius * math.cos(angle))
        y = center_y - int(radius * math.sin(angle))  # Negative sin to start from the top
        label = tk.Label(canvas, text=str(i), width=2, height=1, relief="solid", borderwidth=1)
        label.place(x=x, y=y)
        number_labels.append(label)

def update_display():
    global cll, number_labels
    current = cll.head
    if current:
        for i in range(n):
            if current.value is not None:
                number_labels[i].config(text=str(current.value))
            else:
                number_labels[i].config(text="")
            current = current.next

# Create the main window
root = tk.Tk()
root.title("One Potato Two Potato Game")

# Create the input fields
label_n = tk.Label(root, text="Number of people (n):")
label_n.pack()
entry_n = tk.Entry(root)
entry_n.pack()

label_k = tk.Label(root, text="Number of steps (k):")
label_k.pack()
entry_k = tk.Entry(root)
entry_k.pack()

# Create the start button
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

# Create the eliminate button
eliminate_button = tk.Button(root, text="Eliminate", command=eliminate_number, state=tk.DISABLED)
eliminate_button.pack()

# Create canvas for displaying number squares
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Run the main loop
root.mainloop()

                