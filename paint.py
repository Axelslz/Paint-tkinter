import tkinter as tk
from tkinter import colorchooser
import cv2
import numpy as np

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App con Tkinter y OpenCV")

        self.color = 'black'
        self.eraser_color = 'white'
        self.last_x = None
        self.last_y = None

        self.canvas = tk.Canvas(root, bg='white', width=600, height=400)
        self.canvas.pack(pady=20)

        btn_frame = tk.Frame(root)
        btn_frame.pack(fill=tk.BOTH)

        self.line_btn = tk.Button(btn_frame, text="Línea Recta", command=self.use_line)
        self.line_btn.pack(side=tk.LEFT)

        self.polyline_btn = tk.Button(btn_frame, text="Polilínea", command=self.use_polyline)
        self.polyline_btn.pack(side=tk.LEFT)

        self.rectangle_btn = tk.Button(btn_frame, text="Rectángulo", command=self.use_rectangle)
        self.rectangle_btn.pack(side=tk.LEFT)

        self.circle_btn = tk.Button(btn_frame, text="Círculo", command=self.use_circle)
        self.circle_btn.pack(side=tk.LEFT)

        self.eraser_btn = tk.Button(btn_frame, text="Borrador", command=self.use_eraser)
        self.eraser_btn.pack(side=tk.LEFT)

        self.color_btn = tk.Button(btn_frame, text="Color", command=self.choose_color)
        self.color_btn.pack(side=tk.LEFT)

        self.canvas.bind('<Button-1>', self.start_pos)
        self.canvas.bind('<B1-Motion>', self.draw)

        self.active_button = self.polyline_btn
        self.active_button.config(relief=tk.SUNKEN)
        self.draw_tool = 'polyline'

    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def start_pos(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        x, y = event.x, event.y
        if self.draw_tool == 'line':
            self.canvas.create_line((self.last_x, self.last_y, x, y), fill=self.color)
            self.last_x, self.last_y = x, y  # Uncomment to draw continuous lines
        elif self.draw_tool == 'polyline':
            self.canvas.create_line((self.last_x, self.last_y, x, y), fill=self.color)
            self.last_x, self.last_y = x, y
        elif self.draw_tool == 'rectangle':
            self.canvas.create_rectangle(self.last_x, self.last_y, x, y, outline=self.color)
        elif self.draw_tool == 'circle':
            d = ((self.last_x - x) ** 2 + (self.last_y - y) ** 2) ** 0.5
            self.canvas.create_oval(self.last_x - d, self.last_y - d, self.last_x + d, self.last_y + d, outline=self.color)
        elif self.draw_tool == 'eraser':
            self.canvas.create_rectangle((x-10, y-10, x+10, y+10), fill=self.eraser_color, outline=self.eraser_color)
        self.last_x, self.last_y = x, y

if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()
