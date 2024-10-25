import tkinter as tk
from tkinter import ttk

class Puzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Game")

        # Configure the main layout with a background color
        self.root.config(padx=10, pady=10, bg='#2c3e50')

        # ======================== Puzzle Board Frame ========================
        board_frame = tk.Frame(self.root, bg='#34495e', padx=5, pady=5)
        board_frame.grid(row=0, column=0, padx=10, pady=(0, 10))

        # Creat default board values
        self.tiles = []
        for i in range(9):
            # set 0 to be empty tile
            text = i if i != 0 else ''

            # set diffrent color for empty tile
            color = '#ecf0f1' if i != 0 else '#95a5a6'

            # set the board with numbers
            btn = tk.Button(
                board_frame,
                text=text,
                width=5,
                height=2,
                font=('Arial', 24, 'bold'),
                bg=color,
                fg='#2c3e50' if i != 0 else 'white',
                activebackground='#3498db'
            )
            # set location of each button
            btn.grid(row=i // 3, column=i % 3, padx=2, pady=2)
            self.tiles.append(btn)

        # ======================== Puzzle Board Controler Frame ========================
        board_control_frame = tk.Frame(self.root, bg='#34495e')
        board_control_frame.grid(row=1, column=0, pady=10, sticky='ew')

        # set label for board control frame
        board_label = tk.Label(
            board_control_frame, text="Board", bg='#34495e', fg='white', font=('Arial', 14, 'bold')
        )
        board_label.pack(fill='x', pady=5)

        # randomize buton for randome input board
        randomize_btn = tk.Button(
            board_control_frame, text="Randomize", font=('Arial', 12), bg='#2980b9', fg='white',
            activebackground='#1abc9c'
        )
        randomize_btn.pack(pady=2)

        # custom button for user input board
        custom_input_btn = tk.Button(
            board_control_frame, text="Enter Custom State", font=('Arial', 12), bg='#2980b9', fg='white',
            activebackground='#1abc9c'
        )
        custom_input_btn.pack(pady=2)

        # ======================== Puzzle Search Frame ========================
        search_frame = tk.Frame(self.root, bg='#34495e')
        search_frame.grid(row=2, column=0, pady=10, sticky='ew')

        # set label for srearch frame
        search_label = tk.Label(
            search_frame, text="Search", bg='#34495e', fg='white', font=('Arial', 14, 'bold')
        )
        search_label.pack(fill='x', pady=5)

        algorithm_label = tk.Label(
            search_frame, text="Algorithm", font=('Arial', 12), bg='#34495e', fg='white'
        )
        algorithm_label.pack(anchor='w', padx=10)

        # combobox for choose the specified algorithm
        self.algorithm_combo = ttk.Combobox(
            search_frame, font=('Arial', 12), state='readonly'
        )
        self.algorithm_combo['values'] = ["BFS", "DFS", "IDFS", "A*"]
        # Set default value
        self.algorithm_combo.current(0)  
        self.algorithm_combo.pack(fill='x', padx=10, pady=5)

        # Set ttk theme to match the dark background
        style = ttk.Style()
        style.theme_use('clam')  # Use the 'clam' theme for modern look
        style.configure("TCombobox", fieldbackground="#ecf0f1", background="#3498db")

root = tk.Tk()
Puzzle(root)
root.mainloop()