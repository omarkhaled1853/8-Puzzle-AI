import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from BuzzleSolver.factory import *

class Puzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Game")

        # Configure the main layout with a background color
        self.root.config(padx=10, pady=10, bg='#2c3e50')

        # Configure the main layout to expand vertically and horizontaly
        self.root.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
        self.root.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand

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
            activebackground='#1abc9c', command=self.randomize_board
        )
        randomize_btn.pack(pady=2)

        # custom button for user input board
        custom_input_btn = tk.Button(
            board_control_frame, text="Enter Custom State", font=('Arial', 12), bg='#2980b9', fg='white',
            activebackground='#1abc9c', command=self.show_custom_input_field
        )
        custom_input_btn.pack(pady=2)

        # hidden input field for custom board
        self.custom_input_label = tk.Label(board_control_frame, text="Enter game state", bg='#34495e', fg='white', font=('Arial', 10, 'bold'))
        self.input_entry = tk.Entry(board_control_frame, font=('Arial', 14))
        self.submit_btn = tk.Button(board_control_frame, text="Submit", font=('Arial', 12), bg='#2980b9', fg='white',
            activebackground='#1abc9c', command=self.customize_board
        )
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
        self.algorithm_combo.bind("<<ComboboxSelected>>", self.get_selected_algo)

        # Set ttk theme to match the dark background
        style = ttk.Style()
        style.theme_use('clam')  # Use the 'clam' theme for modern look
        style.configure("TCombobox", fieldbackground="#ecf0f1", background="#3498db")

        # solve button
        solve_btn = tk.Button(
            search_frame, text="Solve", font=('Arial', 12), bg='#2980b9', fg='white',
            activebackground='#1abc9c', command=self.solve_puzzle
        )
        solve_btn.pack(pady=2)
        # ======================== Puzzle output Frame ========================
        output_frame = tk.Frame(self.root, bg='#34495e')
        output_frame.grid(row=3, column=0, pady=10, sticky='ew')

        # Create a Text widget for output display
        self.output_text = tk.Text(output_frame, height=5, width=50, font=('Arial', 12), bg='#ecf0f1', fg='#2c3e50')
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Scrollbar for the Text widget
        self.scrollbar = tk.Scrollbar(output_frame, command=self.output_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Text widget to use the scrollbar
        self.output_text.config(yscrollcommand=self.scrollbar.set)


    # get selected algorithm from combobox
    def get_selected_algo(self, event):
        selected_value = self.algorithm_combo.get()
        print(f"Selected Algorithm: {selected_value}")
    
    # randomize board with update
    def randomize_board(self):
        random.shuffle(self.tiles)
        # update board
        for i in range(9):
            self.tiles[i].grid(row=i // 3, column=i % 3, padx=2, pady=2)

    def show_custom_input_field(self):
        self.custom_input_label.pack(pady=2)
        self.input_entry.pack(pady=2)
        self.submit_btn.pack(pady=2)

    def hide_custom_input_field(self):
        self.custom_input_label.pack_forget()
        self.input_entry.pack_forget()
        self.submit_btn.pack_forget()

    def is_valid_custom_input(self, board):
        if len(board) != 9:
            messagebox.showerror(title="Length Error", message="Invalid input! Please enter exactly 9 characters.")
            return False
        elif not all(c in '012345678' for c in board):
            messagebox.showerror(title="Range Error", message="Invalid input! Please enter characters only from 0 to 8.")
            return False
        elif len(set(board)) != len(board):
            messagebox.showerror(title="Uniqueness Error", message="Invalid input! All numbers must be distinct.")
            return False
        
        return True

    # customize board with update
    def customize_board(self):
        board = self.input_entry.get()
        # check custom input validation
        if self.is_valid_custom_input(board):
            # update board
            for i in range(9):
                # change tile text
                text = board[i] if board[i] != '0' else ''
                self.tiles[i]['text'] = text

                # change tile background color
                bg_color = '#ecf0f1' if board[i] != '0' else '#95a5a6'
                self.tiles[i]['bg'] = bg_color

                # change tile font color
                fg_color = '#2c3e50' if board[i] != '0' else 'white'
                self.tiles[i]['fg'] = fg_color

            # hide the input field and submit button after processing
            self.hide_custom_input_field()
    
    def get_state(self) -> str:
        state = ''
        for tile in self.tiles:
            if tile['text'] == '':
                state += '0'
            else:
                state += str(tile['text'])
        return state

    def solve_puzzle(self):
        # delete previous output if any
        self.output_text.delete(1.0, tk.END)

        # get initial state
        board = self.get_state()
        print(board)
        board = int(board)
        algo = self.algorithm_combo.get()

        technique = Factory.get_technique(algo, intial_state=board)
        
        # perform algorithm
        start = time.time()
        output = technique.solve()
        end = time.time()

        output_str = (
            f"Time: {(end - start) * 1000:.2f} ms\n"
            f"Path to Goal: {output['path_to_goal']}\n"
            f"Cost of Path: {output['cost_of_path']}\n"
            f"Nodes Expanded: {output['nodes_expanded']}\n"
            f"Search Depth: {output['search_depth']}\n"
            f"Path: {output['goal_steps']}\n"
        )

        # insert new output
        self.output_text.insert(tk.END, output_str)

root = tk.Tk()
Puzzle(root)
root.mainloop()