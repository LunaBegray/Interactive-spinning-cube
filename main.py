import tkinter as tk
from PIL import Image, ImageTk
import math
import numpy as np

class SpinningcubeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Spinning cube")
        self.root.geometry("600x600")  # Window size
        
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="black")
        self.canvas.pack()

        # Load the cube logo
        self.original_image = Image.open("image.png")  # Replace with your image path
        self.image = self.original_image
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

        # Add sliders for controlling the rotation angles
        self.angle_x_slider = tk.Scale(self.root, from_=0, to=2 * math.pi, orient=tk.HORIZONTAL, label="X Rotation", resolution=0.01)
        self.angle_x_slider.set(self.angle_x)
        self.angle_x_slider.pack()

        self.angle_y_slider = tk.Scale(self.root, from_=0, to=2 * math.pi, orient=tk.HORIZONTAL, label="Y Rotation", resolution=0.01)
        self.angle_y_slider.set(self.angle_y)
        self.angle_y_slider.pack()

        self.angle_z_slider = tk.Scale(self.root, from_=0, to=2 * math.pi, orient=tk.HORIZONTAL, label="Z Rotation", resolution=0.01)
        self.angle_z_slider.set(self.angle_z)
        self.angle_z_slider.pack()

        # Button to reset the rotation to default angles
        self.reset_button = tk.Button(self.root, text="Reset Rotation", command=self.reset_rotation)
        self.reset_button.pack()

        self.update_rotation()

    def rotate_3d(self, x, y, z):
        """Rotate points in 3D using rotation matrices."""
        
        # Rotation around X-axis
        rotation_x = np.array([
            [1, 0, 0],
            [0, math.cos(self.angle_x), -math.sin(self.angle_x)],
            [0, math.sin(self.angle_x), math.cos(self.angle_x)]
        ])
        
        # Rotation around Y-axis
        rotation_y = np.array([
            [math.cos(self.angle_y), 0, math.sin(self.angle_y)],
            [0, 1, 0],
            [-math.sin(self.angle_y), 0, math.cos(self.angle_y)]
        ])
        
        # Rotation around Z-axis
        rotation_z = np.array([
            [math.cos(self.angle_z), -math.sin(self.angle_z), 0],
            [math.sin(self.angle_z), math.cos(self.angle_z), 0],
            [0, 0, 1]
        ])
        
        # Applying rotations
        point = np.array([x, y, z])
        point = np.dot(rotation_x, point)
        point = np.dot(rotation_y, point)
        point = np.dot(rotation_z, point)
        
        return point

    def draw_cube(self):
        """Draw the spinning cube symbol on the canvas with 3D effect."""
        self.canvas.delete("all")  # Clear the canvas

        # Define the cube shape (simplified points for demonstration)
        points = [
            (0, 0, 0),  # Example points to represent the  symbol
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 0),
            (1, 0, 1),
            (0, 1, 1),
            (1, 1, 1)
        ]
        
        # Rotate all points in 3D space
        rotated_points = []
        for point in points:
            rotated_point = self.rotate_3d(point[0], point[1], point[2])
            rotated_points.append(rotated_point)

        # Project the 3D points to 2D (simple orthogonal projection)
        projected_points = []
        for point in rotated_points:
            # Simple projection, just dropping the z-axis
            x2d = int(point[0] * 200 + 300)  # Scaling and translating for the canvas
            y2d = int(point[1] * 200 + 300)
            projected_points.append((x2d, y2d))

        # Draw the projected points (for example, connecting them to form a shape)
        for point in projected_points:
            self.canvas.create_oval(
                point[0] - 5, point[1] - 5, point[0] + 5, point[1] + 5,
                fill="orange", outline="white"
            )
        
        # Draw lines between the points to form the wireframe shape
        self.connect_points(projected_points)

    def connect_points(self, points):
        """Connect points with lines to form the wireframe."""
        # Connect each point to the other points to create a wireframe shape
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                self.canvas.create_line(
                    points[i][0], points[i][1], points[j][0], points[j][1],
                    fill="white", width=2
                )

    def update_rotation(self):
        """Update the rotation angles and redraw the cube symbol."""
        # Get the current values from the sliders
        self.angle_x = self.angle_x_slider.get()
        self.angle_y = self.angle_y_slider.get()
        self.angle_z = self.angle_z_slider.get()

        self.draw_cube()  # Redraw the symbol at the new angle

        self.root.after(50, self.update_rotation)  # Update every 50 milliseconds

    def reset_rotation(self):
        """Reset rotation to default values."""
        self.angle_x_slider.set(0)
        self.angle_y_slider.set(0)
        self.angle_z_slider.set(0)

# Set up the Tkinter window and start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SpinningcubeApp(root)
    root.mainloop()
